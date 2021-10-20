from typing import Optional
from janis_core import (
    Array,
    File,
    ToolInput,
    ToolOutput,
    Filename,
    InputSelector,
    ToolArgument,
    Directory,
    String,
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
                "inp_files",
                Array(File),
                position=2,
            ),
            ToolInput(
                "output_dir", String(optional=True), default="output_dir", position=8
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Directory, selector=InputSelector("output_dir"))]

    def arguments(self):
        return [
            ToolArgument("mkdir tmpdir;", position=0, shell_quote=False),
            ToolArgument("cp", position=1, shell_quote=False),
            ToolArgument("tmpdir", position=5, shell_quote=False),
            ToolArgument(";", position=6, shell_quote=False),
            ToolArgument("mv tmpdir", position=7, shell_quote=False),
        ]

    def bind_metadata(self):
        self.metadata.documentation = """gather files to a folder"""
