from collections.abc import Mapping


class TextProcessor:
    def __init__(self, remove: list = [], replace: dict[str | int, str] = {}):
        self.table = self._make_table(remove, replace)

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__} class with the following cleaning table:\n\n"
            f"{self.table}"
        )

    def _make_table(
        self, remove: list, replace: dict[str | int, str]
    ) -> Mapping[int, str | None]:
        if remove is None and replace is None:
            raise ValueError(
                "Either removal list or replacement list must be provided. "
                "Both cannot be absent!"
            )

        removal_table = str.maketrans({k: None for k in remove})
        replacement_table = str.maketrans(replace)

        return removal_table | replacement_table

    def clean(self, text: str) -> str:
        return text.translate(self.table)
