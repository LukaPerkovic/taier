import re

from typing import Callable
from collections.abc import Mapping


class TextProcessor:
    """
    Cleans the text. It maps what needs to be removed and what needs to be replaced.
    Removal is a list of characters needed to be removed, while replacement involves a dictionary
    with original and desired value pairs.

    :param replace: Dictionary where key is a string which needs to be replaced, and value
                being the final value. It is possible to also specify a removal via replacment
                by setting value as None.
    :param remove: For explicit removal, this argument accepts a list of targeted items and will
                overwrite the replacement dictionary if it exists.
    :param udfs: Tuple containing custom user defined functions to be applied over text.
    :param udfs_first: If True user defined functions will be applied before replacement and removal.
                       False will apply them as the final step.
    """

    def __init__(
        self,
        replace: Mapping[str, str | None] = {},
        remove: tuple[str] | None = None,
        udfs: tuple[Callable] | None = None,
        udfs_first: bool = True,
        case_insensitive: bool = False,
    ):
        self.udfs = udfs
        self.udfs_first = udfs_first
        self.case_insensitive = case_insensitive

        self._t_map: Mapping[str, str] = {}

        if replace:
            for k, v in replace.items():
                if v is None:
                    v = ""
                self._t_map[str(k)] = str(v)

        if remove:
            self._t_map |= {str(item): "" for item in remove}

    def clean(self, text: str) -> str:

        # Running UDFS in the beginning
        if self.udfs and self.udfs_first:
            for f in self.udfs:
                text = f(text)

        for k, v in self._t_map.items():

            text = re.sub(
                k, v, text, flags=0 if not self.case_insensitive else re.IGNORECASE
            )

        # Running UDFS in the end
        if self.udfs and not self.udfs_first:
            for f in self.udfs:
                text = f(text)

        return text
