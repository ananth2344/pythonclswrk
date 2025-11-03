import random

apple_juice = 15.5
orange_juice = 20.0
grape_juice = 10.25

total_volume = apple_juice + orange_juice + grape_juice
print("Total juice sold (in liters):", total_volume)

total_volume_int = int(total_volume)
print("Total juice sold (integer value):", total_volume_int)

total_volume_str = str(total_volume)
print("The total volume of juice sold today is " + total_volume_str + " liters.")

bonus = random.randint(5, 10)
final_total = total_volume + bonus
print("Final total after adding bonus liters:", final_total)
