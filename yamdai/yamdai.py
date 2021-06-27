import sys  # For reading command line arguments
import re  # for string splitting
import misaka  # for converting to html
import hashlib
import genanki
import yamdai.helper as hlpr
import click

def main():
  args = sys.argv[1]  
  # Start processing file

  # foldername depending on OS
  media_folder = 'collection.media\\' if sys.platform == 'win32' else r'collection.media/'

  FILE_PATH = str(args)
  file = open(FILE_PATH, "r")

   # First line of the file is the filename without extension as a level 1 header
  FILE_NAME = file.readline().strip().split('#')[1].strip()

  # The very first line after the top-level header is the deckname
  DECK_NAME = file.readline().strip()

  # Create genanki deck
  DECK = genanki.Deck(hlpr.simple_hash(DECK_NAME), DECK_NAME)

  TAGS = []
  next_line = file.readline()

  # Grab tags
  while(not next_line.startswith("##")):
      current_tags = re.findall(r"[\w:]+", next_line)
      TAGS += current_tags
      next_line = file.readline()

  #### start producing cards

  # next_line here is first front side.
  # Note: In Typora, headers seem to be always single line
  front = next_line.strip().split("##", 1)[1].strip()
  back = ""

  # Process rest, starting with backside of first card
  next_line = file.readline()
  while next_line:
    if(next_line.strip().startswith("##")):
        
        front = hlpr.MD_to_HTML(front, media_folder)
        back = hlpr.MD_to_HTML(back, media_folder)
        
        my_note = genanki.Note(
            model=hlpr.my_model,
            fields=[front, back],
            tags = TAGS)
        DECK.add_note(my_note)
        
        front = next_line.strip().split("##", 1)[1].strip()
        back = ""
    else:
      back = back + next_line

    next_line = file.readline()

  front = hlpr.MD_to_HTML(front, media_folder)
  back = hlpr.MD_to_HTML(back, media_folder)

  # Add final card
  my_note = genanki.Note(
      model=hlpr.my_model,
      fields=[front, back],
      tags = TAGS)
  DECK.add_note(my_note)

  # Export deck as an apkg file
  genanki.Package(DECK).write_to_file(FILE_NAME+".apkg")

  file.close()

if __name__ == '__main__':
  main()
