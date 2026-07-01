# Binance Futures Testnet Trading Bot

## Install

pip install -r requirements.txt

## Add API Keys

Create .env

API_KEY=your_key

API_SECRET=your_secret

## Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000