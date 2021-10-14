from janis_core import (
    Array,
    File,
    ToolInput,
    ToolOutput,
    Filename,
    InputSelector,
    ToolArgument,
)
from janis_unix.data_types import Tsv
from .unixtool import UnixTool


class TransposeTsv(UnixTool):
    def tool(self):
        return "TransposeTsv"

    def friendly_name(self):
        return "TransposeTsv"

    def base_command(self):
        return None

    def inputs(self):
        return [
            ToolInput("inp", Tsv, position=2),
            ToolInput(
                "outputFilename",
                Filename(
                    InputSelector("inp", remove_file_extension=True),
                    suffix=".transposed",
                    extension=".tsv",
                ),
                prefix=">",
                position=3,
            ),
        ]

    def outputs(self):
        return [ToolOutput("out", Tsv, selector=InputSelector("outputFilename"))]

    def arguments(self):
        return [
            ToolArgument(
                'echo "BEGIN { FS=OFS="\t" }\
{ printf "%s%s", (FNR>1 ? OFS : ""), $ARGIND }\
ENDFILE {\
    print ""\
    if (ARGIND < NF) {\
        ARGV[ARGC] = FILENAME\
        ARGC++\
    }\
}" > tst.awk;',
                position=0,
                shell_quote=True,
            ),
            ToolArgument("awk -f tst.awk ", position=1, shell_quote=False),
        ]

    def bind_metadata(self):
        self.metadata.documentation = """transpose tsv file"""
