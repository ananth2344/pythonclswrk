grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)
def remove_last_item():
    if grocery_list:  
        grocery_list.pop()

show_item = lambda item: print(f"Item: {item}")
def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

def main():
    add_item("butter")
    remove_last_item()

    print("Grocery List:")
    for item in grocery_list:
        show_item(item)
    
    total_chars = count_characters(grocery_list)
    print(f"\nTotal number of characters in item names: {total_chars}")
main()
