from datetime import date

import janis_core as j
from .echo import Echo


class HelloWorkflow(j.Workflow):
    def __init__(self):
        super().__init__("hello", doc="A simple hello world example")

        inp = j.Input("inp", j.String(optional=True), default="Hello, world!")
        echo = j.Step("hello", tool=Echo())
        self.add_edge(inp, echo.inp)
        self.add_edge(echo.out, j.Output("out"))

    def friendly_name(self):
        return "Hello, World!"

    @staticmethod
    def tool_module():
        return "unix"

    def metadata(self):
        meta = self._metadata

        meta.version = "v1.0.0"
        meta.maintainer = "Michael Franklin"
        meta.dateUpdated = date(2019, 8, 12)

        meta.documentation = """\
This is the 'Hello, world' equivalent workflow that uses the Echo unix
tool to log "Hello, World!" to the console, and collects the result.

This is designed to be the first example that you can run with janis, ie:
    
``janis run hello``
"""

        return meta
