"""Generate a commit message"""

from .content import data, CommitCategories
import random


def get_commit_message(category: CommitCategories, description: str) -> str:
    """Get a commit message"""
    template = "{category}: {category_str} {description}, {ending}"
    message = template.format(
        category=category.strip(),
        category_str=random.choice(data.commit.categories[category]),
        description=description.strip(),
        ending=random.choice(data.commit.endings),
    )
    return message
