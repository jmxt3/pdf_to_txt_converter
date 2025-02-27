"""

██████╗░██████╗░███████╗  ████████╗░█████╗░  ████████╗███████╗██╗░░██╗████████╗
██╔══██╗██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
██████╔╝██║░░██║█████╗░░  ░░░██║░░░██║░░██║  ░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░
██╔═══╝░██║░░██║██╔══╝░░  ░░░██║░░░██║░░██║  ░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░
██║░░░░░██████╔╝██║░░░░░  ░░░██║░░░╚█████╔╝  ░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░
╚═╝░░░░░╚═════╝░╚═╝░░░░░  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

██████╗░██╗░░░██╗  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗███████╗████████╗███████╗
██╔══██╗╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗██║░░██║██╔════╝╚══██╔══╝██╔════╝
██████╦╝░╚████╔╝░  ██╔████╔██║███████║██║░░╚═╝███████║█████╗░░░░░██║░░░█████╗░░
██╔══██╗░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██╔══╝░░░░░██║░░░██╔══╝░░
██████╦╝░░░██║░░░  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║███████╗░░░██║░░░███████╗
╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝

This script converts PDF files to text files using the docling library.

The script performs the following operations:
1. Scans the 'assets' directory for PDF files
2. Creates an 'output' directory if it doesn't exist
3. Converts each PDF file to text using the DocumentConverter from docling
4. Saves the converted text in the 'output' directory with the same filename but .txt extension
5. Handles errors during conversion and reports them

Requirements:
- docling library must be installed
- PDF files should be placed in the 'assets' directory
- Output files will be created in the 'output' directory
"""

import os
from pathlib import Path
from docling.document_converter import DocumentConverter


def convert_pdfs_to_txt():
    """
    Convert all PDF files from the assets directory to text files.

    The function looks for PDF files in the 'assets' directory relative to the script location,
    converts them to text using docling's DocumentConverter, and saves the output as .txt files
    in the 'output' directory. Any conversion errors are caught and reported.

    No parameters required.
    No return value.
    """
    # Get the current directory and assets folder path
    current_dir = Path(__file__).parent
    assets_dir = current_dir / "assets"

    # Create output directory if it doesn't exist
    output_dir = current_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Initialize document converter
    converter = DocumentConverter()

    # Loop through all PDF files in assets directory
    for pdf_file in assets_dir.glob("*.pdf"):
        try:
            print(f"Converting {pdf_file.name}...")

            # Convert PDF using docling
            result = converter.convert(str(pdf_file))
            text_content = result.document.export_to_text()

            # Create output file path
            output_file = output_dir / f"{pdf_file.stem}.txt"

            # Write text content to file
            with open(output_file, "w", encoding="utf-8") as txt_file:
                txt_file.write(text_content)

            print(f"Successfully converted {pdf_file.name} to {output_file.name}")

        except Exception as e:
            print(f"Error converting {pdf_file.name}: {str(e)}")


if __name__ == "__main__":
    convert_pdfs_to_txt()
