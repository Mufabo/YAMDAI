import genanki
import hashlib
import misaka
import re
import sys
import pkg_resources
import textwrap
import houdini as h
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.formatters import ClassNotFound
from pygments.lexers import get_lexer_by_name


# https://misaka.61924.nl/
class HighlighterRenderer(misaka.HtmlRenderer):
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter(style='emacs')
            return highlight(text, lexer, formatter)
        # default
        return '\n<pre><code>{}</code></pre>\n'.format(
            h.escape_html(text.strip()))


renderer = HighlighterRenderer()
highlight_markdown = misaka.Markdown(
    renderer, extensions=("fenced-code", "math"))


def MD_to_HTML(field, media_folder):
    """ Takes a MD text as string and returns HTML translation as a string. """

    # $...$     --->  \(...\)
    # $$...$$   --->  \[...\]
    # from ankdwown
    for (sep, (op, cl)) in [("$$", (r"\\[", r"\\]")), ("$", (r"\\(", r"\\)"))]:
        escaped_sep = sep.replace(r"$", r"\$")
        # ignore escaped dollar signs when splitting the field
        field = re.split(r"(?<!\\){}".format(escaped_sep), field)
        # add op(en) and cl(osing) brackets to every second element of the list
        # and remove line breaks.
        field[1::2] = [op + re.sub('\\n', "", e) + cl for e in field[1::2]]
        field = "".join(field)

    # ![...](...collection.media\img.png) ---> ![...](img.png)
    # find everything between media_folder with slashes and )
    regex = media_folder + r'\(.+?)\)' if sys.platform == 'win32' else media_folder + r'(.+?)' + r'\)'
    for img in re.findall(regex, field):
        regs = r'!\[.+?' + r'\]\(.+?' + img + r'\)'
        field = re.sub(regs, r'<img src="' + img + r'">', field)

    return highlight_markdown(field)

# Also from ankdown
def simple_hash(text):
    """MD5 of text, mod 2^63. Probably not a great hash function."""
    h = hashlib.md5()
    h.update(text.encode("utf-8"))
    return int(h.hexdigest(), 16) % (1 << 63)

css_style = """ 
        .card {
            font-family: aerial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
            list-style-position: inside;
            }

    
        """


css_file_path = pkg_resources.resource_filename('yamdai', 'code_highlight.css') 

with open(css_file_path) as css_file:
        css_style += css_file.read().replace('\n', '')

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
    ],
    css=css_style
)
