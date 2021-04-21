# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
#Персы
define Alex = Character('Александр', color="#963c00")
###Тут мысли Александра
define Brain_of_Alex = Character('Александр', color="#539499")
define Captain = Character('Командир', color="#75000e")
define Abel = Character('Абель', color="#ff3838")
define Soldier = Character('Солдат', color="#363223")
define Soldiers = Character('Солдаты', color="#211f15")
define Agata = Character('Агата', color="#750039")
define Priest = Character('Cвященник', color="#a8941e")
define Taras = Character ('Тарас Шевченко', color="#8c3300")
define Doctor = Character ('Фельдшер', color="#a10000")
define StepDoctor = Character ('Помощник Фельдшера', color="#7a1515")
define Milorad = Character ('Генерал Милорадович' , color="#556b2f")
define Obolenski = Character ('Оболенский', color="#C1876B")
define Nikolai = Character ('Николай', color="#B00000")
define Yamshik = Character ('Ямщик', color="#B00000")
#нужные персы:
image keanu = "images/keanu2.png"
image tolpa = "images/unnamed.jpg"
image pole = "images/pole.jpg"
image died = "images/Died.jpg"
#жена александра"Лиза"
#слуга александра"Георгий"
#Characters
#Music and Sounds
define audio.MiddleCentWar = "Y:/Choice Of Life/game/audio/Sounds/MiddleCentWar.mp3"
define audio.MainTheme = "Y:/Choice Of Life/game/audio/Music/main.mp3"
define audio.Hearth = "Y:/Choice Of Life/game/audio/Sounds/Hearth.mp3"
define audio.HeWiWa = "Y:/Choice Of Life/game/audio/Sounds/HeWiWa.mp3"
define audio.RunWithHearth = "Y:/Choice Of Life/game/audio/Sounds/RunWithHearth.mp3"
define audio.Birds = "Y:/Choice Of Life/game/audio/Sounds/Birds.mp3"
define audio.Purga = "Y:/Choice Of Life/game/audio/Sounds/purga.mp3"
define audio.Church = "Y:/Choice Of Life/game/audio/Sounds/Church.mp3"
define audio.murder = "Y:/Choice Of Life/game/audio/Sounds/murder.mp3"
define audio.hit = "Y:/Choice Of Life/game/audio/Sounds/hit.mp3"
define audio.heal = "Y:/Choice Of Life/game/audio/Sounds/heal.mp3"
define audio.povozka = "Y:/Choice Of Life/game/audio/Sounds/povozka.mp3"
define audio.water_bucket = "Y:/Choice Of Life/game/audio/Sounds/water_bucket.mp3"
    #Начало игры
label start:
    jump PreHistory
label PreHistory:
    "После Битвы при Бородино и сдачи Москвы русской армией в пользу Наполеона генерал Кутузов предпринял меры, которые окончательно перетянули инициативу на российскую армию."
    "С тех пор французы могли лишь отступать, принимая удары от армии Российской Империи и союзников."
    "Но без конца французы отступать, к их огромному сожалению, не могли - их спины уткнулись в их последний рубеж - Париж."
    "Однако и этот рубеж не стал их спасением: французская армия пала под натиском России, Пруссии, Вюртемберга и Австрии"
    "Огромный вклад в эту победу со стороны наших соотечественников из рядов армии невозможно переоценить, они являются историческими героями наравне с Кутузовым"
    "Каждый человек, каждая личность внесла свою лепту в победу над врагом"
    "Каждый рисковал своей жизнью, возможностью увидеть свою семью, друзей"
    "Одним из таких героев был Александр - рядовой 1-ого пехотного корпуса армии Российской Империи..."
    jump War
