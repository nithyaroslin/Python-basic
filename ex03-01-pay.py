import sys

try:
    hours = float(input("Enter hours:"))
    rate = float(input("Enter rate:"))
except ValueError:
    print("Error: Please enter numeric Input")
    sys.exit(1)

pay = round(hours * rate,2)
print(f"Pay {pay}")