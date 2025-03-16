import os
import shutil
import subprocess
import tempfile

# Path to the final executable
OUTPUT_EXE = os.path.join(os.getcwd(), "output", "single_program.exe")

# Path to the icons folder
ICON_FOLDER = os.path.join(os.getcwd(), "icons")

def find_icon():
    """Searches for any .ico file in the icons folder"""
    if os.path.exists(ICON_FOLDER):
        icons = [f for f in os.listdir(ICON_FOLDER) if f.endswith(".ico")]
        return os.path.join(ICON_FOLDER, icons[0]) if icons else None
    return None

def clean_crdownload(directory):
    """Removes .crdownload files from the specified folder"""
    for filename in os.listdir(directory):
        if filename.endswith(".crdownload"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"🧹 Removed incomplete file: {file_path}")

def create_executable():
    executables_path = os.path.join(os.getcwd(), "executables")  # Folder with the executables
    if not os.path.exists(executables_path):
        print("❌ ERROR: The 'executables' folder was not found!")
        return

    # Getting the .exe files from the folder
    files = [f for f in os.listdir(executables_path) if f.endswith(".exe")]
    
    if len(files) < 2:
        print("❌ ERROR: Please place at least two .exe files in the 'executables' folder!")
        return
    
    print(f"📂 Files found: {files}")

    # Creating a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Copying the executables to the temporary directory
    for file in files:
        shutil.copy(os.path.join(executables_path, file), temp_dir)

    # Creating a script to execute the extracted files
    with open(os.path.join(temp_dir, "runner.py"), "w", encoding="utf-8") as f:
        f.write(f"""import os, subprocess, sys, shutil, tempfile

temp_path = tempfile.mkdtemp()
files = {files}

# Extract the files to the temporary folder
for file in files:
    with open(os.path.join(temp_path, file), "wb") as out:
        out.write(open(sys._MEIPASS + "/" + file, "rb").read())

# Executes the extracted files
for file in files:
    subprocess.Popen(os.path.join(temp_path, file), shell=True)
""")

    # Searching for an icon in the 'icons' folder
    icon_path = find_icon()

    if icon_path:
        print(f"🎨 Using icon: {icon_path}")
        icon_option = f'--icon="{icon_path}"'
    else:
        print("⚠️ WARNING: No .ico file found in 'icons' folder. The program will be created without an icon.")
        icon_option = ""

    # Creating the executable with PyInstaller
    print("🚀 Creating executable, please wait...")
    
    os.system(f'pyinstaller --onefile --add-data "{temp_dir};." --noconsole {icon_option} {os.path.join(temp_dir, "runner.py")}')

    # Verifying if the executable was created
    runner_exe_path = os.path.join("dist", "runner.exe")
    if not os.path.exists(runner_exe_path):
        print("❌ ERROR: Unable to create the executable.")
        return

    # Ensure the 'output' folder exists
    output_dir = os.path.join(os.getcwd(), "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Remove incomplete files
    clean_crdownload("dist")
    
    # Move the final executable to the output folder
    shutil.move(runner_exe_path, OUTPUT_EXE)

    # Clean up temporary files
    shutil.rmtree("build")
    shutil.rmtree("dist")
    shutil.rmtree(temp_dir)
    os.remove("runner.spec")

    print(f"✅ Executable created and moved to the 'output' folder: {OUTPUT_EXE}")

if __name__ == "__main__":
    create_executable()
