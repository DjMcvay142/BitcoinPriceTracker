# Bitcoin Price Tracker 

A simple Python application that fetches real-time Bitcoin prices using the CoinGecko API.

## Features

- Real-time Bitcoin prices in USD, GBP, and EUR
- 24-hour price change percentage
- Error handling for network issues

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/BitcoinPriceTracker.git
cd BitcoinPriceTracker
```

2. Install requirements:
```bash
pip install requests
```

## Usage

```bash
python main.py
```

### Example Output
```
Bitcoin Price:
USD: $96,847.52
GBP: £76,234.18
EUR: €91,234.56

24h Change: 2.34%
```

## How It Works

Sends a GET request to the CoinGecko API, parses the JSON response, and displays formatted Bitcoin prices in multiple currencies.

## Technologies

- Python 3.13
- Requests library
- CoinGecko API (free, no auth required)

## Future Improvements

- Add more cryptocurrencies
- GUI with Tkinter
- Historical price charts
- Price alerts
- Discord bot integration

## What I Learned

- Working with RESTful APIs
- HTTP requests with the `requests` library
- JSON data parsing
- Error handling with try-except blocks
- String formatting with f-strings

## Author

Dan - Computing and Information Technology Foundation Year Student at Northumbria University

---

*Part of my Python learning journey - December 2024*
