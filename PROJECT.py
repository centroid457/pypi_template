from typing import *
from _aux__release_files import release_files_update


# =====================================================================================================================
# VERSION = (0, 0, 3)   # 1/deprecate _VERSION_TEMPLATE from PRJ object +2/place update_prj here in __main__ +3/separate finalize attrs
VERSION = (0, 0, 4)     # add AUTHOR_NICKNAME_GITHUB for badges


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"
    AUTHOR_NICKNAME_GITHUB: str = "centroid457"

    # PROJECT ----------------------------------------------
    NAME_IMPORT: str = "prj_name"
    KEYWORDS: list[str] = [
        "kw1",
    ]
    CLASSIFIERS_TOPICS_ADD: list[str] = [
        # "Topic :: Communications",
        # "Topic :: Communications :: Email",
    ]

    # README -----------------------------------------------
    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_SHORT: str = "descr short (git/prg descr)"
    DESCRIPTION_LONG: str = """designed for ..."""
    FEATURES: list[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "feat1",
        ["feat2", "block1", "block2"],
    ]

    # HISTORY -----------------------------------------------
    VERSION: tuple[int, int, int] = (0, 0, 0)
    TODO: list[str] = [
        "..."
    ]
    FIXME: list[str] = [
        "..."
    ]
    NEWS: list[str] = [
        "..."
    ]

    # FINALIZE -----------------------------------------------
    VERSION_STR: str = ".".join(map(str, VERSION))
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")


# =====================================================================================================================
if __name__ == '__main__':
    release_files_update(PROJECT)


# =====================================================================================================================
