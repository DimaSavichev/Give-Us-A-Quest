from src.location import parseLocations, Location
from src.config import pathToConfig, STORYLINE_DIR
from os import listdir


class StoryLine:
    def __init__(self, name):
        self.locations = parseLocations(name)
        self.config = parseConfig(name)
        self.current_location = self.locations[self.config["first location"]]

    def step(self):
        if self.current_location == self.locations[self.config["last location"]]:
            self.current_location.start(False)
            return True

        choice = self.current_location.start()
        if isinstance(self.current_location.calls[choice], Location):
            self.current_location = self.current_location.calls[choice]
        else:
            self.current_location = self.current_location.calls[choice].__call__(self)
        return False

def parseConfig(filename):
    f = open(pathToConfig(filename), 'r', encoding='utf-8')
    config = dict()
    for line in f:
        key, value = line.strip().split(': ')
        config[key.lower()] = value

    return config


def findStorylines():
    dirs = listdir(STORYLINE_DIR)
    storylines = dict()
    for directory in dirs:
        key = parseConfig(directory)["name"]
        storylines[key] = directory

    return storylines
