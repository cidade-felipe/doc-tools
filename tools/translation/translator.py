import os
from pathlib import Path

from dotenv import load_dotenv
from openai import AzureOpenAI, OpenAIError

load_dotenv()


def translate(
   original_language: str,
   target_language: str,
   text: str,
   client: AzureOpenAI,
   deployment: str,
   max_output_tokens: int,

) -> str:
   resposta = client.responses.create(
      model=deployment,
      input=[
         {
               'role': 'system',
               'content': (
                  f'''
                     Translate the following text from {original_language} to {target_language}.
                     Maintain the original formatting, including Markdown syntax, headings, lists, and code blocks.
                     DO NOT translate any code snippets, technical terms, emails, URLs, references, names or similar; keep them in their original form.
                     DO NOT add any additional explanations, comments, or text; only provide the translated content.
                     DO NOT change the structure of the text; preserve paragraphs, line breaks, and formatting as in the original.
                     DO NOT translate any text that is already in {target_language}; leave it unchanged.
                     DO NOT translate any text that is in a language other than {original_language} or {target_language}; leave it unchanged.
                     DO NOT translate literals, numbers, or any other non-textual content; keep them as they are.
                     DO NOT translate literaly, but adapt the text to be natural and fluent in {target_language}, while preserving the original meaning and intent.
                  '''
               ),
         },
         {
               'role': 'user',
               'content': text,
         },
      ],
      max_output_tokens=max_output_tokens,
   )
   try:
      translated_text = (resposta.output_text or '').strip()
   except OpenAIError as e:
      raise RuntimeError(f'Azure OpenAI API error: {e}') from e
   except Exception as e:
      raise RuntimeError(f'Error occurred while translating text: {e}') from e
   if not translated_text:
      raise RuntimeError('Azure OpenAI returned an empty response.')
   return translated_text