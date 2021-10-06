"""Global monkey patch to print strings correctly."""

from __future__ import print_function

import builtins
import sys
from re import split
from typing import Any, Callable, Generator, Optional, Union

from _io import TextIOWrapper

from l18nprint.constants import MIN_L18N_LEN


class L18NPrinter:
    """Printer monkey patch to write all strings in l18n form"""

    def __init__(self, stream: TextIOWrapper) -> None:
        """
        Initialize the monkey patch printer object.

        :param stream: The default stream to print to.
        """
        self._stream: TextIOWrapper = stream
        self._original_print: Callable = print
        builtins.print = self.print  # typing: ignore

    @classmethod
    def l18n(cls, obj: Any) -> Union[str, bytes, Any]:
        """
        Convert an object to l18n style text.

        :param obj: The object to attempt conversion for.
        """
        if not isinstance(obj, str) and not isinstance(obj, bytes):
            return str(obj)

        if len(obj) <= MIN_L18N_LEN:
            return obj

        if isinstance(obj, bytes):
            try:
                obj = obj.decode("ascii")
            except ValueError:
                return obj

        return "".join(
            map(
                lambda e: f"{e[0]}{len(e[1:-1])}{e[-1]}"
                if e and not e.isspace()
                else e,
                split(r"(\S+)", obj),
            )
        )

    def print(
        self,
        *objects,
        sep: str = " ",
        end: str = "\n",
        file: Optional[TextIOWrapper] = None,
        flush: bool = False,
    ) -> None:
        """
        Prints the values to a stream, or to sys.stdout by default.

        :param file:  a file-like object (stream)
        :param sep:   string inserted between values, default a space
        :param end:   string appended after the last value, default a newline
        :param flush: whether to forcibly flush the stream
        """
        if file is None:
            file = self._stream

        for obj in objects:
            for l18n_obj in self.l18n(obj):
                file.write(l18n_obj)
            file.write(sep)

        file.write(end)

        if flush:
            file.flush()


_printer = L18NPrinter(sys.stdout)
print = _printer.print
