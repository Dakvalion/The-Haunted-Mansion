define defTrust = 100
define defUntrust = 0
define mod = 0

define albert_trust = 80
define doran_trust = 50
define richard_trust = 50
define gillian_trust = 50

screen trustlevel:
    bar:
        xsize 350
        ysize 30
        xpos 50
        ypos 50
        value AnimatedValue( value=mod, range=defTrust, delay=1.0)
        left_bar Frame ("gui/bar/left.png", 10,10)
        right_bar Frame ("gui/bar/right.png",10,10)


define player = Character("[playername]")
define a = Character("Albert Beam", color='#FF9A00')
define d = Character("Doran Buckley", color='#35D4A4')
define r = Character("Richard Elmer", color='#FF8240')
define g = Character("Gillian Murray", color='#FFB440')


label start:

    $ playername = renpy.input("What is your name?", length=32)
    $ playername = playername.strip()

    if not playername:
        $ playername = "Adren Egan" 

    play music "audio/ocean.mp3" fadeout 0.5
    scene bg ocean


    player "Какая хорошая погода"
    player "Интересно, будет ли в порту также солнечно, когда мы причалим…"
    player "..и что мне принесет визит в старый добрый Ширнесс?"
    "Сыщик держал в руках письмо, подписанное неким «Альбертом Бимом», в котором его попросили срочно приехать"
    "Бим не раскрыл полной сути дела, но оттого было и интереснее поскорее взяться за него"
    player "Мы прибываем через два часа, думаю, пока можно отдохнуть в каюте, если я не хочу предстать перед Альбертом с красным лицом"

    scene bg port with fade
    play music "audio/port.mp3" fadeout 0.5

    player "'Что ж, Альберт сказал, что встретит меня здесь, остаётся только ждать'"

    show albert at right
    with dissolve

    a "-Рад приветствовать вас, [playername]! Я тот, кто писал Вам"
    player "Рад знакомству, Альберт"
    a "Очень рад, что вы приехали так быстро и прошу у вас прощения, если нарушил ваши планы на отпуск"
    player "Ничего страшного, это издержки профессии. Вы расскажите мне, почему потребовалась такая срочность?"
    a "Да, но давайте лучше пройдём ко мне, у всего есть уши"
    player "Да, вы правы"

    scene bg n house with fade
    show albert at right
    with dissolve
    play music "audio/detective.mp3" fadeout 0.5 volume 0.5

    a "В последнее время на местной стройке стали часто пропадать люди"
    a "Ранее семейство Кэррингтон обладали большим поместьем к юго-западу от порта, но пару месяцев назад все погибли при страшном пожаре, а затем его купил Нейт Колуман"  
    a "Он решил построить гостиницу на месте особняка, но как-только начались работы, стали пропадать люди"
    a "В основном пропадают ночью, те работяги, кто остаётся допоздна, или хочет найти, что осталось от прежних жильцов"
    a "Кто-то говорит, что там все ещё ходят призраки почивших Кэррингтонов, но мне кажется, что-то тут нечисто"

    player "Вы не знаете кого-либо, кто «видел» призраков или избежал встречи с ними?"
    a "Да, я дам вам адреса людей, которые могут пригодиться"
    play sound "audio/letter.mp3"
    "В этот момент мы услышали шорох около двери"
    a "Что это?!"

    scene bg letter
    with fade

    pause 0.7

    scene bg street
    with fade

    player "Я выбежал на улицу, чтобы посмотреть, кто мог его подбросить, но увидел лишь пустую дорогу"

    scene bg n house
    with fade
    show albert at right

    a "Чёрт"
    player "Что такое?"
    "Альберт передал мне письмо, в котором было написано «Я знаю, что ты здесь»"

    scene bg hotel with fade

    player "Я пришёл в гостиницу, где остановился на время пребывания в Ширнессе"
    player "Мы с Альбертом ещё немного обсудили детали, и он дал мне пару советов"

    scene bg n house
    with fade
    show albert at right

    a "В этом городе люди мало кому доверяют, поэтому обязательно подумайте семь раз, прежде, чем сказать им что-то"

    scene bg hotel with fade

    player "Что ж, займусь этим завтра"

    jump ep1

