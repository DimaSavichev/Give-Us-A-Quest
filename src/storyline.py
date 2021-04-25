from src.location import *
from os import listdir


class StoryLine:
    def __init__(self, name):
        self.locations = parseLocations(name)
        self.config = parseConfig(name)
        self.current_location = self.locations[self.config["first location"]]

    def step(self):
        choice = self.current_location.start()
        if isinstance(self.current_location.calls[choice], Location):
            self.current_location = self.current_location.calls[choice]
        else:
            self.current_location = self.current_location.calls[choice].__call__(self)


def parseConfig(filename):
    f = open('storylines/configs/' + filename + '.txt', 'r', encoding='utf-8')
    config = dict()
    for line in f:
        key, value = line.strip().split(': ')
        config[key.lower()] = value

    return config


def findStorylines():
    files = listdir("storylines/configs")
    storylines = dict()
    for file in files:
        key = parseConfig(file.replace('.txt', ''))["name"]
        storylines[key] = file.replace('.txt', '')

    return storylines
