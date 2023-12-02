# Parses code section groups

from bs4 import BeautifulSoup

from document import *

# Replaces common escaped characters with equivalents
def clean_str(s):
    replacements = [
        ("\\xc2\\xa0", " "),
        ("\\n", " "),
        ("\\xe2\\x80\\x9c", "\""),
        ("\\xe2\\x80\\x9d", "\""),
        ("\\xe2\\x80\\x99", "'"),
        ("\\xe2\\x80\\x93", "-")
    ]

    for pair in replacements:
        s = s.replace(pair[0], pair[1])
    
    return s

class CodeSectionGroup(Document):
    def __init__(self, web_content):
        super().__init__()

        soup = BeautifulSoup(web_content, "html.parser")
        self.text_body = soup.find_all(style="margin:0;display:inline;")
        self.make_paragraphs()

    def make_paragraphs(self):
        for html_par in self.text_body:
            previous = html_par.previous_sibling.previous_sibling
            if previous.name == "h6": # if html paragraph is proceeded by section heading
                section_title = clean_str(previous.string)
                self.add_paragraph(Heading(section_title, 2))

            self.add_paragraph(clean_str(html_par.string))

if __name__ == "__main__":
    with open("raw_content.html", "r") as content_file:
        csg = CodeSectionGroup(content_file)
        csg.export()