label ep1:

    scene bg hotel with fade

    play music "audio/street.mp3" fadeout 0.5 volume 0.5

    scene bg start street with fade
    player "Утром следующего дня я направился к одному из потерпевших, Дорану Бакли"

    scene bg o house with fade
    play music "audio/o house.mp3" fadeout 0.5 volume 0.5
    player "Я свернул с многолюдной улицы и прошёл ещё несколько кварталов, прежде чем достичь дома Дорана."

    scene bg o zoom with fade
    player "Я подошёл поближе и постучал"
    play sound "audio/knock.mp3"
    pause 2.0
    player "Никакой реакции не последовало"
    player "Я постучал ещё раз"
    play sound "audio/knock.mp3"
    pause 1.0

    show doran at right 
    with dissolve
    player "Дверь открыл недовольный седой мужчина"
    $ mod = doran_trust
    show screen trustlevel with dissolve
    d "Кто ко мне ломится?!"
    player "Вы – Доран Бакли?"
    d "Да! А Вы кто такой?!"

    menu:
        "Меня зовут [playername]":
            $ doran_trust += 20
            $ mod = doran_trust
            d "Оо, мой дом решил посетить такой почтенный сыщик, это честь для меня, входите"
            scene bg o living with fade
            play music "audio/detective.mp3" fadeout 1.0 volume 0.5
            show doran at right 
            with dissolve

            player "Вы работали на стройке в особняке, верно?"
            d "Да, только там ещё не идёт стройка как таковая, особняк все ещё не снесли"
            player "Почему же? Дело в «призраках»?"
            d "Да…"
            "В голосе Дорана пробежала мелькая дрожь"
            d "Понимаете, духи, они..Они не хотят оставлять это поместье"
            d "Уже пять человек без вести пропали, Нейт Коулман доверил стройку Ричарду Элмеру, т.к. сам не может посещать её из-за дел, а этот Ричард никак не хочет прекращать стройку, будь он проклят!!"
            d "Этот самодовольный индюк, которому нужны только денюжки"
            player "Что ещё вы можете сказать насчёт стройки в поместье? Что вы видели? "
            d "Ничего"
            d "Ну, то есть, в один из вечером я остался с Фергюсоном, он рассказывал, что у Кэррингтонов остались сокровища, где-то под поместьем, и он очень хотел их найти"
            player "И?"
            d "Он звал меня с собой, но я решил остаться, всё же, моя жажда наживы не так велика"
            d "Я ждал его час, и тут, откуда не возьмись взялся какой-то вонючий туман и из темноты особняка я видел чьи-то глаза…."
            d "Я сразу же убежал оттуда, а на следующий день, Фергюсон не вернулся"
            player "В особняке не было никаких странных звуков, пока вы ждали его?"
            d "Были шорохи, но крысы везде есть, а вот когда я увидел глаза, я услышал тяжёлые шаги"
            player "Понятно… Спасибо за то, что поделились этим со мной"
            $ doran_trust += 10
            $ mod = doran_trust
            d "Если это поможет, я буду только рад"
            hide screen trustlevel with dissolve
            
            scene bg o zoom with fade
            play music "audio/o house.mp3" fadeout 0.5 volume 0.5
            player "Доран всё-таки думает, что это были призраки…."

            jump later

        "Это неважно":
            $ doran_trust -= 20
            $ mod = doran_trust
            d "Ну тогда катитесь отсюда"
            hide screen trustlevel with dissolve
            hide doran with dissolve
            play sound "audio/close door.mp3"
            "Доран захлопнул дверь и ушёл"
            player "Что ж, а чего ещё можно было ожидать…"
            player "Мне следует быть аккуратнее в будущем, может, в следующий раз"

            jump later


