# CH_03_path_branch.rpy

label CH_03_path_branch:

    window hide
    stop voice
    scene black
    play music "audio/bgm/strange_lullaby.mp3"
    voice "audio/voice/s/03/0_0_あなたは一.mp3"
    narrator_arrow "あなたは一度立ち止まり、あたりをよく観察することにした。\n"
    voice "audio/voice/s/03/0_1_部屋の隅に.mp3"
    extend "部屋の隅に目を向けると、泡を吹いて倒れている看守を見つけた。\n"
    voice "audio/voice/s/03/0_2_死んではい.mp3"
    extend "死んではいないようだが、この場所で一体何があったのだろうか？\n"
    voice "audio/voice/s/03/0_3_看守はその.mp3"
    extend "看守はその場で何かを守ろうとしていたかのように手を握りしめている。\n"

    voice "audio/voice/s/03/0_4_あなたは慎.mp3"
    narrator_arrow "あなたは慎重に近づき、看守のポケットを探ってみる。\n"
    stop music
    play sound "audio/se/発見.mp3"
    scene key_answer at fullscreen_bg
    voice "audio/voice/s/03/0_5_小さな鍵が.mp3"
    extend "小さな鍵が握られていた。\n"
    play music "audio/bgm/strange_lullaby.mp3"
    voice "audio/voice/s/03/0_6_看守が隠し.mp3"
    extend "看守が隠していたこの鍵こそが、ドアを開けるためのものに違いない。\n"
    # ★scene black（全部切り替え）ではなく、黒を“上に重ねる”

    show black at fullscreen_bg with {"master": dissolve}

    voice "audio/voice/s/03/0_7_あなたは鍵.mp3"
    extend "あなたは鍵を手に取り、ドアの鍵穴に差し込んで回す。\n"
    play sound "audio/se/牢屋の扉を閉める.mp3"
    voice "audio/voice/s/03/0_8_カチッとい.mp3"
    extend "カチッという音とともに、重いドアがゆっくりと開き始めた。\n"
    voice "audio/voice/s/03/0_9_あなたは、.mp3"
    extend "あなたは、慎重に次の部屋へと進む。\n"

    scene branch at fullscreen_bg
    with fade
    voice "audio/voice/s/03/0_10_ここから先.mp3"
    narrator_arrow "ここから先は分かれ道のようだ。"

    voice "audio/voice/s/03/0_11_どちらへ進.mp3"
    $ choice_comment = "どちらへ進もうか？"

    menu:
        "１．右へ進む。":
            jump CH_A_04_hall            
        "２．左へ進む。":
            jump CH_B_04_potion_room
    $ choice_comment = ""  
