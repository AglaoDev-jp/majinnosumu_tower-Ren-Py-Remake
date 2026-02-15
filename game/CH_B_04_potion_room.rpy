# CH_B_04_potion_room.rpy

label CH_B_04_potion_room:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"
    stop voice
    scene potion_room at fullscreen_bg
    with fade
    voice "audio/voice/b/04/0_0_次のフロア.mp3"
    narrator_arrow "次のフロアに入った途端、異様な香りが鼻をつく。\n"
    voice "audio/voice/b/04/0_1_棚には色と.mp3"
    extend "棚には色とりどりの瓶が並び、それぞれに奇妙な液体が入っている。\n"
    voice "audio/voice/b/04/0_2_調薬をして.mp3"
    extend "調薬をしていた部屋なのだろうか。\n"
    voice "audio/voice/b/04/0_3_この場所で.mp3"
    extend "この場所で調合した薬が、今もそのまま保管されているのだろう。\n"
    voice "audio/voice/b/04/0_4_部屋の一角.mp3"
    extend "部屋の一角には調合台があり、その上にはまだ使われていない薬草や器具が散乱している。\n"
    voice "audio/voice/b/04/0_5_きわには古.mp3"
    extend "際には古びた本棚が立ち並び、古代の書物が所狭しと詰め込まれている。\n"
    voice "audio/voice/b/04/0_6_部屋の奥に.mp3"
    extend "部屋の奥に目をやると、次のフロアへと続く重厚な扉が見える。\n"
    voice "audio/voice/b/04/0_7_しかし、そ.mp3"
    extend "しかし、その扉には頑丈な錠前がかけられており、このままでは先に進むことができない。\n"
    voice "audio/voice/b/04/0_8_鍵がこの部.mp3"
    extend "鍵がこの部屋のどこかに隠されているのだろうか。"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/b/04/2_0_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？"
    menu:

        "１．ラベルのない瓶を飲んでみる。その中身が何かはわからず、危険を伴うかもしれない。":
            stop music
            stop voice
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene potion_bottle at fullscreen_bg
            voice "audio/voice/b/04/1_0_飲んだ薬は.mp3"
            narrator_arrow "飲んだ薬は、どうやら下剤だったようだ。\n"
            voice "audio/voice/b/04/1_1_あなたは出.mp3"
            extend "あなたは出口を探す前に、トイレを探す羽目になってしまった！\n"

            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()

        "２．調合台の裏を調べる。研究者たちが何か隠していた可能性がある。":
            
            stop music
            stop voice
            play sound "audio/se/発見.mp3"
            scene potion_door at fullscreen_bg
            voice "audio/voice/b/04/0_0_調合台の裏.mp3"
            narrator_arrow "調合台の裏を調べると、隠された鍵を見つけた。\n"
            voice "audio/voice/b/04/0_1_この鍵で部.mp3"
            extend "この鍵で部屋の扉を開ける、次のフロアに進もう。"

            scene black
            with Dissolve(1.0)
            jump CH_B_05_garden
            
        "３．古びた本棚を動かしてみる。本棚の裏に手がかりがあるかもしれない。":
            stop music
            stop voice
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene black
            voice "audio/voice/b/04/0_0_本棚の後ろ.mp3"
            narrator_arrow "本棚の後ろには何もなく、時間を無駄にしてしまった。\n"
            voice "audio/voice/b/04/0_1_あなたはす.mp3"
            extend "あなたはすべてをあきらめた。\n"
            voice "audio/voice/ゲームオーバー.mp3"
            scene skeleton_bad at fullscreen_bg
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()



    $ choice_comment = ""  