# Parses code section groups

from bs4 import BeautifulSoup

import document as doc

if __name__ == "__main__":
    with open("raw_content.html", "r") as content_file:
        soup = BeautifulSoup(content_file, "html.parser")

        sections = soup.find_all(style="margin:0;display:inline;")

        my_doc = doc.Document()
        for section in sections:
            my_doc.add_paragraph(section.string)
        print(my_doc)