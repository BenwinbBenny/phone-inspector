from typing import Any

from colorama import Fore, Style


RESET = Style.RESET_ALL

TITLE = Fore.CYAN + Style.BRIGHT
LABEL = Fore.YELLOW + Style.BRIGHT
VALUE = Fore.WHITE
SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
MUTED = Fore.LIGHTBLACK_EX


BANNER = r"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║              P H O N E   I N S P E C T O R           ║
║                                                      ║
║       Lightweight phone-number metadata utility      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""


def print_header() -> None:
    """Display the application header."""

    print(TITLE + BANNER + RESET)
    print(
        MUTED
        + "Enter a number in international format.\n"
        + "Example: +919876543210\n"
        + RESET
    )


def ask_for_number() -> str:
    """Read a phone number from the terminal."""

    return input(
        LABEL + "\nPhone number > " + RESET
    ).strip()


def ask_to_continue() -> bool:
    """Ask whether the user wants to analyze another number."""

    while True:
        answer = input(
            LABEL + "\nAnalyze another number? [y/n] > " + RESET
        ).strip().lower()

        if answer in {"y", "yes"}:
            return True

        if answer in {"n", "no"}:
            print(
                SUCCESS
                + "\nThank you for using Phone Inspector.\n"
                + RESET
            )
            return False

        print(ERROR + "Please enter y or n." + RESET)


def print_result(data: Any, result_type: str) -> None:
    """Print application output."""

    if result_type == "error":
        print(
            "\n"
            + ERROR
            + f"[!] {data}"
            + RESET
        )
        return

    if result_type != "phone":
        print(data)
        return

    zones = ", ".join(data.timezones) if data.timezones else "Unknown"

    status = (
        SUCCESS + "VALID"
        if data.is_valid
        else ERROR + "INVALID"
    )

    possible = (
        SUCCESS + "YES"
        if data.is_possible
        else ERROR + "NO"
    )

    print("\n" + TITLE + "──── Analysis ────" + RESET)

    rows = [
        ("International", data.formatted_number),
        ("Country code", f"+{data.country_code}"),
        ("Region", data.region),
        ("Carrier", data.carrier),
        ("Location", data.location),
        ("Time zone", zones),
        ("Valid number", status),
        ("Possible number", possible),
    ]

    for label, value in rows:
        print(
            f"{LABEL}{label:<18}{RESET}"
            f"{VALUE}{value}{RESET}"
        )

    print(TITLE + "──────────────────" + RESET)
