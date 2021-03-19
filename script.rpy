﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define g = Character('Александр', color="#53a642")
define k=Character('Командир русской гвардией', color="#ff2200")
define s=Character('Солдат', color="#63605f")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music "as.mp3"
    k "Братья мои, внимайте же меня все в сей момент!
     С минуты на минуту падем мы от французского штыка на незнакомую нам землю, мы все знаем это...
     Но, чтоб меня черт взял, именно за этим мы и пришли на земли вражьи!"
    k "Я хочу спросить вас...Готовы ли вы положить свои молодые судьбы за незыблемость отчизны нашей,
     за долгую жизнь матерей и сестер наших, за нашего светлого государя?"
    k "Не содрагаются ли сердца в вашей крепкой груди?! Не хладеют ли ваши пламенные головы?!
     Родина не поможет нам... Мы вдали от наших родных равнин и лесов..."
    k "В этом сражении надейтесь только на свой клинок, порох на полке ваших ружий и на ваше хлоднокровие...Братья...
    Мы обязаны показать европейской вражине, что русскому бойцу в радость самое настоящее пекло!"
    s "Да! Покажем! В бой же!"
    "{i}Рев солдат и гул топота{/i}"
    g "О боже...Неужели правда это все...Я не смогу человека жизни лишить...Нет! Я обязан!
     За тем ведь я и здесь! Это жестокие захватчики! Я должен ответить им той же монетой..."
    g "Но что,если... Что, если солдат незнакомый мне, по другую сторону баррикад, страшится
      также, и сомнения вторглись в его душу... Ведь люди одинаковы везде... Не понимаю..."
    g "Мир сошел с ума... Ах!"
    "{i}Героя ранят{/i}"

    jump a1

label a1:
  menu:
    "В панике убежать": ##отложено
        "{i}Герой паникует, бежит в деревню поблизости, но добегает лишь до тракта возле деревни и падает в обморок.{/i}"
        jump end
    "Продолжить атаку":##завершено
        g "Ах...Господи...Куда же он...Зачем же...
        Не верю глазам своим...Бог велит мне на войне погибнуть...
        Но я этого так не оставлю!Уйду на тот свет только лишь с тройкой этих гадов!"
        "{i}Герой,храмая,бежит в атаку{/i}"
        "{i}Героя смертельно ранят пулей в грудь{/i}"
        g "Ахг...Дурак..Как же тут стало здесь холодно...
        Не могу и шевельнуться же...Сука,не могу и моргнуть...
        Хех..Метчал о типичной дворянской скучной жизни у камина послеэтого всего,а в итоге..."
        "{i}Сблювал всю свою кровь в след в грязи от французского сапога{/i}"
        g "...Жизнь - интересная штука...
        В вечной скуке мира иного не будет хватать мне её забав и веселий...
        Очень кружится голова...Я боюсь.."
        jump smert
    "Уйти за помощью к врачам":
        g "Ах...Нужно назад...Мне сейчас же нужно...Назад...Не дойду... Микита Шевченко: Гей,друг! Давай ко мне на спину, тебя нужно срочно подлатать! А ну-ка,братец..."
        "{i}Поднимает героя{/i}"
        g "Спасибо...Я в долгу не останусь,клянусь...Спасибо,Микита...Ты - настоящий друг..."
        "Микита" "Да ну тебя! А чего мне ради этот долг? Я по своей чистой воле делаю, не трепись, как баба"
        "{i}Героя отводят к полевым врачам{/i}"
        "Фельдшер" "Ох и угораздило же тебя...Быстрей ко мне его! Ложись-ка на землю,сейчас тебя подправим...Эй,дайте ему водки!И..И мне тоже!"
        "Помощник фельдшера" "Может...Может не сейчас?"
        "Фельдшер" "О, господи! Дай мне водки, ты думаешь я её пить стану? Как тебя такого узколобого вообще во врачи взяли?"
        "Помощник фельдшера" "Гхм...Извините,не могу адекватно мыслить в таких условиях..."
        "Фельдшер" "Ладно,берись за другого,работы по горло,а ты тут демагогию развел!"
        "Фельдшер" "Так-с...Угу..Тебе повезло,голубчик:кость,артерия целы!Сейчас вытащим пулю,зашьем и обратно в бой у меня еще побежишь! Пинцет мне!"
        "{i}Вытаскивает пулю{/i}"
        "{i}Герой неистово кричит{/i}"
        "Фельдшер" "Идиот! Я тебе зачем водку-то принес?Ох,как же с вами,остолопами,cложно! На посмотри лучше на героя нашего дня..."
        "{i}Показывает герою пулю{/i}"
        "{i}Герой падает в обморок{/i}"
        "Фельдшер" "Да чтоб вас всех черт побрал! Два идиота! Неси мне холодной воды, неотесанный ты болван!"
        jump a3

