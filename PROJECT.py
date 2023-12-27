from typing import *


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_INSTALL: str = "prj-name"
    NAME_IMPORT: str = "prj_name"
    KEYWORDS: List[str] = [
        "kw1",
    ]

    # GIT --------------------------------------------------
    DESCRIPTION_SHORT: str = "descr short (git/prg descr)"

    # README -----------------------------------------------
    DESCRIPTION_LONG: str = "designed for ..."
    FEATURES: List[str] = [
        "feat1",
        ["feat2", "block1", "block2"],
    ]
    WISHES: List[str] = [
        "add ..."
    ]

    # HISTORY -----------------------------------------------
    VERSION: str = "0.0.1"
    NEWS: List[str] = [
        "add ..."
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
