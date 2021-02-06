# YAMDAI

YAMDAI stands for Yet Another Markdown Anki Importer.

It takes a specifically formatted markdown document and builds a deck for the flashcard app Anki.
See below for an example

There are already several markdown to anki converters (ankdown, MDanki, markdown-to-anki...).
I didn't like how those handled tags, thus my own version.

## Installation

### Windows

From the command line:

```pip install git+https://github.com/Mufabo/YAMDAI```

### Linux

Requires !(houdini)[https://pypi.org/project/houdini/]

At the moment it gives an error when running on Linux.
I am working on it

## How to create markdown files for YAMDAI

The first line is a level-1 header (line starts with #) and will be the name of the resulting apkg file

The next line is the name of the deck. 
If you want to use a subdeck separate parent deck with double colons from subdecks.

The following lines contain tags. 
Subtags are separated using double colons.
The usage of sub-tags probably requires the respective add-on.
All tags will be used for all cards.

Now start the actual cards.
Frontsides are level 2 headers (lines start with ##)
The following text is the respective backside.

Yamdai supports...
* images as long as they are stored in ankis collection.media folder.
* code highlighting
* inline math
* display math
* bullet points

## How to execute YAMDAI

YAMDAI is executed using the command line:

```python -m yamdai.yamdai Path/to/markdownFile```

The resulting apkg file will be stored in the current working directory.
The apkf file can be imported from within Anki by clicking on File and then choosing
import or CTRL+SHIFT+I from within Anki

## Example markdown file

This example creates a deck called yamdai with a subdeck subyamdai.
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


