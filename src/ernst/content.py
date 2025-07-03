"""Load content from content.yaml"""

from pydantic import BaseModel
from enum import StrEnum, auto
import yaml
from pathlib import Path


class CommitCategories(StrEnum):
    """A commit category."""

    FIX = auto()
    FEATURE = auto()
    TEST = auto()
    REFACTOR = auto()


class Commit(BaseModel):
    """A commit message."""

    categories: dict[CommitCategories, list[str]]
    endings: list[str]


class Content(BaseModel):
    """Contains all the offline content for the CLI."""

    advice: list[str]
    joke: list[str]
    roast: list[str]
    commit: Commit
    wait_items: list[str]


FILE_PATH = Path(__file__).parent / "content.yaml"
data = Content.model_validate(yaml.safe_load(FILE_PATH.read_text()))
