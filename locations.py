from location import Location, parse


def lol():
    print("wow")

def lel():
    print("wew")

def lul():
    print("wuw")


# home = Location()
# street = Location()
bedroom_intro = "lol bedroom"
bedroom_choices = ["Пойти на работу", "Осаться дома", "Пойти гулять"]
bedroom_music = "Утро"

work_intro = "lol bedroom"
work_choices = ["Пойти на работу", "Осаться дома", "Пойти гулять"]
work_music = "Альтернатива"

bedroom = Location("Спальня", bedroom_intro, bedroom_choices)
work = Location("Работа", "lmao you chose work", ["Die"])


bedroom_calls = [work.start, lol, lul]
work_calls = [bedroom.start]

bedroom.calls = bedroom_calls
work.calls = work_calls
