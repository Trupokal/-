# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
define q = Character('QAZ300-&&&', color="#c7ffc7")

    scene bg room
    ы
    q "«…»"
    q "«…»"
    q "«…»"
    q "доброе утро"
    q "«…»"
    q "«…»"
    q "ты всё ещё смотришь?"
    q "«…»"
    q "хочешь знать, почему я сказал доброе утро?"
    q ". {w=0.5}. {w=0.5}."
    q "всё просто, это сентиментальность"
    q "так люди пытаются проявить внимание к своему окружению"
    q "хочешь знать зачем?"
    menu:

        "Да":
            jump choice1_yes

        "Нет":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        e "ну {w=0.9}я не знаю"

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        e "\«…»\"

        jump choice1_done

    label choice1_done:


    show eileen happy


    return
