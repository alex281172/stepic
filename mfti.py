import re

print("Вы вышли на улицу. Что вы будете делать?")

while True:
    answer = input()
    if re.fullmatch(".*откр.*зонт.*", answer.lower()):
        print("Вы забыли зонт дома. Что вы будете делать дальше?")
    elif re.fullmatch(".*выйт.*", answer):
        print("Вы вышли от сюда. До свидания!")
        break
    elif re.fullmatch(".*(идт|иду|напр|передв|вернул|пой(д|т)).*магазин.*", answer.lower()):
        print("Вы пришли в магазин. Что вы там будете делать?")
        while True:
            answer = input()
            if re.fullmatch(".*вернут*|улиц|выйти.*", answer.lower()):
                print("Вы снова на улице")
                break
            elif re.fullmatch(".*(выбир|осматр|подбир).*продукт.*", answer.lower()):
                print("Вы видите хлеб, молоко и кофемашину. Мда, не густо....")
            elif (re.fullmatch(".*взять\s(\w)+.*", answer.lower())):
                matchs = re.search("взять\s(\w)+", answer.lower())
                if matchs:
                    if (matchs[0] == "взять хлеб"):
                        print("Хлеб взяли")
                    elif (matchs[0] == "взять молоко"):
                        print("Пакет оказался порван. Взяли другой пакет")
                    elif (matchs[0] == "взять кофемашину"):
                        print("Она слишком дорогая")
                    else:
                        print("Я не могу ", matchs[0], " этого нет на полке")
                else:
                    print("Не понятно, что именно вы хотите взять")