label a2:##отложено
    "Ваш герой просыпается в незнакомом доме"
    "В комнату входит девушка"
    "Ваш герой в нее влюбляется"
    "Они поженились и жили долго и счастливо за пределами России.........."
    jump end


label a3:
    "{i}Герой едет в повозке{/i}"
    "Помощник Фельдшера" "Да...Сейчас..."
    "Фельдшер" "Да чтоб по тебе армия французов прошлась! Вода не с той стороны!"
    "{i}Помощник приносит воду фельдшеру{/i}"
    "Фельдшер" "Ну-ка аккуратней! Я уже не знаю, что от тебя и ожидать! Дай ведро!"
    "{i}фельдшер выливает ведро холодной воды на героя и тот просыпается{/i}"
    "Фельдшер" "Эй, слышишь меня, братец?"
    g "Угу..."
    g "{i}Кашляет{/i}"
    "Фельдшер" "Грузите его в повозку"
    "{i}помощник ударил головой герой о повозку{/i}"
    "Фельдшер" "Я устал уже на тебя, дурачка, кричать..."
    "Фельдшер" "Следующий пациент!"
    "{i}Героой находится в повозке{/i}"
    g "Ах...Нога...Да еще и голова каким-то боком...Но я еще легко отделался...Судя по тому,сколько рядом со мной людей без рук и ног...Господи..."
    g "Война всегда меня манила,её запах пороха,визг мечей и рев людей...Но слишком высока цена за эти эмоции...Слишком высока..."
    "{i}Герой едет по Европе{/i}"
    menu:
        "Извозчик" "Ну как вам здесь, в Европе то?"
        "Мне здесь нравится":
            $ evropa=True
        "Не нравится мне здесь":
            $ evropa=False
    "{i}Повозка въезжает в Прагу проездом{/i}"
    if evropa:
        g "Н-да...Многое мы на Родине упускаем мимо себя:свободные счастливые люди,опрятные дома,даже вот брусчатка есть,солнце теплее,да и трава зеленее,как говорится..."
        g "Ах,ужасна Родина моя,да верен я ей навсегда...Но, чтобы как теб люди жить, я рад на Родине и грудь на землю положить..Хех,не знал, что ранения прибавляют мне поэтического мастерства..."
        g "Податься,может,мне в поэты и забыть всю эту жизнь военную? Да хоть и сейчас начну! Сей же момент! Был же у меня сверток бумаги у накидке на случай,если предсмертное письмо родным писать я собирусь..Нашел!Ага..С чего бы начать..."
        "{i}Спустя 10 минут{/i}"
        "{i}читает стихотворение{/i}"
        g "Вези меня,ямщик,обратно!Мне больно, жалко, тяжелоСмотреть на то, как все опрятно,Ухоженно, тепло, светло,Как идеально в этом мире, Но посвятить хочу я лире Все подлости своей страны,Изнанки мёрзлой Сатаны..."
        g "Н-да...Видит бог, судьба моя - на поле битвы смертью храбрых пасть..."## возможно надо удалить
        jump a5
    else:
        g "И что они в этом нашли...Как-то притворно все это...Все ухоженно,красиво,cтройно...Нет в этом,понимаешь,души какой-то...Да и величавый наш Санкт-Петербург по всем фронтам этот жалкий городок опередит!"
        g "Правильно, что мы с этими блаженными соперничаем! Не допустит Великая Российская Империя этого слабого засилия по всему миру...Этому свету нужна сильная рука нашего Светлейшего Императора..."
        g "Видит бог,и на этих землях однажды возведет будет чёрно-жёлто-белый флаг и герб наш воцарится над Европой...Жаль, что не доживу я к тем векам..."
        jump a5

