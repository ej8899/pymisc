import os


candies = {}

while True:
    candy_name = input("Enter candy name (or 'done' to finish): ")
    if candy_name == "done":
        break
    candy_quantity = int(input("Enter candy quantity: "))
    candies[candy_name] = candy_quantity

os.system('cls' if os.name == 'nt' else 'clear')
print("Candy distribution:")
for candy, quantity in candies.items():
    print(candy + ": " + " ☐" * quantity)
