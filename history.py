import pathlib
import re
import time
from typing import *

from PROJECT import PROJECT


# =====================================================================================================================
class ReleaseFileBase:
    # ------------------------------------------------
    FILE_NAME: str = "FILE.md"

    # ------------------------------------------------
    LINE_SEPARATOR_MAIN: str = "*" * 80

    @property
    def filepath(self) -> pathlib.Path:
        return pathlib.Path(self.FILE_NAME)

    # FILE WRITE ======================================================================================================
    def file_clear(self) -> None:
        self.filepath.write_text("")

    def file_append_lines(self, lines: Optional[Union[str, List[str]]] = None) -> None:
        if not lines:
            lines = ""
        if isinstance(lines, str):
            lines = [lines, ]
        with self.filepath.open("a") as fo_append:
            for lines in lines:
                fo_append.write(f"{lines}\n")

    # GROUP ===========================================================================================================
    def lines_create__group(self, lines: List[str], title: str = None) -> List[str]:
        group: List[str] = []

        if title:
            group.append(title.upper())

        for num, line in enumerate(lines, start=1):
            if isinstance(line, list):
                group.append(f"{num}. {line[0]}:  ")
                for block in line[1:]:
                    group.append(f"\t- {block}  ")
            else:
                group.append(f"{num}. {line}  ")
        return group


class History(ReleaseFileBase):
    # ------------------------------------------------
    FILE_NAME: str = "HISTORY.md"

    # ------------------------------------------------
    LINE_SEPARATOR_NEWS: str = "-" * 30
    PATTERN_SEPARATOR_NEWS = r'#+ NEWS:'

    LAST_NEWS: str = ""

    # PREPARE =========================================================================================================
    def check_new_release__is_correct(self) -> bool:
        pattern = r'\n((?:\d+\.?){3}) \((?:\d{2,4}[/:\s]?){6}\)'
        match = re.search(pattern, self.filepath.read_text())
        if match and match[1] == PROJECT.VERSION_STR:
            return False
        return True

    def load_last_news(self) -> None:
        pass

    def lines_create__news(self) -> List[str]:
        group: List[str] = [
            f"## NEWS:",
            "",
            f"{PROJECT.VERSION_STR} ({time.strftime("%Y/%m/%d %H:%M:%S")})",
            self.LINE_SEPARATOR_NEWS,
        ]
        news_new = self.lines_create__group(PROJECT.NEWS)
        group.extend(news_new)
        return group

    def autogenerate(self) -> None:
        if not self.check_new_release__is_correct():
            msg = f"[ERROR] Incorrect new data (change version/...)"
            raise Exception(msg)

        self.load_last_news()
        self.file_clear()
        self.append_main()

    def append_main(self):
        lines = [
            f"# RELEASE HISTORY",
            f"",
            self.LINE_SEPARATOR_MAIN,
            *self.lines_create__group(PROJECT.TODO, "## TODO"),
            f"",
            self.LINE_SEPARATOR_MAIN,
            *self.lines_create__group(PROJECT.FIXME, "## FIXME"),
            f"",
            self.LINE_SEPARATOR_MAIN,
            *self.lines_create__news(),
            f"",
            self.LAST_NEWS,
            self.LINE_SEPARATOR_MAIN,
        ]
        self.file_append_lines(lines)


# =====================================================================================================================
if __name__ == '__main__':
    History().autogenerate()


# =====================================================================================================================
