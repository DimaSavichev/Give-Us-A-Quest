STORYLINE_DIR = 'storylines'
LOCATIONS_FILENAME = 'locations.txt'
CONFIG_FILENAME = 'config.txt'
FUNCTIONS_MODULENAME = 'functions'
MUSIC_DIRECTORY = 'music'
DEFAULT_MUSIC_FILENAME = 'default'


def pathToLocations(name):
    return STORYLINE_DIR + '/' + name + '/' + LOCATIONS_FILENAME


def pathToConfig(name):
    return STORYLINE_DIR + '/' + name + '/' + CONFIG_FILENAME


def moduleNameForFunctions(name):
    return STORYLINE_DIR + '.' + name + '.' + FUNCTIONS_MODULENAME


def pathToMusic(name, music_name):
    return STORYLINE_DIR + '/' + name + '/' + MUSIC_DIRECTORY + '/' + music_name + '.mp3'
