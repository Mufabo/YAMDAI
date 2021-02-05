# YAMDAI

YAMDAI stands for Yet Another Markdown Anki Importer.

It takes a specifically formatted markdown document and builds a deck for the flashcard app Anki.

## Installation

```pip install git+https://github.com/Mufabo/YAMDAI```

## How to create markdown files for YAMDAI

The very first line is a level-1 header and will be the name of the resulting apkg file

The very next line is the name of the deck

the following lines contain tags.

Now start the actual cards.
Frontsides are level 2 headers
The following text is the respective backside.

## How to execute YAMDAI

YAMDAI is executed using the command line:

```python -m yamdai.yamdai Path/to/markdownFile```

The resulting apkg file will be stored in the current working directory.

## Example markdown file

Create a deck called yamdai with a subdeck called subyamdai.
Each note in this deck has the tags tag1 and tag2::subtag1

~~~markdown
# Yamdai_example
yamdai::subyamdai

tag1 tag2::subtag1

## Inline math

$\sum_i \tau$ 

## Display math

$$
\sum_i^\infty \gamma
$$

 ## Just text

Paris is the capitol of France

Berlin is the capitol of Germany

## Image 
Make sure the image is located in Anki's collection.media folder

![Samojed - Wikipedija, prosta enciklopedija](C:\Users\Computer\AppData\Roaming\Anki2\Fatih\collection.media\picture)



## Bullet points

* A
* B
* C

## Code

````python
import numpy as np
print("Hello World!")
````
~~~


