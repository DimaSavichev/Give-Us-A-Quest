import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
pg.init()

current_music = "default"


class Location:
    def __init__(self, name, intro, choices, calls=None, music="default"):
        if calls is None:
            calls = []
        self.name = name
        self.intro = intro
        self.choices = choices
        self.calls = calls
        self.music = music

    def play_music(self):
        global current_music
        if self.music != current_music:
            pg.mixer.music.unload()
            pg.mixer.music.load("music/" + self.music + ".mp3")
            pg.mixer.music.play(-1)
            current_music = self.music


    def list_choices(self):
        for i in range(len(self.choices)):
            print(str(i) + ". " + self.choices[i])

    def find(self, choice):
        return int(choice)  # self.choices.index(choice)  # Todo добавить обработку естествееного языка

    def start(self):
        self.play_music()
        print("Локация: " + self.name)
        print(self.intro)
        print("Ваши действия:")
        self.list_choices()
        choice = input()
        return self.find(choice)

    def __repr__(self):
        return f'Name: {self.name}; Intro: {self.intro}; Choices: {self.choices}; Musix: {self.music}'

    def __str__(self):
        return f'Name: {self.name}; Intro: {self.intro}; Choices: {self.choices}; Musix: {self.music}'


def parseLocations(filename):
    f = open('storylines/locations/' + filename + '.txt', 'r', encoding='utf-8')
    locations = dict()
    data = list()
    for line in f:
        params = line.split('; ')
        params[2] = params[2].split(', ')
        params[3] = params[3].split(', ')
        if params[2][0] == "": params[2] = []
        if params[3][0] == "": params[3] = []
        if params[-1][-1] == '\n': params[-1] = params[-1][:-1]
        location = Location(params[0], params[1], params[2].copy(), music=params[4])
        locations[params[0]] = location
        data.append(params.copy())
    try:
        mod = getattr(__import__('storylines.functions.' + filename), "functions")
        mod = getattr(mod, filename)
        found = True
    except ():
        found = False
    for i in range(len(data)):
        for func in data[i][3]:
            if func == "": break
            if func in locations.keys():
                locations[data[i][0]].calls.append(locations[func])
            elif found and hasattr(mod, func):
                locations[data[i][0]].calls.append(getattr(mod, func))
            else:
                print("Used function/location " + func + " not found")
                return
    return locations


