
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = orders.split(",")

print(len(orders_list))

order_set = set(orders_list)
orders_list = sorted(order_set, reverse=True)

print(orders_list)
