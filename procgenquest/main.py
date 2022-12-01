import typer

from typing import Optional

from .quest import QuestApp

app = typer.Typer()


@app.command()
def main(seed: Optional[int] = typer.Argument(None)) -> None:
    quest = QuestApp()
    quest.run()


if __name__ == "__main__":
    app()
