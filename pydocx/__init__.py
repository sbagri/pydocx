from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

import sys

from pydocx.parsers import Docx2Html, Docx2Markdown

__version__ = '0.4.2'


def docx2html(path):
    return Docx2Html(path).parsed


def docx2markdown(path):
    return Docx2Markdown(path).parsed


def main():
    try:
        parser_to_use = sys.argv[1]
        path_to_docx = sys.argv[2]
        path_to_html = sys.argv[3]
    except IndexError:
        print('Must specify which parser as well as the file to convert and the name of the resulting file.')  # noqa
        sys.exit()
    if parser_to_use == '--html':
        html = Docx2Html(path_to_docx).parsed
    elif parser_to_use == '--markdown':
        html = Docx2Markdown(path_to_docx).parsed
    else:
        print('Only valid parsers are --html and --markdown')
        sys.exit()
    if sys.version_info < (3, 0):
        with open(path_to_html, 'w') as f:
            f.write(html.encode('utf-8'))
    else:
        with open(path_to_html, 'wb') as f:
            f.write(html.encode('utf-8'))

if __name__ == '__main__':
    main()
