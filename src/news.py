import random
from typing import Optional, List, Dict
from src.events_m.events_storer import EventsStorer

class News:
    def __init__(self, event_storers: Dict[str, EventsStorer]):
        self.event_storers = event_storers

    def get_news_titles(self) -> List[str]:
        """
        Gets the headlines of all available news based on current events. 
        """
        headlines = []
        for storer in self.event_storers.keys():
            active_events = storer.get_active_sons()
            for event in active_events:
                headlines.append(f"Breaking News: {event.get_event_name()}!")
        return headlines

    def get_news_article(self, event_name: str) -> Optional[str]:
        """
        Gets the news article for a particular event.
        """
        for storer in self.event_storers.keys():
            for event in storer.get_active_sons():
                if event.get_event_name() == event_name:
                    return f"{event.get_event_name()}: {event.description}"
        return None
