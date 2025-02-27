# PDF to Text Converter
A Python script that converts PDF files to text using the docling library. This tool is designed to batch process PDF files, making it easy to extract text content from multiple documents at once.

## Features

- Automatically processes all PDF files in the `assets` directory
- Creates text output files in the `output` directory
- Maintains the original filename (with .txt extension)
- Handles conversion errors gracefully
- Reports conversion progress and status

## Requirements

- Python 3.x
- docling library
- Virtual environment (included in the repository)

## Project Structure

```
docling_converter/
├── assets/            # Place PDF files here
├── output/           # Converted text files appear here
├── env/             # Virtual environment
├── main.py          # Main conversion script
└── README.md        # This file
```

## Setup

1. Ensure Python 3.x is installed on your system
2. Activate the virtual environment:
   - Windows: `.\env\Scripts\activate`
   - Unix/MacOS: `source env/bin/activate`

## Usage

1. Place your PDF files in the `assets` directory
2. Run the script:
   ```
   python main.py
   ```
3. Find the converted text files in the `output` directory

## How It Works

The script uses the `docling` library's `DocumentConverter` to process PDF files. For each PDF file in the `assets` directory, it:

1. Creates an output directory if it doesn't exist
2. Converts the PDF content to text
3. Saves the text with the same filename (but .txt extension) in the output directory
4. Reports success or any errors encountered

## Error Handling

The script includes error handling for individual file conversions. If a file fails to convert, the script:
- Prints an error message with the specific file name
- Continues processing remaining files
- Maintains a log of any conversion failures