label War:
    scene pole
    show keanu at left
    with dissolve
    Captain "Братья мои, внимайте же меня все в сей момент! С минуты на минуту падем мы от французского штыка на незнакомой нам землю, мы все знаем это... Но, чтоб меня черт подери, именно за этим мы и пришли на земли вражьи!"
    Captain "Я хочу спросить вас... Готовы ли вы положить свои молодые судьбы за незыблемость отчизны нашей, за долгую жизнь матерей и сестер наших, за нашего светлого императора?!"
    Captain "Не содрагаются ли сердца в вашей крепкой груди?! Не хладеют ли ваши пламенные головы?!"
    Captain "Родина не поможет нам... Мы вдали от наших родных равнин и лесов... В этом сражении надейтесь только на свой клинок, порох на полке ваших ружей и на ваше хладнокровие..."
    Captain "Братья... Мы обязаны показать европейской вражине, что русскому бойцу в радость самое настоящее пекло!"
    show tolpa:
        xalign 1.0 yalign 0.5
    Soldier "Гото-о-вы, друг, еще как готовы! Покажем этим круасаночным солдатикам петровскую мощь!"
    Soldiers "Да! Покажем! В бой же, братья!"
    hide keanu
    hide tolpa
    Brain_of_Alex "О боже... Неужели правда это все... Я не смогу человека жизни лишить..."
    Brain_of_Alex "Нет! Вздор! Я обязан! За тем ведь я и здесь! Это жестокие захватчики! Я должен ответить им той же монетой... Но что, если..."
    Brain_of_Alex "Что, если солдат незнакомый мне, по другую сторону баррикад, страшится также, и сомнения вторглись в его душу... Ведь люди одинаковы везде... Не понимаю... Мир сошел с ума..."
    Brain_of_Alex "Ах!"
    jump War2
label War2:
    Brain_of_Alex "Надо же... Даже повоевать не успел, а уже словил свинца в свою плоть... Что ж делать теперь..."
    menu:
        "{color=#FFFFFF}Спасаться{/color}":
            scene Спасаться
            Brain_of_Alex "Нет... Война - совсем не мое! Поскорей бы убраться с этой мясорубки... Вижу брешь! Туда скорей!"
            Brain_of_Alex "Фух... Вроде визг клинков начал утихать... Ох, как же плохо... Сейчас свалюсь... Нужно до видного места дойти..."
            Brain_of_Alex "Кажется, я вижу дорогу! Скорей туда... По мере моих способностей, конечно..."
            jump France
        "{color=#FFFFFF}Герои не убегают, поджав хвост{/color}":
            Alex "Смерть иродам! Добьем желчь французскую!"
            Alex "Ахг... Дурак.Как же тут стало здесь холодно...Не могу и шевельнуться же...Черт, не могу и моргнуть..."
            Alex "Хех... Мечтал о типичной дворянской скучной жизни у камина после этого всего, а в итоге...Сблевал всю свою кровь в след в грязи от французского сапога."
            Alex "Жизнь - интересная штука.В вечной скуке мира иного не будет хватать мне её забав и веселий.Очень кружится голова... "
            Alex "Мне страшно..."
            jump die1
        "{color=#FFFFFF}К врачам!{/color}":
            jump Medics1
