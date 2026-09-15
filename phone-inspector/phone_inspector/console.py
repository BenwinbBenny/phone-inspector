import os
import platform


def clear_screen() -> None:
    """Clear the terminal screen on Windows, Linux, and macOS."""

    command = "cls" if platform.system() == "Windows" else "clear"
    os.system(command)


def pause(message: str = "Press Enter to continue...") -> None:
    """Pause until the user presses Enter."""

    input(message)
