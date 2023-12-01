class Document:
    def __init__(self):
        self._paragraphs = []

    def add_paragraph(self, content):
        self._paragraphs.append(content)

    def __str__(self):
        separator = "\n\n"
        par_strings = [str(par) for par in self._paragraphs]
        s = separator.join(par_strings)
        return s

class Heading:
    def __init__(self, content: str, level=1):
        self.content = content
        self.level = level

    # In Markdown format
    def __str__(self):
        hashes = "#" * self.level
        s = f"{hashes} {self.content}"
        return s
    
if __name__ == "__main__":
    my_doc = Document()
    my_doc.add_paragraph(Heading("Hello, world."))
    my_doc.add_paragraph("The quick, brown fox jumps over the lazy dog.")

    print(my_doc)