from tripdata import get_trip_details
from datetime import datetime
import json

trips = [
    get_trip_details("Paris", "15-05-2023", "Beautiful city with amazing food!"),
    get_trip_details("Tokyo", "10-09-2022", "Loved the culture and technology."),
    get_trip_details("New York", "05-02-2024", "The city that never sleeps!")
]
for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")
json_data = json.dumps(trips, indent=4)
print(json_data)
