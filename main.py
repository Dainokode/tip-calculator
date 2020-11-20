print("Welcome to the Tip Calculator")

bill = float(input("How much is the bill?"))

tip = int(input("How much would you like to tip: 10, 12, 15?"))

people = int(input("How many people are splitting the bill?"))

tip_percent = tip / 100

total_tip = bill * tip_percent

total_bill = bill + total_tip

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

message = f"Each person should pay: {final_amount}"

print(message)