label later:
    play music "audio/street.mp3" fadeout 0.5 volume 0.5
    scene bg start street with fade
    player "Следующий у нас Ричард Элмер.."

    scene bg company with fade
    play music "audio/o house.mp3" fadeout 0.5 volume 0.5
    player "Я дошёл до красивого здания почти в центре города"
    player "Хм? Нынче строительные конторы даже в небольших городишках выглядят не так плохо"

    play music "audio/detective.mp3" fadeout 0.5 volume 0.5
    scene bg corridor with fade
    $ mod = gillian_trust
    show gillian at left 
    with dissolve
    show screen trustlevel with dissolve

    g "Добро пожаловать в «Элмер и Ко», чем я могу вам помочь?"
    player "Могу ли я переговорить с Ричардом Элмером?"
    g "Можете ли вы назвать своё имя?"
    player "Меня зовут [playername]"
    g "Сейчас я уточню"
    hide screen trustlevel with dissolve
    hide gillian with dissolve

    pause 2.0

    
    show gillian at left 
    with dissolve
    show screen trustlevel with dissolve

    g "Он готов принять Вас"

    scene bg r office with fade
    $ mod = richard_trust
    show richard at left
    with dissolve
    show screen trustlevel with dissolve

    player "Рад видеть Вас, мистер Элмер, спасибо, что смогли уделить мне время"
    r "О ну что Вы, я всегда рад таким важным для нашего общества людям"
    r "Что могло привести ко мне такого почтенного гражданина?" 

    menu:
        "Спросить в лоб": 
            player "Можете ли вы мне рассказать о стройке в особняке, которую курирует ваша компания?"
            $ richard_trust -= 10
            $ mod = richard_trust
            r " А что-то не так?"
            player "Я говорил с одним из ваших бывших работников и мне сказали, что там промышляют призраки"
            r "Ах, эти чудаки, им всё мерещится"
            player "Пропавшие люди тоже мерещатся?"
            $ richard_trust -= 10
            $ mod = richard_trust
            r "Вы меня в чём-то подозреваете?"
            player "Нет, просто хочу дойти до правды"
            r "Правда в том, что с моей стройкой всё в порядке, я регулярно извещаю мистера Коулмана о всех неполадках и всё замечательно"
            r "К тому же, нам регулярно требуются рабочие, т.к. там будет строиться нечто грандиозное, что поможет Ширнессу принимать больше туристов"

            jump richard_choice
        
        "Спросить аккуратно":
            player "Я тут проездом в Ширнессе, говорят, гостиничный бизнес тут стал процветать, по крайней мере, по отношению к клиентам всё стало гораздо лучше"
            $ richard_trust += 5
            $ mod = richard_trust
            r "А в какой гостинице вы остановились?"
            player "«Элементаль»"
            $ richard_trust += 5
            $ mod = richard_trust
            r "Оо, прекрасный выбор, там действительно с каждым годом всё лучше и лучше"
            player "И я к тому же, периодически проезжаю мимо, останавливаюсь всегда там"
            player "В этот раз решил узнать чиьх рук дело здание «Элементаля» и поблагодарить за такое чудесное место рядом с центром города"
            $ richard_trust += 5
            $ mod = richard_trust
            r "О, ну что Вы, все лавры следует отдать мистеру Джеккинсу, ведь это он вывел гостиницу на такой уровень"
            r "Но мне очень приятно, что вы решили посетить нас с такой целью"
            r "Скажу Вам по секрету, скоро здесь появится большой гостиничный комплекс с парковой зоной!"
            player "Ничего себе! И, конечно же, строительство будет курировать ваша компания?"
            r "Абсолютно верно!"
            r "Не сомневайтесь, это будет грандиозно"
            player "А достаточно ли в Ширнессе рабочей силы для такой большой стройки?"
            r "Есть некоторая текучка кадров, иногда попадаются лентяи и пройдохи, которые и гроша не стоят, поэтому приходится тратить много времени на собеседования"
            player "А где же будет располагаться ваш гостевой комплекс?"
            r "Мы расположим его на месте старого особняка почивших Кэрринготонов"
            player "Оу..Вот оно что. Казалось мне, пожар был всего пару месяцев назад, не страшно ли попасть на гнев почивших?"
            $ richard_trust -= 10
            $ mod = richard_trust
            r "О нет, не говорите мне, что вы тоже верите в эти слухи"
            player "Кто знает, во всём есть доля правды"
            r "Что ж.."

            jump richard_choice




