import csv
from pathlib import Path


def split_csv_into_chunks(
    input_file: str,
    output_dir: str = "./processed",
    rows_per_file: int = 110,
    encoding: str = "utf-8",
):
    """
    Split a CSV file into smaller chunks with headers.

    Args:
        input_file: Path to input CSV file
        output_dir: Directory for output chunks
        rows_per_file: Number of rows per chunk
        encoding: File encoding
    """

    try:
        input_path = Path(input_file)
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        with open(input_path, newline="", encoding=encoding) as csvfile:
            reader = list(csv.reader(csvfile))
            header = reader[0]
            rows = reader[1:]

        for i in range(0, len(rows), rows_per_file):
            chunk = rows[i : i + rows_per_file]
            chunk_number = (i // rows_per_file) + 1
            output_file = output_path / f"chunk_{chunk_number}.csv"

            with open(output_file, mode="w", newline="", encoding=encoding) as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(chunk)

            print(f"Wrote {output_file} with {len(chunk)} rows")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    input_file = "./processed/filename.csv"  # replace with your actual file path
    split_csv_into_chunks(input_file)
