from dataclasses import dataclass


@dataclass
class Country:
    """Represents a country that participates in the eurovision song contest."""

    name: str
    """Full name of country in english."""

    abbreviation: str
    """Short name of country."""


class Ranking:
    pass


@dataclass
class Contest:
    """A eurovision song contest instance in one specific year."""

    first_semi: Ranking
    second_semi: Ranking

    final: Ranking


class Eurovision:
    """Basic structure holding all information about the eurovision song contests."""

    contests: list[Contest]
    """List of all ever contests."""
