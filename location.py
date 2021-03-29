class Location:
    def __init__(self, name, intro, choices, calls=[], music="default"):
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

