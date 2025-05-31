import csv
from typing import Tuple
from pathlib import Path
from decimal import Decimal
from datetime import datetime


class MoneyManagerConverter:
    """
    Handles conversion of Money Manager (https://www.realbyteapps.com/) export \
        files to Beyond Budget (https://www.beyondbudgetapp.com/) format.
    """

    DATE_FORMAT_FULL = "%m/%d/%Y %H:%M:%S"
    DATE_FORMAT_DATE = "%m/%d/%Y"

    FIELDNAMES = [
        "Date",
        "Payment Mode",
        "Category",
        "Amount",
        "Note",
        "Type",
        "Tag",
    ]  # Header names for the output CSV

    @staticmethod
    def format_date(date_string: str) -> Tuple[str, str]:
        """
        Format date string and extract time if available.

        Args:
            date_string: Input date string

        Returns:
            Tuple of (formatted_date, time_string)
        """

        if not isinstance(date_string, str):
            raise ValueError("Date input must be a string")

        try:
            if len(date_string) >= 19:
                dt_obj = datetime.strptime(
                    date_string, MoneyManagerConverter.DATE_FORMAT_FULL
                )
                return dt_obj.strftime(
                    MoneyManagerConverter.DATE_FORMAT_DATE
                ), dt_obj.strftime("%H:%M:%S")
            else:
                dt_obj = datetime.strptime(
                    date_string, MoneyManagerConverter.DATE_FORMAT_DATE
                )
                return (
                    dt_obj.strftime(MoneyManagerConverter.DATE_FORMAT_DATE),
                    "No time data",
                )
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}") from e

    @classmethod
    def convert_file(cls, input_path: str, output_path: str) -> None:
        """
        Convert Money Manager (https://www.realbyteapps.com/) export file \
            to Beyond Budget (https://www.beyondbudgetapp.com/) format.

        Args:
            input_path: Path to input CSV file
            output_path: Path to output CSV file
        """

        input_ppath = Path(input_path)  # type: ignore
        output_ppath = Path(output_path)  # type: ignore

        if not input_ppath.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        output_ppath.parent.mkdir(parents=True, exist_ok=True)

        with open(input_ppath, "r") as input_file, open(
            output_ppath, "w", newline=""
        ) as output_file:

            reader = csv.DictReader(input_file)
            writer = csv.DictWriter(output_file, fieldnames=cls.FIELDNAMES)
            writer.writeheader()

            for row in reader:
                try:
                    date, time = cls.format_date(row["Date"])
                    amount = Decimal(row["Amount"])

                    # modify/extend rows however you want :-)
                    new_row = {
                        "Date": date,
                        "Payment Mode": row["Account"],
                        "Category": row["Category"],
                        "Amount": (
                            f"-{amount:.2f}"
                            if row["Income/Expense"].lower() == "expense"
                            else f"{amount:.2f}"
                        ),
                        "Note": f"Time: {time} —— {row['Description']}",
                        "Type": row["Income/Expense"],
                        "Tag": (
                            "Money In"
                            if row["Income/Expense"].lower() == "income"
                            else "Money Out"
                        ),
                    }
                    writer.writerow(new_row)

                except (ValueError, KeyError) as e:
                    print(f"Error processing row: {row}. Error: {str(e)}")


if __name__ == "__main__":
    converter = MoneyManagerConverter()
    converter.convert_file(
        input_path="./sources/filename.csv",
        output_path="./processed/filename.csv",
    )
