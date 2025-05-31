# Stock High-Low Visualizer

A simple Python script that fetches **1 month** of stock data using Yahoo Finance and visualizes the **daily high-low price ranges** using Matplotlib.

---

## Project Structure

```
.
├── data/
│   └── data.json          # Output JSON file with stock data
├── script.py              # Main script to fetch data and generate plot
├── pyproject.toml         # Dependency declarations
└── README.md              
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/stock-highlow-visualizer.git
cd stock-highlow-visualizer
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install matplotlib==3.10.3 numpy==2.2.6 pandas==2.2.3 yfinance==0.2.61
```

If you're using a tool like Poetry or Pipenv, the dependencies are listed in `pyproject.toml`.

---

## Usage

Run the script to download stock data and generate the plot:

```bash
python script.py
```

This will:

- Fetch the past month of historical prices for the given stock (default: `AAPL`)
- Save it to `data/data.json`
- Plot daily high-low ranges as vertical lines

---

## ✏️ Configuration

To change the stock ticker:

```python
retrieving_data("TSLA")  # Replace "TSLA" with your desired symbol
```

Make sure the `data/` directory exists before running the script.

---

## Dependencies

- `matplotlib==3.10.3`
- `numpy==2.2.6`
- `pandas==2.2.3`
- `yfinance==0.2.61`
- Python 3.11

---

## Future Ideas

- Add candlestick chart support  
- Export plots as PNG or SVG  
- Add CLI support for dynamic ticker and date input