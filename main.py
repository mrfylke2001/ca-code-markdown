import urllib.request

import code_section_group as csg

USER_AGENT = "CA Code to Markdown Converter https://github.com/mrfylke2001/ca-code-markdown"

if __name__ == "__main__":
    url = "https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CONS&division=&title=&part=&chapter=&article=I"
    request = urllib.request.Request(
        url,
        data=None,
        headers={
            "User-Agent": USER_AGENT
        }
    )
    content = str(urllib.request.urlopen(request).read())

    with open("raw_content.html", "w") as content_file:
        content_file.write(content)