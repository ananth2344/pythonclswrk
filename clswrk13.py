filename = "items.txt"
new_item = input("Enter the name of the new item: ")

try:
    with open(filename, "r"):
        pass

    with open(filename, "a") as file:
        file.write(new_item + "\n")

except FileNotFoundError:
    with open(filename, "w") as file:
        file.write(new_item + "\n")

print("\nCurrent list of items:")
with open(filename, "r") as file:
    items = file.readlines()
    for item in items:
        print(item.strip())
