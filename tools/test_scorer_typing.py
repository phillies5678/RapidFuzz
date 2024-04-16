from __future__ import annotations

import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

scorer_test_boilerplate = """
from __future__ import annotations

from rapidfuzz.distance import *

def string_preprocessor(a: str) -> str:
    return a

class MyClass:
    def __init__(self) -> None:
         self.a: str = ""

"""

scorer_test_int = (
    scorer_test_boilerplate
    + """
def test():
    a: int = {scorer}("", "")
    a = {scorer}("", 1)  # type: ignore [call-overload]
    a = {scorer}(1, "")  # type: ignore [call-overload]
    a = {scorer}(list(""), "")
    a = {scorer}("", list(""))
    a = {scorer}("", "", score_cutoff=0.5)  # type: ignore [call-overload]
    a = {scorer}("", "", processor=string_preprocessor)
    a = {scorer}("", list(""), processor=string_preprocessor)  # type: ignore [arg-type]
    a = {scorer}(list(""), "", processor=string_preprocessor)  # type: ignore [arg-type]
    a = {scorer}(MyClass(), MyClass(), processor=lambda x: x.a)
"""
)

scorer_test_float = (
    scorer_test_boilerplate
    + """
def test():
    a: float = {scorer}("", "")
    b: int = {scorer}("", "")  # type: ignore [assignment]
    a = {scorer}("", 1)  # type: ignore [call-overload]
    a = {scorer}(1, "")  # type: ignore [call-overload]
    a = {scorer}(list(""), "")
    a = {scorer}("", list(""))
    a = {scorer}("", "", processor=string_preprocessor)
    a = {scorer}("", list(""), processor=string_preprocessor)  # type: ignore [arg-type]
    a = {scorer}(list(""), "", processor=string_preprocessor)  # type: ignore [arg-type]
    a = {scorer}(MyClass(), MyClass(), processor=lambda x: x.a)
"""
)


def test_scorer(scorer, res_type):
    with TemporaryDirectory() as d:
        f_name = Path(d) / "scorer_test.py"
        with open(f_name, "w") as f:
            if res_type is int:
                f.write(scorer_test_int.format(scorer=scorer))
            else:
                f.write(scorer_test_float.format(scorer=scorer))

        print(f"testing {scorer}")
        subprocess.run(["python", "-m", "mypy", str(f_name), "--warn-unused-ignores"], check=True)


for module in ("DamerauLevenshtein", "Hamming", "Indel", "LCSseq", "Levenshtein", "OSA", "Postfix", "Prefix"):
    test_scorer(f"{module}.distance", int)
    test_scorer(f"{module}.similarity", int)
    test_scorer(f"{module}.normalized_distance", float)
    test_scorer(f"{module}.normalized_similarity", float)

for module in ("Jaro", "JaroWinkler"):
    test_scorer(f"{module}.distance", float)
    test_scorer(f"{module}.similarity", float)
    test_scorer(f"{module}.normalized_distance", float)
    test_scorer(f"{module}.normalized_similarity", float)