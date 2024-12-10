from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn, TransferSpeedColumn
from rich.console import Console
from rich.theme import Theme

from datetime import datetime

from src.config import configurator


class Prettifier:
    def __init__(self):
        self.theme = Theme({
            "help": "i grey35",
            "info": "bold cyan",
            "data": "magenta",
            "sucess": "spring_green3",
            "warning": "gold1",
            "error": "blink orange_red1",
        })

        self.console = Console(theme=self.theme)
        self.__progress = Progress(SpinnerColumn(), *Progress.get_default_columns(),
                                   TimeElapsedColumn(), TransferSpeedColumn(), transient=True)

    def print(self, text: str, style: str, end: str = "\n", show_time: bool = True) -> None:
        if show_time:
            time = datetime.now().strftime(configurator.time_format)
            self.console.print(f"{time} {text}", style=style, end=end)
        else:
            self.console.print(text, style=style, end=end)

    def get_progress_bar(self):
        return self.__progress


prettifier = Prettifier()
