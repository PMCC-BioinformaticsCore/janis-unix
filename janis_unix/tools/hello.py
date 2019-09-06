from datetime import date

import janis_core as j
from .echo import Echo

# class Echo(j.CommandTool):
#     @staticmethod
#     def tool():
#         return "echo"
#
#     def friendly_name(self):
#         return "Echo"
#
#     @staticmethod
#     def base_command():
#         return "echo"
#
#     def inputs(self):
#         return [
#             j.ToolInput("inp", j.String(), position=1),
#             j.ToolInput(
#                 "includeNewline",
#                 j.Boolean(optional=True),
#                 prefix="-n",
#                 doc="Do not print the trailing newline character.  This may also be achieved by appending `\c' to "
#                 "the end of the string, as is done by iBCS2 compatible systems.  Note that this option as well as the "
#                 "effect of `\c' are implementation-defined in IEEE Std 1003.1-2001 (``POSIX.1'') as amended by "
#                 "Cor. 1-2002.  Applications aiming for maximum portability are strongly encouraged to use printf(1) "
#                 "to suppress the newline character.",
#             ),
#         ]
#     @staticmethod
#     def tool_module():
#         return "unix"
#
#     @staticmethod
#     def container():
#         return "ubuntu:latest"
#
#     @staticmethod
#     def version():
#         return "v1.0.0"
#
#     def outputs(self):
#         return [j.ToolOutput("out", j.Stdout())]
#
#     def bind_metadata(self):
#         self.metadata.documentation = """\
# The echo utility writes any specified operands, separated by single blank (` ') characters \
# and followed by a newline (`\n') character, to the standard output.
#
# Some shells may provide a builtin echo command which is similar or identical to this utility. \
# Most notably, the builtin echo in sh(1) does not accept the -n option. Consult the builtin(1) manual page."""
#


class HelloWorkflow(j.Workflow):
    def __init__(self):
        super().__init__("hello")

        self.input("inp", j.String(optional=True), default="Hello, world!")
        self.step("hello", Echo, inp=self.inp)
        self.output("out", source=self.hello)

    def friendly_name(self):
        return "Hello, World!"

    @staticmethod
    def tool_module():
        return "unix"

    def bind_metadata(self):

        self.metadata.version = "v1.0.0"
        self.metadata.maintainer = "Michael Franklin"
        self.metadata.dateUpdated = date(2019, 8, 12)

        self.metadata.documentation = """\
This is the 'Hello, world' equivalent workflow that uses the Echo unix
tool to log "Hello, World!" to the console, and collects the result.

This is designed to be the first example that you can run with janis, ie:
    
``janis run hello``
"""


if __name__ == "__main__":
    print(HelloWorkflow().translate("cwl"))
