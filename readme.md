# Money Manager ➔ Beyond Budget Converter

A handy toolkit to help you move your financial life from Money Manager to Beyond Budget — and make the shift to zero-based budgeting as painless as possible.

## Why This Exists

When I first switched from simply tracking expenses in Money Manager to the more intentional world of zero-based budgeting with Beyond Budget, I hit a wall: migrating my old data. So, out of frustration (and a few too many late nights), I built this tool to convert Money Manager's CSV exports into a format that Beyond Budget understands — making the transition smoother for anyone else on the same journey.

## What This Tool Does

- Converts your Money Manager CSV exports into a Beyond Budget-friendly format
- Keeps your full transaction history, with timestamps intact
- Works with both income and expenses
- Can break large CSV files into smaller, more manageable chunks
- Maintains your categories and payment methods
- Adds tags for easier income/expense tracking once imported

## What You'll Need

- Python 3.8 or higher
- A CSV export from Money Manager
- A Beyond Budget account (of course)

## How to Get Started

First, grab the code:

```bash
git clone https://github.com/yourusername/money-manager-to-beyond-budget-converter.git
cd money-manager-to-beyond-budget-converter
```

## How to Use It

1. Export your transactions from Money Manager as a CSV file.
2. Place the exported file in the `sources` directory.
3.Open `mmanager_to_bbudget.py` and update line `120` and `121` with:
    - The name of your exported file
    - What you want to call your new, converted file
4. Run the converter:

```bash
python mmanager_to_bbudget.py
```

For large files, you can split them into chunks:

```bash
python split_to_chunk.py
```

## Project Structure

```
.
├── sources/            # Place your Money Manager CSV exports here
├── processed/          # Converted files will appear here
├── mmanager_to_bbudget.py
└── split_to_chunk.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Thanks To

- [Money Manager](https://www.realbyteapps.com/) by Realbyteapps
- [Beyond Budget](https://www.beyondbudgetapp.com/) App
- The [zero-based budgeting](https://en.wikipedia.org/wiki/Zero-based_budgeting) community for changing how I see money

## Why Zero-Based Budgeting?

Zero-based budgeting has revolutionized my financial planning by ensuring every dollar has a purpose. Unlike traditional budgeting methods that focus on tracking expenses, zero-based budgeting helps you:

- Plan intentionally for every dollar
- Reduce wasteful spending
- Build better saving habits
- Achieve financial goals faster

This converter is here to make that same leap easier for you too.
