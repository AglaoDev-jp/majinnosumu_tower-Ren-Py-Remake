# CH_C_06_dark_corridor

label CH_C_06_dark_corridor:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"
    scene dark_corridor at fullscreen_bg
    with fade
    voice "audio/voice/c/06/0_9_あなたは塔.mp3"
    narrator_arrow "あなたは塔の深部に足を踏み入れた。\n"
    voice "audio/voice/c/06/0_10_そこには、.mp3"
    extend "そこには、完全な暗闇に包まれた長い回廊が待ち受けていた。\n"
    voice "audio/voice/c/06/0_11_目を凝らし.mp3"
    extend "目を凝らしても何も見えず、頼りになるのは壁を手探りする自分の手だけだった。\n"
    voice "audio/voice/c/06/0_12_冷たい石壁.mp3"
    extend "冷たい石壁の感触が指先に伝わり、湿気を含んだ空気が不快にまとわりつく。"

    scene dark_corridor_8 at fullscreen_bg
    with fade
    voice "audio/voice/c/06/0_13_一歩一歩、.mp3"
    narrator_arrow "一歩一歩、慎重に前へ進む。\n"
    voice "audio/voice/c/06/0_14_足音は回廊.mp3"
    extend "足音は回廊に吸い込まれるように消え去り、その静寂はかえって恐怖を煽った。\n"
    voice "audio/voice/c/06/0_15_突然、背後.mp3"
    extend "突然、背後からかすかな音が聞こえる。\n"
    voice "audio/voice/c/06/0_16_何かがあな.mp3"
    extend "何かがあなたの後をつけているのだろうか？\n"
    voice "audio/voice/c/06/0_17_それとも、.mp3"
    extend "それとも、ただの気のせいなのか？\n"
    voice "audio/voice/c/06/0_18_立ち止まる.mp3"
    extend "立ち止まると、その音もまた止まる。\n"
    voice "audio/voice/c/06/0_19_しかし、振.mp3"
    extend "しかし、振り返っても、暗闇の中には何も見えない。"

    scene dark_corridor_2 at fullscreen_bg
    voice "audio/voice/c/06/0_20_さらに進む.mp3"
    narrator_arrow "さらに進むと、回廊は二手に分かれている。"
    voice "audio/voice/c/06/0_21_その時、壁.mp3"
    extend "その時、壁に触れていた手がぬるりとした感触を捉える。\n"
    voice "audio/voice/c/06/0_22_まるで何か.mp3"
    extend "まるで何かの液体が壁を伝っているようだ。\n"
    voice "audio/voice/c/06/0_23_冷たさと不.mp3"
    extend "冷たさと不快感があなたを襲う。\n"
    voice "audio/voice/c/06/0_24_背後にはま.mp3"
    extend "背後にはまだ何かが潜んでいるかもしれない。\n"
    voice "audio/voice/c/06/0_25_緊張が高ま.mp3"
    extend "緊張が高まる中、あなたは進むべき道を選ばなければならない。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/c/06/0_26_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？" 

    menu:

        "１．左の回廊に進む":
            stop voice
            scene dark_corridor_6 at fullscreen_bg
            with fade
            voice "audio/voice/c/06/1_0_あなたは迷.mp3"
            narrator_arrow "あなたは迷いながらも左の回廊へ進むことを選んだ。\n"
            voice "audio/voice/c/06/1_1_回廊は進む.mp3"
            extend "回廊は進むにつれてどんどん狭くなり、まるで壁が押し寄せてくるかのように感じる。\n"
            stop music
            play sound "audio/se/地響き.mp3"
            scene hallway_2 at fullscreen_bg 
            voice "audio/voice/c/06/1_2_突然、壁が.mp3"
            extend "突然、壁が激しく軋む音が響き渡り、回廊が崩れ始めた。\n"

            play sound "audio/se/怖い系リプレイ音.mp3"          
            voice "audio/voice/c/06/1_3_あなたは必.mp3"
            narrator_arrow "あなたは必死に逃げようとするが、逃げ道はすでに塞がれている。\n"
            voice "audio/voice/c/06/1_4_重たい瓦礫.mp3"
            extend "重たい瓦礫が次々と降り注ぎ、あなたは暗闇の中に埋もれてしまった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() 

        "２．右の回廊に進む":
            stop voice
            scene dark_corridor_3 at fullscreen_bg
            with fade
            play music "audio/bgm/strange_lullaby.mp3"
            voice "audio/voice/c/06/3_0あなたは右.mp3"
            narrator_arrow "あなたは右の回廊を選び、慎重に一歩ずつ進んでいく。\n"
            voice "audio/voice/c/06/3_1_周囲はまだ.mp3"
            extend "周囲はまだ暗闇に包まれているが、左の回廊に比べて少し広く、息苦しさは感じない。\n"
            voice "audio/voice/c/06/3_2_それでも足.mp3"
            extend "それでも足元には注意を払いながら進んでいく。\n"
            stop music
            play sound "audio/se/地響き.mp3" fadeout 1.5
            show black at fullscreen_bg with {"master": dissolve}
            voice "audio/voice/c/06/3_3しばらくす.mp3"
            extend "しばらくすると、地面が軽く揺れ、左の方向から何かが崩れるような音が聞こえた。\n"
            voice "audio/voice/c/06/3_4_あなたは立.mp3"
            extend "あなたは立ち止まり、慎重に足を運ぶ。" 

            jump CH_C_07_Heros_Statue

        "３．気配を感じ、立ち止まる":
            stop voice
            stop music
            scene dark_corridor_4 at fullscreen_bg
            with fade
            voice "audio/voice/c/06/2_0_あなたは何.mp3"
            narrator_arrow "あなたは何かが後をつけている気配を感じ、立ち止まった。\n"
            voice "audio/voice/c/06/2_1_ここで迎え.mp3"
            extend "ここで迎え撃つ覚悟を決めた。\n"
            voice "audio/voice/c/06/2_2_しばらくそ.mp3"
            show black at fullscreen_bg with {"master": dissolve}
            extend "しばらくその場で耳を澄ませ、何が起きるのかを待つ。\n"

            stop music
            play sound "audio/se/重力魔法2.mp3"
            scene dark_misty_hallway_1 at fullscreen_bg
            voice "audio/voice/c/06/2_3_突然、回廊.mp3"
            narrator_arrow "突然、回廊の奥から黒い霧が立ち上がり、その霧がゆっくりとあなたに近づいてくる。\n"
            voice "audio/voice/c/06/2_5_霧に触れた.mp3"
            scene dark_misty_hallway_2 at fullscreen_bg
            with fade
            extend "霧に触れた瞬間、冷たい感触が全身を包み込み、動けなくなる。\n"
            voice "audio/voice/c/06/2_6_からだが凍.mp3"
            extend "からだが凍りついたように重く、呼吸すらも困難になっていく。\n"

            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            voice "audio/voice/c/06/2_7_必死にもが.mp3"
            narrator_arrow "必死にもがくが、霧の力はどんどん強まり、やがて完全にあなたを飲み込んだ。\n"
            voice "audio/voice/c/06/2_8_暗闇と静寂.mp3"
            show black at fullscreen_bg with {"master": dissolve}
            extend "暗闇と静寂の中で、あなたの意識は遠のき、全てが冷たく静かな無の中に消え去った。\n"
            voice "audio/voice/c/06/2_9_あなたは、.mp3"
            extend "あなたは、その場に留まりすぎたことで、永遠に暗闇に閉じ込められることになった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() 


    $ choice_comment = ""  