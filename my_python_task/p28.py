#car insurance premium calculator

category = input("Enter Category (A/B/C): ").upper()
car_value = float(input("Enter Car Value: "))

match category:
    case "A":
        premium = car_value * 0.02
    case "B":
        premium = car_value * 0.03
    case "C":
        premium = car_value * 0.05
    case _:
        premium = 0
        print("Invalid Category")

if premium > 0:
    print("Insurance Premium =", premium)