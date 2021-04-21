import operator
from typing import Optional, List, Callable, Dict

from janis_core import File
from janis_core.tool.test_classes import TTestExpectedOutput, TTestPreprocessor


class ZipFile(File):
    def __init__(self, optional=False, extension=".zip"):
        super().__init__(optional, extension=extension)

    @staticmethod
    def name():
        return "Zip"

    def doc(self):
        return "A zip archive, ending with .zip"

    @classmethod
    def basic_test(
        cls,
        tag: str,
        min_size: int,
        md5: Optional[str] = None,
        array_index: Optional[int] = None,
    ) -> List[TTestExpectedOutput]:
        outcome = [
            TTestExpectedOutput(
                tag=tag,
                preprocessor=TTestPreprocessor.FileSize,
                operator=operator.ge,
                expected_value=min_size,
                array_index=array_index,
            ),
        ]
        if md5 is not None:
            outcome += [
                TTestExpectedOutput(
                    tag=tag,
                    preprocessor=TTestPreprocessor.FileMd5,
                    operator=operator.eq,
                    expected_value=md5,
                    array_index=array_index,
                ),
            ]
        return outcome

    @classmethod
    def array_wrapper(
        cls,
        tag: str,
        test: Callable,
        list_size: int,
        expected_values: Optional[Dict] = {},
    ) -> List[TTestExpectedOutput]:
        outcome = []
        for i in range(list_size):
            expected_values_for_one_file = {}
            for j in expected_values.keys():
                expected_values_for_one_file[j] = expected_values[j][i]
            try:
                outcome += test(tag=tag, array_index=i, **expected_values_for_one_file)
            except TypeError:
                print("Wrong arguments passed to " + test.__name__)
        return outcome