label a5:
    "{i}Солдаты повздорили с чехами и убивают одного из них{/i}"
    "{i}Повозка движется уже загородом,по полевой дороге.{/i}"
    "{i}Вдруг девушка,переходя дорогу,падает прямо перед этой повозкой и русский, озлобленный чем-то,солдат скандалит с ней{/i}"
    "Солдат сопровождения" "Куда ты лезешь,соплячка?!Тебе жить надоело? Ты не видишь кого и откуда мы везем?!Я тебя спрашиваю!Кто тебе позволил?!"
    "Девушка" "Vůbec jsem nechtěl ... Promiňte, prosím! Jsme bratrské národy, smilujte se nade mnou! Už odcházím..."
    "Девушка" "(Я совсем не хотела...Извините меня пожалуйста!Мы ведь с вами братские народы,помилуйте меня!Я уже ухожу...)"
    "Солдат сопровождения" "Что ты там бормочешь, халуйка? Ты не представляешь с кем ты разговариваешь,чернь!"
    g "Куда ты бежишь?! Я с тобой еще не закончил! Или ты хочешь, чтобы об этой встрече ты с ужасом вспоминала всю жизнь?Не беги,я сказал!"
    "{i}Солдат хватает девушку за волосы и ударяет её ладонью{/i}"
    "Солдат сопровождения" "Тебе еще мало,а?!"
    "Девушка" "Smiluj se nade mnou ... Není třeba ... (Смилуйтесь надо мной,не надо)"
    "Солдат" "Мерзкавка,я тебя просто так не отпущу!"
    "{i}Вокруг собралась толпа зевак и один юноша побежал на помощь девушке{/i}"
    "Юноша" "Nedotýkej se jí! (Не трогай ее!)"
    "Девушка" "Lukaši, drž se dál, bude to jen horší! ( Лукаш,не подходи,будет только хуже! )"
    "{i}Юноша толкает солдата,но тот был в броне,поэтому ничего не вышло{/i}"
    "Юноша" "Dej od ní ruce! (Убери от нее руки!)"
    "Солдат" "Куда ты лезешь, идиот?! Я тебе кишки выпущу!"
    "{i}Cолдат взмахнул мечом и в точности выполнил своё обещание{/i}"
    "{i}все с ужасом ахнули{/i}"
    "Солдат" "Ненормальный...Я ведь говорил, чтобы он не лез...Уходим отсюда!"
    "{i}Солдат оттаскивает умирающего юношу на обочину и толкает девушку,чтобы она упала рядом с ним{/i}"
    "Девушка" "Lukash ... Pane ... Proč ... Kdo se tě zeptal ... Odpusť mi, bratře ... ( Лукаш...Господи....Зачем...Кто тебя просил...Прости меня, братец... )"
    "{i}Девушка плачет взахлеб,к уже мертвому и обезображенному телу сходится народ,повозка с раненными уезжает,народ забрасывает их камнями вслед{/i}"

    if evropa:
        g "Что это было...Как человек на такое способен?...У солдат должна быть честь...Куда же подевались честные и доблестные русские бойцы?"
        g "Все доблестные ребята умирают такой же смертью на поле боя, и лишь отпетые мерзавцы лишают жизни таких юных и добрых людей...Да еще и таким гнусным способом..."
        g "Была бы моя воля...Эх...Настоящих героев никогда не вспомнят - таково правило нашего века..."
        jump a6
    else:
        g "Герой: Куда же он полез...Дурак...Совсем эти неруси поехали головой...Как ясное солнце было видно то, что нашему воину не до шуток..."
        g "С войны люди возвращаются либо с пустыми глазами, либо с сединой на голове,либо с отчаянной злобой в груди..."
        g "Со злобой на все вокруг,ведь их преданных друзей в минувшие дни иноземные гады прикончили... Пустоголовый паренёк...Поделом ему..."
        jump a6

label a6:
    "{i}Герой приехал{/i}"
    g "Кх-кх-кх...Ох,не хватало ещё и простудится перед службой...С самого утра день не задался...Чую я,будет что-то неладное..."
    "{i}Герой встаёт с кровати и идёт умываться{/i}"
    g "Может мне остаться дома?"

    menu:
        "Ехать в Петербург":
            jump peterburg
        "Остаться дома":
            jump suesid
