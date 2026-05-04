# CH_A_06_Tomb_of_the_Warriors

label CH_A_06_Tomb_of_the_Warriors:

    window hide

    play music "audio/bgm/strange_lullaby.mp3"
    scene armor_room_investigation at fullscreen_bg
    with fade

    voice "audio/voice/a/06/0_0_あなたは部.mp3"
    narrator_arrow "あなたは部屋を調べ、甲冑の停止が何を意味するのか考える。\n"
    voice "audio/voice/a/06/0_1_壁には塔の.mp3"
    extend "壁には塔の古い見取り図が掛かっていた。\n"
    voice "audio/voice/a/06/0_2_この武器庫.mp3"
    extend "この武器庫の端には小さく「出口」と書かれた場所が見える。\n"
    voice "audio/voice/a/06/0_3_もしや、こ.mp3"
    $ ctc_mode = "page"
    extend "もしや、ここから外に出られるのではないか。\n"

    scene exit_discovery at fullscreen_bg
    with fade
    voice "audio/voice/a/06/0_4_部屋の隅に.mp3"
    narrator_arrow "部屋の隅に隠された小さな扉を見つけ、あなたはそれが塔の外へ続く道だと悟る。\n"
    voice "audio/voice/a/06/0_5_不安を感じ.mp3"
    $ ctc_mode = "page"
    extend "不安を感じながらも、あなたは扉を開けて外に出ることを決意する。\n"

    play music "audio/se/風に揺れる草木1.mp3"
    scene forest_entrance_1 at fullscreen_bg
    with fade
    voice "audio/voice/a/06/0_6_塔の中にい.mp3"
    narrator_arrow "塔の中にいたせいか、外の空気が冷たかった。\n"
    voice "audio/voice/a/06/0_7_あなたは、.mp3"
    extend "あなたは、すぐに茂みの中へと足を踏み入れる。\n"
    voice "audio/voice/a/06/0_8_茂みをかき.mp3"
    extend "茂みをかき分けながら進むと、徐々に視界が開けてきた。\n"
    voice "audio/voice/a/06/0_9_遠くからは.mp3"
    extend "遠くからは風に乗って木々のざわめきが聞こえる。\n"
    voice "audio/voice/a/06/0_10_その先に広.mp3"
    $ ctc_mode = "page"
    extend "その先に広がる異様な光景に、あなたは足を止める。\n"

    scene sword_grave at fullscreen_bg
    with fade

    voice "audio/voice/a/06/0_11_無数の剣が.mp3"
    narrator_arrow "無数の剣が大地に突き立てられ、錆びついた刃が月明かりに鈍く光る。\n"
    voice "audio/voice/a/06/0_12_その場所は.mp3"
    extend "その場所は、まるで戦士たちの魂を弔う墓碑のようだ。\n"
    voice "audio/voice/a/06/0_13_冷たい風が.mp3"
    $ ctc_mode = "page"
    extend "冷たい風が吹き抜け、木々がざわめき始める。\n"

    scene sword_a at fullscreen_bg
    with fade
    voice "audio/voice/a/06/0_14_不意に、あ.mp3"
    narrator_arrow "不意に、あなたが握る剣が淡く光を放つ。\n"
    voice "audio/voice/a/06/0_15_呼応するか.mp3"
    extend "呼応するかのように剣の周囲から霧のような白い光が立ち上り、次々と形をなしていく。\n"
    voice "audio/voice/a/06/0_16_やがて、無.mp3"
    $ ctc_mode = "page"
    extend "やがて、無数の戦士の霊があなたの前に浮かび上がる。\n"

    play music "audio/bgm/透明な亡霊.mp3"
    scene ghosts_1 at fullscreen_bg
    with fade
    voice "audio/voice/a/06/0_17_「これは….mp3"
    narrator_arrow "「これは…勇者の剣ではないか！」\n"
    voice "audio/voice/a/06/0_18_戦士の霊た.mp3"
    extend "戦士の霊たちは目を見開き、あなたを見つめる。\n"
    voice "audio/voice/a/06/0_19_彼らはあな.mp3"
    extend "彼らはあなたの持つ剣を見て驚愕し、取り囲むようにして近づいてくる。\n"
    voice "audio/voice/a/06/0_20_「まさか、.mp3"
    extend "「まさか、あなたが勇者だというのか…？"
    voice "audio/voice/a/06/0_21_我らが待ち.mp3"
    extend "我らが待ち望んだ、あの勇者がここに…！」\n"
    voice "audio/voice/a/06/0_22_霊たちの眼.mp3"
    extend "霊たちの眼差しには期待と畏敬の念が混じっている。\n"
    voice "audio/voice/a/06/0_23_しかし、そ.mp3"
    $ ctc_mode = "page"
    extend "しかし、その中には深い悲しみと無念の思いも感じられる。\n"

    voice "audio/voice/a/06/0_24_「我らはか.mp3"
    narrator_arrow "「我らはかつて、魔人たちと戦い、この地で散った者たちだ。"
    voice "audio/voice/a/06/0_25_多くの仲間.mp3"
    extend "多くの仲間が勇敢に戦い、そして力尽きた…。"
    voice "audio/voice/a/06/0_26_それでも我.mp3"
    extend "それでも我らは、勇者が現れ、この剣を手に魔人を倒す日を信じて待っていたのだ。」\n"
    voice "audio/voice/a/06/0_27_しかし、あ.mp3"
    extend "しかし、あなたは心の中で戸惑いを覚える。\n"
    voice "audio/voice/a/06/0_28_彼らが勘違.mp3"
    extend "彼らが勘違いしているのだろうか。\n"
    voice "audio/voice/a/06/0_29_それとも、.mp3"
    $ ctc_mode = "page"
    extend "それとも、この剣が何か特別な意味を持つのだろうか。\n"

    voice "audio/voice/a/06/0_30_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？" 

    menu:

        "１．勇者だと答える。":
            jump CH_A_06_bad_Tomb_of_the_Warriors_1
        "２．勇者ではないと答える。":
            jump CH_A_06_good_Tomb_of_the_Warriors            
        "３．剣で戦士の霊に切りかかる。":
            jump CH_A_06_bad_Tomb_of_the_Warriors_2


    $ choice_comment = ""  


