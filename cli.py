import argparse

from bot.orders import place_order
from bot.validators import validate_side
from bot.validators import validate_order_type


parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)

parser.add_argument("--side", required=True)

parser.add_argument("--type", required=True)

parser.add_argument("--quantity", required=True, type=float)

parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    if order_type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT order requires --price")

    print("\nOrder Request")
    print("----------------")
    print("Symbol :", args.symbol)
    print("Side :", side)
    print("Type :", order_type)
    print("Quantity :", args.quantity)

    if args.price:
        print("Price :", args.price)

    order = place_order(
        args.symbol,
        side,
        order_type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print("----------------")
    print("Order ID :", order.get("orderId"))
    print("Status :", order.get("status"))
    print("Executed Qty :", order.get("executedQty"))
    print("Average Price :", order.get("avgPrice"))

    print("\nOrder Placed Successfully")

except Exception as e:

    print("\nFailed")
    print(e)