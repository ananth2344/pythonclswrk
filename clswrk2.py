header = """\n\t*** BOOKSTORE RECEIPT ***
\t-------------------------"""

book1_title = "Python Basics"
book1_price = 450
book2_title = "Data Science Intro"
book2_price = 600

item1 = "\n\tBook Title: {}\t– ₹{}".format(book1_title, book1_price)
item2 = "\n\tBook Title: {}\t– ₹{}".format(book2_title, book2_price)

total = book1_price + book2_price
total_line = "\n\tTOTAL PRICE:\t₹{}".format(total)

thank_you = "\n\n\tTHANK YOU FOR SHOPPING WITH US!"

receipt = (header + item1 + item2 + total_line + thank_you).upper()
print(receipt)
