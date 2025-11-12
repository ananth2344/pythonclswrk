fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Juice", "Soda", "Water"]

fruits.append("Mango")

vegetables.insert(1, "Cabbage")
beverages.pop()

inventory = [fruits, vegetables, beverages]
print("First two fruits:", fruits[:2])

print("Last vegetable:", vegetables[-1])

fruit_lengths = [len(fruit) for fruit in fruits]
print("Lengths of fruits:", fruit_lengths)

print("Is 'Water' in beverages?", "Water" in beverages)

first_items = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items)

print("\nFull Inventory:", inventory)
