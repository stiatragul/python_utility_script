import win32com.client as win32
import os
import argparse
from datetime import date

def convert_excel_to_pdf(input_filepath):
    """
    Converts an Excel file to a single-page landscape PDF, saving it in the same directory.
    
    Args:
        input_filepath (str): The full path to the input Excel (.xlsx) file.
    """
    absolute_filepath = os.path.abspath(input_filepath)
    
    if not os.path.exists(absolute_filepath):
        print(f"Error: Input file not found at {absolute_filepath}")
        return

    input_directory = os.path.dirname(absolute_filepath)
    today = date.today().strftime("%Y%m%d")
    output_filename = f"2025_AES_Program_{today}.pdf"
    output_filepath = os.path.join(input_directory, output_filename)

    excel = None
    try:
        excel = win32.DispatchEx("Excel.Application")
        excel.Visible = False
        
        workbook = excel.Workbooks.Open(absolute_filepath)
        
        # Select all worksheets
        workbook.Sheets.Select()

        worksheet = workbook.ActiveSheet
        
        # Configure page setup using integer values
        worksheet.PageSetup.Orientation = 2  # 2 corresponds to xlLandscape
        worksheet.PageSetup.Zoom = False
        worksheet.PageSetup.FitToPagesWide = 1
        worksheet.PageSetup.FitToPagesTall = 1
        
        # Save as PDF using the integer value
        workbook.ExportAsFixedFormat(0, output_filepath) # 0 corresponds to xlTypePDF

        print(f"Successfully converted '{os.path.basename(absolute_filepath)}' to '{os.path.basename(output_filepath)}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if excel:
            excel.Quit()
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an Excel file to a single-page landscape PDF.")
    parser.add_argument("excel_file", type=str, help="The path to the Excel file to convert.")
    
    args = parser.parse_args()
    
    convert_excel_to_pdf(args.excel_file)