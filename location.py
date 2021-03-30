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
        pass  # Todo добавить воспроизведение аудиофайлов

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
        self.calls[self.find(choice)].__call__()

    def __repr__(self):
        print(self.calls)
        return f'Name: {self.name}; Intro: {self.intro}; Choices: {self.choices}; Calls: ; Musixc: {self.music}'

    def __str__(self):
        print(self.calls)
        return f'Name: {self.name}; Intro: {self.intro}; Choices: {self.choices}; Calls: ; Musixc: {self.music}'


def parse(filename):
    f = open('locations/' + filename + '.txt', 'r', encoding='utf-8')
    locations = dict()
    data = list()
    for line in f:
        params = line.split('; ')
        params[2] = params[2].split(', ')
        params[3] = params[3].split(', ')
        if params[-1][-1] == '\n': params[-1] = params[-1][:-1]
        location = Location(params[0], params[1], params[2].copy(), music=params[4])
        locations[params[0]] = location
        data.append(params.copy())
    # print(locations)
    try:
        mod = getattr(__import__('functions.' + filename), filename)
        found = True
    except ():
        found = False
    for i in range(len(data)):
        for func in data[i][3]:
            if func in locations.keys():
                locations[data[i][0]].calls.append(locations[func].start)
            elif found and hasattr(mod, func):
                locations[data[i][0]].calls.append(getattr(mod, func))
                print(locations[data[i][0]].calls)
            else:
                print("Used function/location " + func + " not found")
                return
            # print(locations[data[i][0]])
    return locations