label suesid:
    g "Не пойду я никуда,иначе кто знает,что со мной может произойти?А ведь у меня жена,сын...Пойду-ка лучше под плед...Ах,как стыдно будет перед товарищами..."
    g "Но,как говорила моя няня, задыхаясь от пронзительного больного кашля:Здоровье важнее,Сашенька...Нет дороже сокровища и дара божьего, чем крепкое и ладное здоровье...Храни его и слова мои..."
    g "И я храню твои слова,нянечка...Ни за что не забуду темных вечеров под теплым светом лампадки,твоих сказок на ночь...Покойся с миром,родная няня..."
    "{i}Герой погружается в сон{/i}"
    "{i}Встаёт на следующее утро{/i}"
    g "Ох...Ну сейчас вроде получше...Самое время оправдываться перед командиром...Еду в Санкт-Петербург..."
    g "Соскучился я по этому сказочному мрачному миру...Лиза,скажи Григорию,чтобы он готовил мне лошадь! Через 20 минут я выезжаю!"
    "{i}Герой выходит на тракт и едет а сторону Петербурга{/i}"
    "Встречный человек" "(Захлебываясь в слезах,и бубня себе под нос)Сынок... Зачем?...Ну какой черт тебя взял?... Революции-удел глупцов,я всегда был уверен,что ты выше всего этого..."
    "Встречный" "Разве так ты любишь своего папку?...Я...Как мне сказать об этом твоей матери?...Она ведь,бедная,до сих пор верит, что ты опять ушел на свои гулянки..."
    "Встречный" "Вольное мое сокровище...Ты был неугомонен...Нет мне смысла жить в этом мире без тебя...Без моего сыночка...С тобой похороню и себя,и будут наши тела навечно стынуть в мёрзлой земле..."
    g "Эй, мужчина,что стряслось?Чего такой проникший?"
    "{i}Он не отвечает{/i}"
    g "Не молчи,когда солдат спрашивает?Говори же мне,что случилось?"
    "Встречный" "Сенатская площадь...Всех...Всех убили...Лишь счастливчики сбежали..."
    g "Ты бредишь! Какая площадь? Что случилось? Объясни же мне наконец!Не томи!"
    "Встречный" "Солдаты...2 дивизии вышли на площадь,дабы арестовать императора...По слухам, заговорщики зашли в казармы и вывели солдат на площадь."
    "Встречный" "Несогласных и мешающих прикончили на месте...План был идеален,но...Череда ошибок,не важно каких,я сам не знаю, привела к тому,что моего сына изрешетило картечью..."
    "Встречный" "Господи,помилуй его грешную душу! Намучился мой сынок!Даруй же ему вечный покой!..."
    g "Не верю...Где держат выживших?"
    "Встречный" "Их допрашивают,не пытайтесь их найти..."
    g "Не указывай мне,я знаю,что мне делать..."
    "{i}Герой прибывает на сенатскую площадь{/i}"
    g "Черт...Этот чудак не шутил...Все залилось красным цветом...Нужно найти Бестужева! Срочно!"
    "{i}Герой подходит к солдату,стоящему на дозоре площади{/i}"
    g "Приветствую!Мне нужно знать,где сейчас находится Бестужев!Срочно!Я его близкий друг!"
    "Солдат" "Мне не разрешено разглашать тайну."
    g "Да ты видимо не понимаешь,с кем ты говоришь? Посмотри на меня,глупец!"
    "Солдат" "Ах...Не признал...У меня для вас плохие новости... Вашего товарища приговорили к казни...Через повешение..."
    g "Вздор!Она запрещена!"
    "Солдат" "Они предприняли попытку государственного переворота...Они враги народа..."
    g "Не смей так говорить про него!"
    "{i}Герой ударяет солдата, завязывается драка,но их разнимают ,а героя выгоняют с площади{/i}"
    "{i}Герой приезжает домой,по пути сходив в бар,его жена уехала к сестре,дом пуст,лишь слуга находится в своей комнате{/i}"
    "{i}Герой берет бумагу и пишет супруге прощальное письмо{/i}"
    g "{i}Дорогая Лиза, сегодня я узнал,что мои родные товарищи,друзья и братья погибли...Все до одного...С таким позором я жить не смогу.{/i}"
    g "{i}Все мое наследство достается тебе...Ты больше не увидишь меня, прощай.{/i}"
    "{i}Герой достает оружейный ящика,медленно, молча заряжает пистолет{/i}"
    g "Увидимся в лучшем мире, друзья...Я очень по вам скучаю..."
    "{i}Выстрел{/i}"
    jump end

label peterburg:
    g "{i} ополоснул лицо прохладной водой и сразу почувствовал себя свежее{/i}"
    g "Надо собраться. Болезнь не оправдание для лени! Там все мои товарищи и друзья. а я думаю только о себе. "
    g "Я не должен отлынивать! Я сам выбрал такой путь! Нельзя давать слабину!"
    g "Можно и потерпеть немного, я же мужчина, могу потерпеть несколько  дней. {i}Вышел из ванной комнаты{/i}"
    g "Лиза, скажи Григорию. чтобы он приготовил лошадей! Я еду в Санкт Петербург!Так. вроде все собрано.Одежда здесь. Зонт взял. Все. теперь я точно готов!"
    g "До свидания ,Лиза, я скоро вернусь, так что не переживай, если что то произойдет, то я обязательно напишу тебе"
    g "{i}Жена нежно поцеловала меня в щеку{/i}"
    "Лиза" "До свидания, милый."
    g "{i}Вышел из дома и подошел к Георгию{/i}"
    ##тут

label smert:
    jump end
label end:##совсем конец
    "Это пока что все"
return
