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