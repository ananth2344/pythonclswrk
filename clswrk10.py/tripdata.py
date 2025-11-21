def get_trip_details(city, date, comment):
    """
    Returns trip details as a dictionary.
    city: str
    date: str (in format dd-mm-yyyy)
    comment: str
    """
    return {
        "city": city,
        "date": date,
        "comment": comment
    }
