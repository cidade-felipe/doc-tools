def divide_into_blocks(text: str, limit: int) -> list[str]:
   paragraphs = text.split('\n\n')
   blocks = []
   current_block = ''

   for paragraph in paragraphs:
      candidate = f'{current_block}\n\n{paragraph}'.strip()

      if len(candidate) > limit and current_block:
         blocks.append(current_block)
         current_block = paragraph
      else:
         current_block = candidate  

   if current_block:
      blocks.append(current_block)

   return blocks