# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot developed for the Binance Futures Testnet (USDT-M). It provides a simple command-line interface (CLI) to place Market and Limit orders while following a clean project structure, input validation, logging, and exception handling.

## Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Support for **BUY** and **SELL** order sides
* Command-line interface using `argparse`
* Input validation for order type and side
* Structured project architecture
* Logging of API requests, responses, and errors
* Exception handling for invalid inputs, API errors, and network failures

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── trading_bot.log
```

## Prerequisites

* Python 3.10 or later
* Binance Futures Testnet account
* Binance Futures Testnet API Key
* Binance Futures Testnet Secret Key

## Installation

Clone the repository:

```bash
git clone https://github.com/ParkaviSM/trading_bot.git
```

Navigate to the project folder:

```bash
cd trading_bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_SECRET_KEY
```

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Sample Output

The application displays:

* Order request summary
* Order ID
* Order status
* Executed quantity
* Average execution price (when available)
* Success or failure message

## Logging

All API requests, responses, and errors are recorded in:

```text
trading_bot.log
```

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Missing limit price
* Binance API exceptions
* Network-related exceptions
* Invalid user input

## Assumptions

* The user has an active Binance Futures Testnet account.
* API credentials are valid.
* The selected trading symbol is supported by Binance Futures Testnet.
* Internet connectivity is available while placing orders.

## Dependencies

* python-binance
* python-dotenv

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Author

**S. M. Parkavi**

GitHub: https://github.com/ParkaviSM
