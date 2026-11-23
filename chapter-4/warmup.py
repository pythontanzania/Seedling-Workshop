school = "Kilele Primary School"
desks = 40
price = 12500
print(school)
print(desks + 10)
print(desks * price)

target = 500000
pledges = [
    {"name": "Juma", "amount": 100000, "paid": 100000},
    {"name": "Neema", "amount": 50000, "paid": 20000},
    {"name": "Baraka", "amount": 150000, "paid": 0},
    {"name": "Amina", "amount": 75000, "paid": 75000},
]
print(pledges[0]["name"])

total_paid = 0
for p in pledges:
    total_paid = total_paid + p["paid"]
print("Paid so far:", total_paid)
print("Percent:", total_paid * 100 // target)

for p in pledges:
    if p["paid"] >= p["amount"]:
        print(p["name"], "has paid in full")
    else:
        print(p["name"], "still owes", p["amount"] - p["paid"])

def balance(pledge):
    return pledge["amount"] - pledge["paid"]

print(balance(pledges[1]))
