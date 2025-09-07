import logging
import sys
from typing import List

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("commaLog.txt")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def format_list(items: List[str]) -> str:
    """
    Format a list of strings into a human-readable comma-separated string.

    Example:
        ["apples", "bananas", "cherries"] -> "apples, bananas and cherries"
    """
    if not items:
        return ""

    if len(items) == 1:
        return items[0]

    return ", ".join(items[:-1]) + " and " + items[-1]


def collect_items() -> List[str]:
    """
    Collect items interactively from the user until an empty input is given.
    Returns:
        A list of entered items.
    """
    items = []
    first_item = input("Enter the first item of your list (leave empty to exit): ").strip()

    if not first_item:
        print("Empty list. Exiting program.")
        logger.info("User exited without entering items.")
        sys.exit()

    items.append(first_item)

    while True:
        item = input(f"Enter item {len(items) + 1} (leave empty to finish): ").strip()
        if not item:
            break
        items.append(item)

    return items


def main() -> None:
    """Main program entry point."""
    logger.debug("Program started")
    items = collect_items()
    formatted = format_list(items)
    print(f"Your list: {formatted}")
    logger.debug("Program finished")


if __name__ == "__main__":
    main()