label richard_choice:
    r "К сожалению, я не могу выделить Вам больше времени, мне нужно собеседовать очередного кандидата"
    player "Я понимаю"

    scene bg corridor with fade
    show richard at left
    with dissolve

    r "Прощайте, [playername]"

    hide screen trustlevel with dissolve
    hide richard with dissolve

    pause 1.0

    $ mod = gillian_trust

    show gillian at left
    with dissolve
    show screen trustlevel with dissolve

    player "Она чем-то взволнована"
    g "Можете ли Вы мне помочь найти важные вещи? Мне срочно нужно идти за мистером Элмером, но у меня в кабинете такой бардак…"
    player "Конечно"

    jump hidden_game

label hidden_game:

    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ InitGame("bg secretary", 15.0,
    ((125, 322), "obj docs"), 
    ((855, 590), "obj map"), 
    ((1145, 320), "obj mirror"), 
    ((610, 313), "obj parfume"),
    ((830, 349), "obj pen")
    )

    $ GameAsBG()
    show gillian at left
    with dissolve

    g "Мне нужно найти папку с документами, карту города, ручку, а ещё духи и зеркальце…"
    player "Я думаю, это не проблема"
    hide gillian with dissolve
    hide screen trustlevel with dissolve
    play music "audio/energy.mp3" fadeout 0.5 volume 0.3
    "Помоги Гиллиан найти папку с документами, карту города, ручку, духи и зеркальце.\nУ тебя 10 секунд. Вперёд!"
    window hide
    $ StartGame()
    scene bg secretary 
    $ renpy.pause(0.05, hard=True)
    # результаты
    if not_found == 0:
        window show
        "Ура! Все предметы собраны!"
        stop music
        jump after
    else:
        window show
        "GAME OVER\nНе собрано предметов: [not_found]."
        jump hidden_game

    
label after:
    
    show gillian at left
    with dissolve
    show screen trustlevel with dissolve

    g "Боже мой, спасибо за Вашу помощь!"
    $ gillian_trust += 10
    $ mod = gillian_trust
    play music "audio/detective.mp3" fadeout 0.5 volume 0.5
    g "И, ну…"
    "Она дала мне ключ"
    g "Это ключ от кабинета мистера Элмера…я понимаю, что это неправильно, но мне кажется, тут творится что-то очень странное…"
    g "Мистер Элмер что-то хранит у себя в ящике стола, думаю, Вам будет интересно взглянуть"
    g "Но у вас не так много времени"
    "Я отблагодарил её и быстро ушёл"
    hide screen trustlevel with dissolve

    scene bg corridor with fade
    scene bg r office with fade
    play music "audio/mistery jazz.mp3" fadeout 0.5 volume 0.5

    player "Что ж, посмотрим на твой стол, Ричард"

    scene bg table with fade

    player "Хм… странно… зачем он пометил кнопки 5, 6 и 9 на телефоне?"
    player "И что это за зметка? «Чем больше – тем лучше»"
    player "Гиллиан что-то говорила про ящик.."

    jump codegame

label codegame:
    scene bg code start with fade
    
    player "Кодовый замок? Там точно что-то важное"
    window hide
    show screen safe_code
    $ renpy.pause(0.05, hard=True)
    play sound "audio/open drawer.mp3"
    jump end

label end:
    
    scene bg code end 
    player "Есть!"
    scene bg table with fade
    "Я достал из ящика небольшой свиток, в котором был нарисован лабиринт"
    player "И зачем ему это?"
    player "Ну ладно, мне нельзя терять время"
    "Я перерисовал себе карту, положил всё на место и вышел из кабинета"

    play music "audio/street.mp3" fadeout 0.5 volume 0.5
    scene bg end street with fade

    player "Тут и впрямь что-то не чисто..."
    "Был вечер, я направился в гостиницу сквозь толпы спешащих домой людей"

    stop music
    scene bg hotel with fade
    play music "audio/detective.mp3" fadeout 1.0 volume 0.5
    player "Нужно позвонить Альберту"

    "Спасибо за прохождение демоверсии игры «The Haunted Mansion»!"

    return



