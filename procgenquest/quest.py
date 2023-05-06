from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, TextLog

from .widgets import EventLog, CharacterSheet
from .generators import CaveGenerator


class QuestApp(App):
    """Main app to play the game."""

    BINDINGS = [
        ("ctrl+q", "quit", "Quit app"),
        ("ctrl+d", "toggle_dark", "Toggle dark mode"),
    ]

    CSS_PATH = "../resources/app.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(EventLog(id="log"), Vertical(CharacterSheet(), id="sheet"))
        yield Footer()

    def on_ready(self) -> None:
        text_log = self.query_one(TextLog)
        cave_gen = CaveGenerator()
        text_log.write(cave_gen.show())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
