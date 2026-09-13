from docling.document_converter import DocumentConverter

def convert_to_md(input_file: str, output_file: str):
   """
   Converts a document to Markdown format.

   Args:
      input_file (str): The path to the input document file.
      output_file (str): The path to the output Markdown file.
   """
   converter = DocumentConverter()
   converter.convert(input_file, output_file, output_format='md')
   
def convert_to_txt(input_file: str, output_file: str):
   """
   Converts a document to plain text format.

   Args:
      input_file (str): The path to the input document file.
      output_file (str): The path to the output plain text file.
   """
   converter = DocumentConverter()
   converter.convert(input_file, output_file, output_format='txt')
   
def convert_to_html(input_file: str, output_file: str):
   """
   Converts a document to HTML format.

   Args:
      input_file (str): The path to the input document file.
      output_file (str): The path to the output HTML file.
   """
   converter = DocumentConverter()
   converter.convert(input_file, output_file, output_format='html')
   
def convert_to_pdf(input_file: str, output_file: str):
   """
   Converts a document to PDF format.

   Args:
      input_file (str): The path to the input document file.
      output_file (str): The path to the output PDF file.
   """
   converter = DocumentConverter()
   converter.convert(input_file, output_file, output_format='pdf')

