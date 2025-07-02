"""Generate a commit message"""

from .content import data, CommitCategories
import random


def get_commit_message(category: CommitCategories, description: str) -> str:
    """Get a commit message"""
    template = random.choice(data.commit.templates)
    message = template.format(
        category=random.choice(data.commit.categories[category]),
        description=description,
        ending=random.choice(data.commit.endings),
    )
    return message
