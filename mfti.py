import re

print("Вы вышли на улицу. Можно идти в магазин, можно в парк. Куда пойдете?")



while True:
    answer = input('ваш выбор: ')
    if re.fullmatch(".*(вый(т|ш)|закон|отмен|выхож|выход).*", answer):
        print("Вы вышли от сюда. До свидания!")
        break
    elif re.fullmatch(".*(идт|иду|напр|передв|вернут|пой(д|т)).*магазин.*", answer.lower()):
        print("Вы пришли в магазин. Что вы там будете делать?")
        while True:
            answer = input('ваш выбор: ')
            if re.fullmatch(".*(вернут|выйти|выход).*", answer.lower()):
                print("Вы снова на улице")
                break
            elif re.fullmatch(".*(выбир|осматр|подбир).*продукт.*", answer.lower()):
                print("Вы видите хлеб, молоко и кофемашину. Мда, не густо....")
            elif (re.fullmatch(".*(взять|купить)\s\w.*", answer.lower())):
                matchs = re.sub(("(взять|купить)\s"), "", answer.lower())
                if matchs:
                    if matchs == "хлеб":
                        print("Хлеб взяли")
                    elif matchs == "молоко":
                        print("Пакет оказался порван. Взяли другой пакет")

                    elif matchs == "кофемашину":
                        print("Она слишком дорогая")
                    else:
                        print(f"Я не могу купить, {matchs}. Этого нет в магазине")


    elif re.fullmatch(".*(идт|иду|напр|передв|вернул|пой(д|т)).*парк.*", answer.lower()):
        print("Вы в парке. Там аттракционы. Что дальше?")
        while True:
            answer = input()
            if re.fullmatch(".*(вернут|выйти|выход).*", answer.lower()):
                print("Вы вернудись домой")
                break
            elif re.fullmatch(".*(выбир|выбор|осматр|подбир).*аттр.*", answer.lower()):
                print("Есть выбор: веселая карусель, комната ужасов, американские горки. Ваш выбор: карусель, комната, горки")

            elif (re.fullmatch(".*(выбор)\s(\w)+.*", answer.lower())):
                matchs = re.search("выбор\s(\w)+.*", answer.lower())

                if matchs:
                    if matchs[0] in ["выбор веселая карусель","выбор карусель"]:
                        print("катаюсь на карусели - закружилась голова")
                    elif matchs[0] in ["выбор комната", "выбор комната ужасов"]:
                        print("очень страшно в комнате ужасов!")
                    elif matchs[0] in ["выбор американские горки", "выбор горки"]:
                        print("вот это да! дух захватывает")
                    elif (matchs[0] == "выбор домой"):
                        print("Мы пришли домой. До свидания")
                        break
                    else:
                        matchs = re.sub(("выбор\s"), "", answer.lower())
                        print("В парке нет аттракциона", matchs)
