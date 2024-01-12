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
    def _file_clear(self) -> None:
        self.filepath.write_text("")

    def _file_append_lines(self, lines: Optional[Union[str, List[str]]] = None) -> None:
        if not lines:
            lines = ""
        if isinstance(lines, str):
            lines = [lines, ]
        with self.filepath.open("a") as fo_append:
            for lines in lines:
                fo_append.write(f"{lines}\n")

    # GROUP ===========================================================================================================
    def _lines_create__group(self, lines: List[str], title: Optional[str] = None, nums: bool = True) -> List[str]:
        group: List[str] = []

        if title:
            group.append(title.upper())

        for num, line in enumerate(lines, start=1):
            if nums:
                bullet = f"{num}. "
            else:
                bullet = "- "

            if isinstance(line, list):
                group.append(f"{bullet}{line[0]}:  ")
                for block in line[1:]:
                    group.append(f"\t- {block}  ")
            else:
                group.append(f"{bullet}{line}  ")
        return group


# =====================================================================================================================
class History(ReleaseFileBase):
    # ------------------------------------------------
    FILE_NAME: str = "HISTORY.md"

    # ------------------------------------------------
    LINE_SEPARATOR_NEWS: str = "-" * 30
    PATTERN_SEPARATOR_NEWS = r'#+ NEWS:\s*'
    PATTERN_NEWS = r'#+ NEWS:\s*(.+)\s*\*{10,}\s*'
    # PATTERN_NEWS = r'\n((?:\d+\.?){3} \((?:\d{2,4}[/:\s]?){6}\).*)\s*\*{10,}'

    LAST_NEWS: str = ""

    # PREPARE =========================================================================================================
    def _load_last_news(self) -> None:
        string = self.filepath.read_text()

        # # VAR 1 --------------------------------
        # match = re.search(self.PATTERN_NEWS, string)
        # if match:
        #     self.LAST_NEWS = match[1]
        # # VAR 1 --------------------------------

        # VAR 2 --------------------------------
        splits = re.split(self.PATTERN_SEPARATOR_NEWS, string)
        if len(splits) > 1:
            self.LAST_NEWS = splits[-1]

            splits = re.split(r'\s*\*{10,}\s*', self.LAST_NEWS)
            self.LAST_NEWS = splits[0]
            # VAR 2 --------------------------------

        # print(f"{string=}")
        # print(f"{self.LAST_NEWS=}")

    def _check_new_release__is_correct(self) -> bool:
        # ----------------------------
        if self.LAST_NEWS.startswith(f"{PROJECT.VERSION_STR} ("):
            msg = f"exists_version"
            print(msg)
            return False

        # ----------------------------
        for news_item in PROJECT.NEWS:
            if re.search(r'- ' + str(news_item) + r'\s*\n', self.LAST_NEWS):
                msg = f"exists_news"
                print(msg)
                return False

        # ----------------------------
        return True

    # WORK ============================================================================================================
    def _lines_create__news(self) -> List[str]:
        group: List[str] = [
            f"## NEWS:",
            "",
            f"{PROJECT.VERSION_STR} ({time.strftime("%Y/%m/%d %H:%M:%S")})",
            self.LINE_SEPARATOR_NEWS,
        ]
        news_new = self._lines_create__group(PROJECT.NEWS, nums=False)
        group.extend(news_new)
        return group

    def autogenerate(self) -> None:
        # PREPARE --------------------------------------
        self._load_last_news()
        if not self._check_new_release__is_correct():
            msg = f"[ERROR] Incorrect new data (change version/...)"
            raise Exception(msg)

        # WRITE ----------------------------------------
        self._file_clear()
        self._append_main()

    def _append_main(self):
        lines = [
            f"# RELEASE HISTORY",
            f"",
            self.LINE_SEPARATOR_MAIN,
            *self._lines_create__group(PROJECT.TODO, "## TODO"),
            f"",
            self.LINE_SEPARATOR_MAIN,
            *self._lines_create__group(PROJECT.FIXME, "## FIXME"),
            f"",
            self.LINE_SEPARATOR_MAIN,
            *self._lines_create__news(),
            f"",
            self.LAST_NEWS,
            f"",
            self.LINE_SEPARATOR_MAIN,
        ]
        self._file_append_lines(lines)


# =====================================================================================================================
if __name__ == '__main__':
    History().autogenerate()


# =====================================================================================================================
