def interest(x, y, z):
    formula = (x * y * z) / 100
    return formula

value = float(input("Enter value: "))
percentage = float(input("Enter percentage: "))
time = float(input("Enter year: "))

interest_earned = interest(value, percentage, time)

print(f"\nInterest Earned: {interest_earned}")
print(f"Principle Amount: {value}")
print(f"Total value: {value + interest_earned}")
