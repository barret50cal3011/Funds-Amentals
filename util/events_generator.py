import os
import json

# Define the path to the file
file_path = "./data/events.json"

# Check if the file does not exist
if not os.path.isfile(file_path):
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)



# Reference
# events:dict = {"War": Events(event_name="War", event_duration=12, event_percentage_range=(-30, 40)),
#               "Technology Advances": Events(event_name="Technology Advances", event_duration=4, event_percentage_range=(-20, 50)), 
#               "Accident": Events(event_name="Accident", event_duration=6, event_percentage_range=(-50, -10)), 
#               "Seasons": Events(event_name="Seasons", event_duration=3, event_percentage_range=(-10, 60)), 
#               "Natural Disasters": Events(event_name="Natural Disasters", event_duration=1, event_percentage_range=(-20, -5)), 
#               "Social Media": Events(event_name="Social Media", event_duration=2, event_percentage_range=(-60, 80))}




# Create an empty dict for the events
events_trends:dict = {}

events_description:dict = {}

running = True
while running:
    name = input("Name of the event:\n")
    description = input("Event description:\n")
    writing_stocks = True
    events_trends[name] = {}
    events_description[name] = description
    while writing_stocks:
        stock = input("stock_name:\n")
        consequence = [int(x) for x in input("Conseuence of the event in the stock:\n").split()]
        events_trends.get(name)[stock] = consequence
        if input("Is there more stoks to consider?\n") == "n":
            writing_stocks = False
    if(input("Do you wish to continue??\n") == "n"):
        running = False


events = {'events': events_trends, 'events_description': events_description}

# print(events)
for x in events_description:
    print(events_description[x])

if input("Its okay?") == "y":
    # Write the events to the file
    with open(file_path, "w") as f:
        json.dump(events, f, indent=1)
