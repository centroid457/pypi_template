import pathlib
from typing import *


# =====================================================================================================================
STR_SEPARATOR: str = "## USAGE EXAMPLES"


# =====================================================================================================================
file_readme = pathlib.Path("README.md")

dirpath = pathlib.Path("examples")
files = [item for item in dirpath.iterdir() if item.is_file()]
print(files)      #[WindowsPath('examples/example1.py')]


result_lines: List[str] = []
for line in

for file in files:


# =====================================================================================================================
