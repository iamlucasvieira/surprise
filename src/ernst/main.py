import typer
from .jokes import get_joke
from typing import Annotated
from .content import CommitCategories
from .commit import get_commit_message

ASCII_ART = """
    A CLI that's actually funny!\n
    ╔═══╗╔═══╗╔═╗ ╔╗╔═══╗╔════╗ \n
    ║╔══╝║╔═╗║║║╚╗║║║╔═╗║║╔╗╔╗║ \n
    ║╚══╗║╚═╝║║╔╗╚╝║║╚══╗╚╝║║╚╝ \n
    ║╔══╝║╔╗╔╝║║╚╗║║╚══╗║  ║║   \n
    ║╚══╗║║║╚╗║║ ║║║║╚═╝║  ║║   \n
    ╚═══╝╚╝╚═╝╚╝ ╚═╝╚═══╝  ╚╝   \n
"""
app = typer.Typer(no_args_is_help=True, help=ASCII_ART)


@app.command()
def joke(
    word: Annotated[
        str,
        typer.Option(
            help="A word to search for a related joke",
            prompt="Enter a word",
        ),
    ],
) -> None:
    """
    Get a joke based on a single search word
    """
    # Validate that input is a single word
    if len(word.split()) > 1:
        typer.echo(
            "Whoa there! That's more words than a dad telling a story about 'back in my day'. Let's keep it to just one word!"
        )
        raise typer.Exit(1)

    joke = get_joke(word)
    typer.echo(joke.joke)


@app.command()
def commit(
    category: Annotated[
        CommitCategories,
        typer.Option(
            help="The category of the commit",
            prompt="Enter a category",
        ),
    ],
    description: Annotated[
        str,
        typer.Option(
            help="What did you work on?",
            prompt="What did you work on?",
        ),
    ],
):
    """
    Get a commit message
    """
    typer.echo("")
    typer.secho(get_commit_message(category, description), fg=typer.colors.GREEN)
    typer.echo("")


@app.command()
def message():
    """
    Print a surprise message
    """
    typer.echo("\n")
    typer.secho(
        """
    ╦ ╦╔═╗╔═╗╔═╗╦ ╦  ╔╗ ╦╦═╗╔╦╗╦ ╦╔╦╗╔═╗╦ ╦┬
    ╠═╣╠═╣╠═╝╠═╝╚╦╝  ╠╩╗║╠╦╝ ║ ╠═╣ ║║╠═╣╚╦╝│
    ╩ ╚╩ ╩╩  ╩   ╩   ╚═╝╩╩╚══╩═╩ ╩═╩╝╩ ╩ ╩ o
    """,
        fg=typer.colors.GREEN,
        bold=True,
    )
    typer.echo("""
    You're aging like legacy code:
    1. hard to maintain
    2. full of wisdom
    3. and still running in production

    """)


if __name__ == "__main__":
    app()
