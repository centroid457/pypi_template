import pathlib
import re
from typing import *


# =====================================================================================================================
SEPARATOR_PATTERN = r'(\**\n+)*## USAGE EXAMPLES'

STARS_WRAPPER = "*" * 80
STARS_FILE_SEPARATOR = "*" * 30

LINE_EXAMPLES_START: str = f"\n\n{STARS_WRAPPER}\n## USAGE EXAMPLES (autogenerated)\nSee tests and sourcecode for other examples.\n\n"
LINE_FILE_HEADER: str = "```python\n"
LINE_FILE_FOOTER: str = "```\n"
LINE_SEPARATOR_FILE: str = f"{STARS_FILE_SEPARATOR}\n"
LINE_EXAMPLES_FINISH: str = f"{STARS_WRAPPER}\n"

# =====================================================================================================================
file_readme = pathlib.Path("README.md")
file_readme_text: str = file_readme.read_text().strip()
file_readme_splited = re.split(pattern=SEPARATOR_PATTERN, string=file_readme_text, maxsplit=1)
if len(file_readme_splited) > 1:
    file_readme.write_text(file_readme_splited[0])


# =====================================================================================================================
dirpath = pathlib.Path("examples")
files = [item for item in dirpath.iterdir() if item.is_file()]

# NOTE: don't skip none-python files! it could be as part of examples! just name it in appropriate way!

with file_readme.open("a") as file_readme_append:
    file_readme_append.write(LINE_EXAMPLES_START)

    for index, file in enumerate(files, start=1):
        file_readme_append.write(LINE_SEPARATOR_FILE)
        file_readme_append.write(f"### {index}. {file.name}\n")

        file_readme_append.write(LINE_FILE_HEADER)
        file_readme_append.write(f"{file.read_text().strip()}\n")
        file_readme_append.write(LINE_FILE_FOOTER)
    file_readme_append.write(LINE_EXAMPLES_FINISH)


# =====================================================================================================================
