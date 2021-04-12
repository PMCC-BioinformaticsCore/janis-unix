import operator
from typing import Optional

from janis_core import File
from janis_core.tool.test_classes import TTestExpectedOutput, TTestPreprocessor


class TextFile(File):
    def __init__(self, optional=False, extension=".txt"):
        super().__init__(optional, extension=extension)

    @staticmethod
    def name():
        return "TextFile"

    def doc(self):
        return "A textfile, ending with .txt"

    @classmethod
    def basic_test(
        cls,
        tag: str,
        min_size: int,
        content: str,
        line_count: int,
        md5: Optional[str] = None,
    ):
        outcome = [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.ge,
                expected_value=min_size,
            ),
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.FileContent,
                operator=operator.contains,
                expected_value=content,
            ),
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.LineCount,
                operator=operator.eq,
                expected_value=line_count,
            ),
        ]
        if md5 is not None:
            outcome += [
                TTestExpectedOutput(
                    tag=tag,
                    preprocessor=TTestPreprocessor.FileMd5,
                    operator=operator.eq,
                    expected_value=md5,
                ),
            ]
        return outcome
