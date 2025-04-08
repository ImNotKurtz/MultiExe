# MultiExe

**MultiExe** is a Python tool that allows you to bundle multiple `.exe` files into a single executable. This makes it easier to distribute and run multiple applications as one package. MultiExe extracts and runs the files in a temporary directory at runtime, making the process more efficient and straightforward.

## Features

- Bundle multiple executables into a single file.
- Extract and execute files at runtime.
- Uses PyInstaller and optionally UPX for compression.

## Technologies Used

- **Python**: Main programming language.
- **PyInstaller**: For building the executables.
- **UPX** (optional): For executable compression.

## Project Image

![MultiExe Image](https://media.discordapp.net/attachments/1359212742489149494/1359236286166208682/image.png?ex=67f6bef0&is=67f56d70&hm=1ec4a8cb3cd4536cccf8aefc602c75b7afcd40d3baf585dbb5437fc5e575e6ae&=&format=webp&quality=lossless&width=1654&height=827)


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ImNotKurtz/MultiExe.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MultiExe
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Build the executable:
    ```bash
    python multi_exe.py
    ```

## Contribution

Feel free to contribute! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
    ```bash
    git checkout -b my-feature
    ```
3. Make your changes and submit a pull request.

## License

This project is licensed under the MIT License.
