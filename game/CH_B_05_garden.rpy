# CH_B_05_garden.rpy

label CH_B_05_garden:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"

    scene garden_path at fullscreen_bg
    with fade
    voice "audio/voice/b/05/0_2_目の前に広.mp3"
    narrator_arrow "目の前に広がる美しい景色に息を呑む。\n"
    voice "audio/voice/b/05/0_3_草木が生い.mp3"
    extend "草木が生い茂り、色とりどりの花が咲き誇っている。\n"
    voice "audio/voice/b/05/0_4_そこには部.mp3"
    extend "そこには部屋の中とは思えない空間が広がっていた。\n"
    voice "audio/voice/b/05/0_5_室内庭園と.mp3"
    extend "室内庭園といったところだろうか\n"

    scene garden at fullscreen_bg
    with fade
    voice "audio/voice/b/05/0_6_庭園の奥に.mp3"
    narrator_arrow "庭園の奥に進むと、そこかしこに古代の遺物のようなモニュメントが点在している。\n"
    voice "audio/voice/b/05/0_7_石の彫刻や.mp3"
    extend "石の彫刻や古い噴水、草むらにもなにか隠れているようだ。\n"
    voice "audio/voice/b/05/0_8_しかし長年.mp3"
    extend "しかし長年手が入っていないのか、鬱蒼としている。\n"
    voice "audio/voice/b/05/0_9_出口のよう.mp3"
    extend "出口のようなものは見当たらない。\n"
    voice "audio/voice/b/05/1_0_注意深く、.mp3"
    extend "注意深く、次のフロアへ進むための手がかりを探す。"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/b/05/1_0_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？"
    menu:

        "１．古い噴水を調べる。噴水の中に何か隠されているかもしれない。":
            
            stop music
            stop voice
            play sound "audio/se/発見.mp3"
            scene garden_hidden_stairs at fullscreen_bg
            with fade
            voice "audio/voice/b/05/0_0_古い噴水を.mp3"
            narrator_arrow "古い噴水を調べると、水が引いて隠された階段が現れた。\n"
            voice "audio/voice/b/05/0_1_次のフロア.mp3"
            extend "次のフロアに進もう。"

            scene black
            with Dissolve(1.0)
            jump CH_B_06_mirror_room

            
        "２．草むらを探る。草むらの中に扉が隠れている可能性がある。":
            stop music
            stop voice
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene bitten_by_snake at fullscreen_bg
            voice "audio/voice/b/05/0_0_草むらの中.mp3"
            narrator_arrow "草むらの中に隠れていた蛇が飛び出してきた！\n"
            voice "audio/voice/b/05/0_1_あなたは、.mp3"
            extend "あなたは、あなたはショックで気絶してしまった。\n"

            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()

        "３．石の彫刻を動かす。彫刻の下に秘密が隠されているかもしれない。":

            stop music
            stop voice
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene fallen_statue at fullscreen_bg
            voice "audio/voice/b/05/0_0_彫刻が倒れ.mp3"
            narrator_arrow "彫刻が倒れ、激しく頭を打ち付けてしまった！\n"
            voice "audio/voice/b/05/0_1_目の前が暗.mp3"
            extend "目の前が暗くなり、意識が遠のいていく。\n"
            voice "audio/voice/b/05/0_2_もう、これ.mp3"
            extend "もう、これ以上動くことはできそうにない――。\n"

            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()

    $ choice_comment = ""  