"""Module for getting advice."""

from .content import data

import random


def get_advice(roast_chance: float = 0.6) -> str:
    """Return a random advice or roast.

    Args:
        roast_chance: The chance to return a roast.
    """

    if random.random() < roast_chance:  # 60% chance to roast
        return random.choice(data.roast)
    return random.choice(data.advice)
