from janis_core import (
    Array,
    File,
    ToolInput,
    ToolOutput,
    Filename,
    InputSelector,
    ToolArgument,
    Directory,
)

from .unixtool import UnixTool


class GatherFilesToFolder(UnixTool):
    def tool(self):
        return "GatherFilesToFolder"

    def friendly_name(self):
        return "GatherFilesToFolder"

    def base_command(self):
        return None

    def inputs(self):
        return [
            ToolInput(
                "inp",
                Array(File),
                prefix="cp",
                separate_value_from_prefix=False,
                position=1,
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Directory, selector="output_folder")]

    def arguments(self):
        return [
            ToolArgument("mkdir output_folder;", position=0, shell_quote=False),
            ToolArgument("output_folder", position=2, shell_quote=False),
        ]

    def bind_metadata(self):
        self.metadata.documentation = """gather files to a folder"""
