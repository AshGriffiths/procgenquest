from textual.app import ComposeResult
from textual.widgets import Static, TabbedContent, TabPane, DataTable, TextLog, Label


class EventLog(Static):
    """A container for a TextLog to track what is going on."""

    def compose(self) -> ComposeResult:
        yield Label("World", id="log_title")
        yield TextLog(id="text_log")


class CharacterSheet(Static):
    """A container for the character's stats and skills."""

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Stats", id="stats"):
                yield DataTable()
            with TabPane("Skills", id="skills"):
                yield DataTable()
