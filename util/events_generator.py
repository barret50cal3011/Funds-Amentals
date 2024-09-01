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
events:dict = {}
stocks:dict = {}

events_description:dict = {}

running_events = True
while running_events:
    name = input("Name of the event, father:\n")
    description = input("Event description:\n")
    writing_sons = True
    events[name] = {}
    events_description[name] = description
    while writing_sons:
        son = input("stock_name:\n")
        consequence = [int(x) for x in input("Conseuence of the event in the stock:\n").split()]
        events.get(name)[son] = consequence
        if input("Is there more stoks to consider?\n") == "n":
            writing_sons = False
    if(input("Do you wish to continue??\n") == "n"):
        running_events = False

running_stocks = True
while running_stocks:
    name = input("Name of the event, father:\n")
    description = input("Event description:\n")
    writing_sons = True
    events[name] = {}
    events_description[name] = description
    while writing_sons:
        stock = input("stock_name:\n")
        consequence = [int(x) for x in input("Conseuence of the event in the stock:\n").split()]
        events.get(name)[stock] = consequence
        if input("Is there more stoks to consider?\n") == "n":
            writing_sons = False
    if(input("Do you wish to continue??\n") == "n"):
        running_stocks = False



hi = [
    "events_description": {
  "War": "A New Conflict has Erupts\nIn a significant escalation of tensions, two countries have entered into open conflict. The hostilities began following a series of incidents that heightened diplomatic strains. This will affect {}, making the value of their actions {}. International leaders are calling for an immediate ceasefire and diplomatic negotiations to resolve the crisis.",
  "Technology Advances": "Breakthrough in Technology Announced \nScientists and engineers have announced a groundbreaking advancement. The new technology promises to revolutionize some process and will optimize others making some products of enterprises better, this could inside the value of stock of {} {}. Experts believe this innovation could have far-reaching implications and pave the way for future developments.",
  "Accident": "Major Accident has occurred\nAuthorities are investigating the cause of the accident, this will have a high repercussion on the confident of the population and investors in {}, this could make their stocks values go down. The enterprise wait to solve this as fast as possible and are asking for calm for their investors",
  "Seasons": "Season Arrives \nThe arrival of a new season brings a change in weather and activities. Residents are enjoying this because they could do many activities with their family, meanwhile local businesses prepare for the seasonal shift, making offers and waiting for the possible sales for this season. This could influence the sales from {} and in their stocks, making her value {}. Meteorologists predict in the coming weeks, encouraging everyone to make the most of the season.",
  "Natural Disasters": "Overwhelming Natural Disaster \nA powerful natural disaster struck unexpectedly close to {} buildings, causing widespread destruction and loss of life. This will affect his operations and could impact in their stock values, making them go down.Rescue teams are working tirelessly to assist those affected, while relief efforts are being coordinated to provide essential supplies and support.",
  "Social Media": "New Social Media Trend Takes by Storm \nA new trend has emerged on social media, captivating users worldwide. It has garnered millions of views and participation from celebrities and influencers. Experts suggest that this trend could influence about the perception that people has in {}, having a  high impact in their stock values making them {}; the experts highlighting the power of social media in shaping public discourse and entertainment."
 }]



events = {'events': events, 'stocks': stocks}


# print(events)
for x in events_description:
    print(events_description[x])

if input("Its okay?") == "y":
    # Write the events to the file
    with open(file_path, "w") as file:
        json.dump(events, file, indent=1)
