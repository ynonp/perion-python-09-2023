import io
from typing import Pattern
import re

text = io.StringIO("""hello - don't print me
HELLO - but I'm ok
Im a line that shouldn't be printed
BUT I'm a line that should""")

pat = re.compile(r'^[A-Z]+\b')

for line in text:
    if pat.search(line):
        print(line)


def rename_by_pattern(input_format: str, output_format: str, filenames: list[str]) -> list[str]:
    pass

