def calculate_change(amount_paid, total_bill):
    change = amount_paid - total_bill
    return change  
bill_amount = 2.50
money_given = 4.00
vishals_change = calculate_change(money_given, bill_amount)
print(f"The shopkeeper should return: ${vishals_change:.2f}")