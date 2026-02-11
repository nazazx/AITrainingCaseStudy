# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`

from numbers import Real

def calculate_average_order_value(orders):
    total = 0
    count = 0
    
    for order in orders:
        if order.get("status") != "cancelled":
            amount = order.get("amount")
            if amount is None:
                continue
            if not isinstance(amount,Real):
                continue
            
            total += amount
            count += 1
    
    if count == 0:
        return None
    
    return total / count
