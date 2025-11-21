def is_valid_title(title):
    """Check if title has only alphabets and spaces."""
    return title.replace(" ", "").isalpha()


def is_valid_year(year):
    return year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))


try:
    title = input("Enter the book title: ")

    if not is_valid_title(title):
        raise ValueError("Error: Title must contain only alphabets and spaces.")
    year = input("Enter the publication year (e.g., 1998, 2015): ")
    if not is_valid_year(year):
        raise ValueError("Error: Year must be a 4-digit number starting with '19' or '20'.")

    print("\nBook added successfully!")
    print(f"Title: {title}")
    print(f"Publication Year: {year}")

except ValueError as e:
    print(e)

finally:
    print("\nProgram finished — thank you for using the mini library system!")
