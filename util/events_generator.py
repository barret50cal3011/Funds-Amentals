import os
import json

# Define the path to the file
file_path = "./data/events.json"

# Check if the file does not exist
if not os.path.isfile(file_path):
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)



# Create an empty list for the events
events = {"events": []}

running = True
while running:
    name = input("Name of the event:\n")
    description = input("Event description:\n")
    writing_stocks = True
    while writing_stocks:
        stock = input("stock_name:\n")
        consequence = input("Conseuence of the event in the stock:\n")
        if input("Is there more stoks to consider?\n") == "n":
            writing_stocks = False
    if(input("Do you wish to continue??\n") == "n"):
        running = False


# Write the events to the file
with open(file_path, "w") as f:
    json.dump(events, f)
