import random
import math

names_input = input("Enter the names of invited guests (comma-separated): ")

names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))
selected_name = random.choice(unique_names)
reversed_name = selected_name[::-1]
count_unique = len(unique_names)

sqrt_rounded = round(math.sqrt(count_unique))
print("\n--- Game Results ---")
print(f"Unique names: {unique_names}")
print(f"Total unique names: {count_unique}")
print(f"Rounded square root: {sqrt_rounded}")
print(f"Selected name: {selected_name}")
print(f"Reversed selected name: {reversed_name}")
