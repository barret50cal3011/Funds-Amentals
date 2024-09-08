import os
import json

# Define the path to the file
file_path = "./data/events.json"

# Check if the file does not exist
if not os.path.isfile(file_path):
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


# Create an empty dict for the events
events:dict = {}
stocks:dict = {}

events_description:dict = {}



running_events_type =True

while running_events_type:
    events_type: str = input("Name of the event type:\n") 
    events[events_type] = {}
    running_events =True

    while running_events:
        event_name = input("Name of the event, father:\n")
        events.get(events_type)[event_name] = []

        running_events_sons =True
        while running_events_sons:
            event_son_duration: float = float(input("Duration of the event:\n"))
            event_son_percentage_range: tuple = tuple(input("Range of the percentage of the event:\n").split())
            event_name_son = input("Name of the event (affected_stock):\n")
            weight: float = float(input("Weight of the event:\n"))
            actives: float = float(input("Actives from the stock:\n"))
            events.get(events_type).get(event_name).append(event_son_duration, event_son_percentage_range, weight, event_name_son, actives)

            if input("Do you want to add another son event?") == "n":
                running_events_sons = False
        
        if input("Do you want to add another event?") == "n":
                running_events = False



# TODO Stocks will be defined in the future, when we know all his atributtes values



events_description = {
"War": "A New Conflict has Erupts\nIn a significant escalation of tensions, two countries have entered into open conflict. The hostilities began following a series of incidents that heightened diplomatic strains. This will affect {}, making the value of their actions {}. International leaders are calling for an immediate ceasefire and diplomatic negotiations to resolve the crisis.",
"Technology Advances": "Breakthrough in Technology Announced \nScientists and engineers have announced a groundbreaking advancement. The new technology promises to revolutionize some process and will optimize others making some products of enterprises better, this could inside the value of stock of {} {}. Experts believe this innovation could have far-reaching implications and pave the way for future developments.",
"Accident": "Major Accident has occurred\nAuthorities are investigating the cause of the accident, this will have a high repercussion on the confident of the population and investors in {}, this could make their stocks values go down. The enterprise wait to solve this as fast as possible and are asking for calm for their investors",
"Seasons": "Season Arrives \nThe arrival of a new season brings a change in weather and activities. Residents are enjoying this because they could do many activities with their family, meanwhile local businesses prepare for the seasonal shift, making offers and waiting for the possible sales for this season. This could influence the sales from {} and in their stocks, making her value {}. Meteorologists predict in the coming weeks, encouraging everyone to make the most of the season.",
"Natural Disasters": "Overwhelming Natural Disaster \nA powerful natural disaster struck unexpectedly close to {} buildings, causing widespread destruction and loss of life. This will affect his operations and could impact in their stock values, making them go down.Rescue teams are working tirelessly to assist those affected, while relief efforts are being coordinated to provide essential supplies and support.",
"Social Media": "New Social Media Trend Takes by Storm \nA new trend has emerged on social media, captivating users worldwide. It has garnered millions of views and participation from celebrities and influencers. Experts suggest that this trend could influence about the perception that people has in {}, having a  high impact in their stock values making them {}; the experts highlighting the power of social media in shaping public discourse and entertainment."
}



stocks_description = {



}


events = {'events': events, 'stocks': stocks, 'events_description': events_description, 'stocks_description': stocks_description}


# print(events)
for x in events_description:
    print(events_description[x])

if input("Its okay?") == "y":
    # Write the events to the file
    with open(file_path, "w") as file:
        json.dump(events, file, indent=1)