label France:
    Abel "Reveille-toi pauvre chose... (Просыпайся,бедняжка...)"
    Abel "Vous avez deja l'air mieux... Pour etre honnete... Vous etes generalement tres beau... (Ты уже получше выглядишь, а если честно, ты... Ты вообще очень красивый...)"
    Agata "Abel, tu m'as promis que tu m'apporterais du lait pour le souper! Tu ne peux pas tenir parole? Apporte-moi du lait, ma fille! ( Абель, ты обещала мне, что ты принесешь мне молоко для ужина! Неужели ты не держишь слово? Принеси мне молока, доченька!)"
    Abel "Oui, j'irai, maman, attendez-moi ici... Mais ou irez-vous... (Да, я иду, мам! Жди меня здесь... Хотя ты все равно у меня даже в себя не пришел..."
    Brain_of_Alex "Ох... Как же болит голова... А нога... Она будто превратилась в синоним слова «Cтрадания»...Да и где это я???"
    Brain_of_Alex "Что за... Почему тут так жарко? Я не помню, чтобы я собирался на юг... Я совсем не у себя дома..."
    Brain_of_Alex "Последнее, что я помню: звон клинков, пороховые облака на поле битвы, крики... Много грязи и крови... А потом удар, вспышка, колосья бьют по шее, звон в ушах и свое глубокое дыхание... И темнота..."
    Brain_of_Alex "Я, кажется, должен был умереть, но на ад это не очень-то и похоже... Что?! Не верю своим ушам! Это французский! Я во Франции?! Боже, помилуй, куда меня занесло..."
    Alex "Кто ты???"
    Abel "Hourra, tu es reveille! J'etais tellement inquiete! Plus precisement... Vous ne pouvez pas vous tenir debout, vous etes toujours malade.."
    Abel "Asseyez-vous sur le lit, dites-moi tout enfin... ( Ура, вы проснулись! Я так переживала! Точнее... Вам нельзя стоять на ногах, вы еще больны... Садитесь на кровать, расскажите мне все наконец...)"
    Alex "Как я сюда попал? Точнее... Ou suis-je, qui etes-vous, que se passe-t-il? ( Где я? Кто вы такая? Что происходит?)"
    Brain_of_Alex "Она довольно мила..."
    Abel "Mon pere t'a trouve sur une autoroute pres du village. Il a dit que vous etes un envahisseur russe, que vous avez ete blesse et que vous avez quitte le champ de bataille... (Мой папа нашел вас на тракте недалеко от деревни. Он сказал, что вы русский оккупант, что вас ранили и вы ушли с поля боя...)"
    Abel "Il n'allait pas vous aider, mais je... Mon c?ur sensible ne pouvait pas vous aider, et je nous ai dit de vous emmener. C'est comme ca que vous etes arrive ici... (Он не собирался вам помогать, но я... Мое чуткое сердце не смогло вам не помочь, и я сказала,чтобы мы вас взяли. Вот так ты и оказался здесь...)"
    Abel "Vous mentez depuis 2 semaines, et pendant tout ce temps je prends soin de vous... (Ты лежишь уже 2 недели,и все это время я забочусь о тебе...)"
    Alex "Desole de vous interrompre, mais... Comment vous appelez-vous? ( Извините,что прирываю,но... Как вас зовут?)"
    Abel "Oh, tellement inattendu... Mon nom est Abel, ravi de vous rencontrer, et vous? ( Ох, так неожиданно... Меня зовут Абель, приятно познакомиться, а вас?)"
    Alex "Vous avez... Vous avez de tres beaux yeux, Abel, le saviez-vous? ( У вас... У вас очень красивые глазa, Абель, вы знали?..)"
    jump wedding
label wedding:

    Priest "Que Dieu vous benisse pour la longue vie ensemble d'Abel et de Alexandro... (Пусть благославит вас бог на долгую совместную жизнь Абель и Александро."
    Priest "Desormais et pour toujours, vous etes mari et femme (Отныне и навсегда вы - муж и жена)"
    Alex "Je t'aime Abel... ( Я люблю тебя,Абель... )"
    Abel "Et je t'aime,Alexandri... (И я люблю тебя, Сашенька...)"
    Abel "Embrasse-moi... (Поцелуй же меня...)"
    jump die1
label Medics1:
    Brain_of_Alex "Ах... Нужно назад... Мне сейчас же нужно... Назад... Не дойду..."
    Taras "Гей, друг! Давай ко мне на спину, тебя нужно срочно подлатать! А ну-ка, братец..."
    Alex "Спасибо... Я в долгу не останусь, клянусь... Спасибо, Микита... Ты - настоящий друг..."
    Taras "Да ну тебя! А чего мне ради этот долг? Я по своей чистой воле делаю, не трепись, как баба, Cашка!"
    jump Medics2
label Medics2:
    Doctor "Ох и угораздило же тебя... Быстрей ко мне его! Ложись-ка на землю, сейчас тебя подправим... Эй, дайте ему водки! И... И мне тоже!"
    StepDoctor "Может... Может не сейчас?"
    Doctor "О, господи! Дай мне водки, ты думаешь я её пить стану? Как тебя такого узколобого вообще во врачи взяли?"
    StepDoctor "Гхм… Извините, не могу адекватно мыслить в таких условиях..."
    Doctor "Ладно, берись за другого, работы по горло, а ты тут демагогию развел!"
    Doctor "Так-с... Угу... Тебе повезло, голубчик: кость, артерия целы! Сейчас вытащим пулю, зашьем и обратно в бой у меня еще побежишь! Пинцет мне!"
    Doctor "Идиот! Я тебе зачем, водку-то принес? Ох, как же с вами, остолопами, cложно! На посмотри лучше на героя нашего дня..."
    Doctor "Да чтоб вас всех черт побрал! Обморок! Два идиота! Неси мне холодной воды, неотесанный ты болван!"
    jump a3##Конец кода Эльмира
label die1:
    scene died:
        xalign 0.5 yalign 0.5
    "You dead"
    return
