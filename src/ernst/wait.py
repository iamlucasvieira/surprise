"""Module for creating wait messages"""

from .content import data

import random
import time
from rich.progress import Progress


def get_wait_message(seconds: int) -> str:
    """Return a random wait message"""
    return random.choice(data.wait_items)


def render_wait_progress(seconds: int) -> None:
    """Render a progress bar for the wait command"""
    with Progress() as progress:
        task = progress.add_task("Procrastinating productively...", total=seconds)

        for value in range(seconds):
            # Print messages to the progress console (above the progress bar)
            if (value + 1) % 5 == 0:
                progress.console.print(f"[bold blue]- {get_wait_message(value)}")

            time.sleep(1)
            progress.advance(task)
