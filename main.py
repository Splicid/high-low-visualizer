import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import json
import asyncio

def retrieving_data(ticker):
    data = yf.Ticker(ticker)
    formatted_data = pd.DataFrame(data.history(period='1mo'))
    dd_j = formatted_data.to_json(orient="index", date_format="iso", indent=2)

    with open("data/data.json", "w") as file:
        file.write(dd_j)

    create_plot()


def create_plot():
    with open("data/data.json", "r") as file:
        data = json.load(file)

    fig, ax = plt.subplots(figsize=(10, 5))

    print([entry["High"] for entry in data.values()])

    highs = [entry["High"] for entry in data.values()]
    lows = [entry["Low"] for entry in data.values()]

    for i, (low, high) in enumerate(zip(lows, highs)):
        ax.plot([i, i], [low, high], color='red')  

    ax.set_title("Daily High-Low Ranges")
    ax.set_xlabel("Day Index")
    ax.set_ylabel("Price")
    plt.tight_layout()
    plt.show()


retrieving_data("AAPl")