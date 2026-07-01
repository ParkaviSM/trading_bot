from binance.enums import *
from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    try:

        logger.info(
            f"Request: {symbol} {side} {order_type} {quantity} {price}"
        )

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

        else:

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )

        logger.info(order)

        return order

    except Exception as e:

        logger.error(str(e))

        raise