from dataclasses import dataclass


@dataclass
class Country:
    """Represents a country that participates in the eurovision song contest."""

    name: str
    """Full name of country in english."""

    abbreviation: str
    """Short name of country."""


@dataclass
class Contest:
    """A eurovision song contest instance in one specific year."""


class Eurovision:
    contests: list[Contest]
