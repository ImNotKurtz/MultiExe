import os
import shutil
import subprocess
import tempfile

# Final output file path
OUTPUT_EXE = os.path.join(os.getcwd(), "output", "programa_unico.exe")

def clean_crdownload(directory):
    # Remove any .crdownload files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".crdownload"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"🧹 Removed incomplete file: {file_path}")

def create_executable():
    executables_path = os.path.join(os.getcwd(), "executaveis")  # Path to the executables folder
    if not os.path.exists(executables_path):
        print("❌ ERROR: The 'executaveis' folder was not found!")
        return

    # Getting all .exe files from the executables folder
    files = [f for f in os.listdir(executables_path) if f.endswith(".exe")]
    
    if len(files) < 2:
        print("❌ ERROR: Please place at least two .exe files in the 'executaveis' folder!")
        return
    
    print(f"📂 Files found: {files}")

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Copy the .exe files to the temporary directory
    for file in files:
        shutil.copy(os.path.join(executables_path, file), temp_dir)

    # Creating a Python script to run the executables after extraction
    with open(os.path.join(temp_dir, "runner.py"), "w", encoding="utf-8") as f:
        f.write(f"""import os, subprocess, sys, shutil, tempfile

temp_path = tempfile.mkdtemp()
files = {files}

# Extract the files to the temporary folder
for file in files:
    with open(os.path.join(temp_path, file), "wb") as out:
        out.write(open(sys._MEIPASS + "/" + file, "rb").read())

# Execute the extracted files
for file in files:
    subprocess.Popen(os.path.join(temp_path, file), shell=True)
""")

    # Creating the executable with PyInstaller
    print("🚀 Creating executable, please wait...")
    os.system(f'pyinstaller --onefile --add-data "{temp_dir};." --noconsole {os.path.join(temp_dir, "runner.py")}')

    # Checking if the executable was created in the dist folder
    runner_exe_path = os.path.join("dist", "runner.exe")
    if not os.path.exists(runner_exe_path):
        print("❌ ERROR: Unable to create the executable.")
        return

    # Ensure the 'output' folder exists
    output_dir = os.path.join(os.getcwd(), "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Cleaning up incomplete files, such as .crdownload
    clean_crdownload("dist")
    
    # Moving the final executable to the output folder
    shutil.move(runner_exe_path, OUTPUT_EXE)

    # Cleaning up temporary files
    shutil.rmtree("build")
    shutil.rmtree("dist")
    shutil.rmtree(temp_dir)
    os.remove("runner.spec")

    print(f"✅ Executable created and moved to the 'output' folder: {OUTPUT_EXE}")

if __name__ == "__main__":
    create_executable()
