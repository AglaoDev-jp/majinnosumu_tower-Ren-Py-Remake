# CH_A_04_hall.rpy

label CH_A_04_hall:

    window hide

    # play music "audio/bgm/strange_lullaby.mp3" # 不自然なのでコメントアウト。問題があれば戻す。
    scene hall at fullscreen_bg
    with fade

    voice "audio/voice/a/04/0_0_長い通路の.mp3"
    narrator_arrow "長い通路の先は、広間だった。\n"
    voice "audio/voice/a/04/0_1_足を踏み入.mp3"
    extend "足を踏み入れると、その不釣り合いな豪華さに圧倒される。\n"
    voice "audio/voice/a/04/0_2_天井からは.mp3"
    extend "天井からは豪華なシャンデリア。\n"
    voice "audio/voice/a/04/0_3_壁一面には.mp3"
    extend "壁一面には古代の芸術を思わせるタペストリーが掛けられている。\n"
    voice "audio/voice/a/04/0_4_床には豪華.mp3"
    extend "床には豪華な絨毯が敷かれ、中央には巨大なテーブルがある。\n"
    voice "audio/voice/a/04/0_5_テーブルは.mp3"
    extend "テーブルは一見豪華ではあるが、食器類が散乱し、残飯が腐り果てている。\n"
    voice "audio/voice/a/04/0_6_隅々まで注.mp3"
    $ ctc_mode = "page"
    extend "隅々まで注意深く見渡すと、いくつか異変を見つけることができた。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/a/04/0_7_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？" 

    menu:

        "１．シャンデリアのチェーンを引いてみる。何か仕掛けがあるかもしれない。":
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene chandelier_fall at fullscreen_bg
            voice "audio/voice/a/04/1_0_シャンデリ.mp3"
            narrator_arrow "シャンデリアが落ちてきて、あなたは押しつぶされてしまった。\n"
            voice "audio/voice/a/04/1_1_その重さで.mp3"
            extend "その重さで、もうあなたは動けない！\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() 

        "２．巨大なテーブルの下を調べる。その下には何か秘密があるかもしれない。":
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene black
            voice "audio/voice/a/04/2_0_テーブルの.mp3"
            narrator_arrow "テーブルの下には、大量のネズミが！\n"
            voice "audio/voice/a/04/2_1_あなたは、.mp3"
            extend "あなたは、ショックで気絶してしまった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart()

        "３．壁に掛けられたタペストリー。タペストリーの裏に手がかりがあるかもしれない。":
            stop music
            play sound "audio/se/発見.mp3"
            scene tapestry_switch at fullscreen_bg

            voice "audio/voice/a/04/3_0_タペストリ.mp3"
            narrator_arrow "タペストリーの裏に、隠し扉のスイッチを見つけた。\n"
            voice "audio/voice/a/04/3_1_扉を抜ける.mp3"      
            $ ctc_mode = "page"      
            extend "扉を抜けると次のフロアへと続く。\n"
            scene black
            with Dissolve(1.0)

            jump CH_A_05_armory

        "４．隣の部屋に行ってみる。":
            jump CH_C_05_hidden_library

    $ choice_comment = ""  