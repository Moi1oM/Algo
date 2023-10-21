PERIOD = 10
PRINCIPAL = 5000.00
amount = PRINCIPAL
interest_rate = 0.11
year = 0

def compute_interest(year, amount):
    value = amount + interest_rate * amount
    year = year + 1
    amount = value
    return year, amount


while year <= PERIOD:
    print(year, amount)
    year, amount = compute_interest(year, amount)
