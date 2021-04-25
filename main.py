from src.storyline import *
storylines = findStorylines()
print("Добро пожаловать в игру Дайте Квест (!). Выберите сценарий, в который вы хотите сыграть")
for key in storylines.keys():
    print(key)

while True:
    c = input()
    try:
        storyline = StoryLine(storylines[c])
        break
    except:
        print("Кажется вы ошиблись и такого сценария пока нет :с Попробуйте снова")

while True:
    storyline.step()