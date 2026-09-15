from phone_inspector.analyzer import PhoneAnalyzer
from phone_inspector.console import clear_screen, pause
from phone_inspector.ui import (
    print_header,
    print_result,
    ask_for_number,
    ask_to_continue,
)


def run() -> None:
    """Start the Phone Inspector application."""

    clear_screen()
    print_header()

    analyzer = PhoneAnalyzer()

    while True:
        raw_number = ask_for_number()

        if not raw_number:
            print_result("No phone number was entered.", "error")
            continue

        try:
            result = analyzer.inspect(raw_number)
            print_result(result, "phone")
        except ValueError as exc:
            print_result(str(exc), "error")
        except Exception:
            print_result(
                "An unexpected error occurred while processing the number.",
                "error",
            )

        if not ask_to_continue():
            break

        clear_screen()
        print_header()

    pause("Press Enter to close...")


if __name__ == "__main__":
    run()
