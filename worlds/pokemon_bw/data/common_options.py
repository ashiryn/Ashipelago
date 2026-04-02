import typing

from Options import OptionSet, OptionError


class CasefoldOptionSet(OptionSet):
    valid_keys_casefold = True

    def __init__(self, value: typing.Iterable[str]):
        self.value = set(val.casefold() for val in value)
        super(OptionSet, self).__init__()

    def __contains__(self, item: str):
        return item.casefold() in self.value

    def verify_keys(self) -> None:
        if self.valid_keys:
            dataset = set(word.casefold() for word in self.value)
            extra = dataset - set(key.casefold() for key in self._valid_keys)
            if extra:
                raise OptionError(
                    f"Found unexpected key {', '.join(extra)} in {getattr(self, 'display_name', self)}. "
                    f"Allowed keys: {self._valid_keys}."
                )

class PlandoEncounter(typing.NamedTuple):
    map: str
    seasons: list[str]
    method: str
    slots: list[int]
    species: list[str]