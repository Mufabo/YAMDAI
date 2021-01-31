import genanki
import hashlib
import misaka
import re
import sys


# TODOS
# backslash becomes double backslash when reading file.

# < ---> &lt;
# > ---> &gt;
# & ---> &amp;

# Turn $...$ into \(...\)
# and

# $$...$$

# into \[...\]

# Helper functions


# # TestFile
# test::subdeck
# tag1  tag2::subtag
#    tag3
# 
# 
# ## This text here should be < > &

# $$
# \Lambda = \sum_i^\infty
# $$


# ![image-20210122114046628](C:\Users\Computer\AppData\Roaming\Anki2\Fatih\collection.media\image-20210117093000871.png)

# $\Lambda = \sum_i^\infty$

# ````python
# import numpy as np
# print("hi")

# ````

# ------------------------------------------------------

# <div>This text here should be &lt; &gt; &amp;<br><\div>

# <div>
# \[
# \Lambda = \sum_i^\infty
# \]<br>
# <br>
# <img src="image-20210117093000871.png">
# <br>
# \(\Lambda = \sum_i^\infty\)
# </div>
def MD_to_HTML(field, media_folder):
    """ Takes a MD text as string and returns HTML translation string. """

    # $...$     --->  \(...\)
    # $$...$$   --->  \[...\]
    # From ankdown
    for (sep, (op, cl)) in [("$$", (r"\\[", r"\\]")), ("$", (r"\\(", r"\\)"))]:
        escaped_sep = sep.replace(r"$", r"\$")
        field = re.split(r"(?<!\\){}".format(escaped_sep), field) 
        # add op(en) and cl(osing) brackets to every second element of the list
        field[1::2] = [op + e + cl for e in field[1::2]] 
        field = "".join(field)
    # > ---> &gt;
    # < ---> &lt;
    # done by misaka

    # \n ---> <br>

    # ![...](...collection.media\img.png) ---> ![...](img.png)
    # conversion to html by misaka
    regex = media_folder + r'\(.+?)\)'
    for img in re.findall(regex, field):
        regs = r'\]\(.+?'+ img + r'\)'
        field = re.sub(regs, r"\]\(" + img + r"\)", field)

    return misaka.html(field, extensions=["math", "fenced-code"])



# IMG_HTML = lambda x: \
#   "<img src=\"" + re.split(media_folder, x)[-1] + "\">"

def simple_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    h = hashlib.md5()
    h.update(text.encode("utf-8"))
    return int(h.hexdigest(), 16) % (1 << 63)


# From genanki readme
my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        }
    ]
)
