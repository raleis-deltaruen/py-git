import csv
from tabulate import tabulate

pizzas = []
with open("regular.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pizzas.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})

print(tabulate(pizzas, headers="keys", tablefmt="grid"))