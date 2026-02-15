# CH_A_05_armory

label CH_A_05_armory:

    window hide

    play music "audio/bgm/strange_lullaby.mp3"
    scene armory at fullscreen_bg
    with fade

    voice "audio/voice/a/05/0_0_このフロア.mp3"
    narrator_arrow "このフロアは武器庫のようだ。\n"
    voice "audio/voice/a/05/0_1_足を踏み入.mp3"
    extend "足を踏み入れると、薄暗い照明の中に浮かび上がる古代の武器や甲冑の数々が目に入る。\n"
    voice "audio/voice/a/05/0_2_壁一面には.mp3"
    extend "壁一面には剣や槍、盾や鎧が整然と並べられている。\n"
    voice "audio/voice/a/05/0_3_部屋の中央.mp3"
    extend "部屋の中央には大きな甲冑が展示されており、その迫力に圧倒される。\n"
    voice "audio/voice/a/05/0_4_空気はひん.mp3"
    extend "空気はひんやりとしており、古い鉄の匂いが漂っている。\n"
    voice "audio/voice/a/05/0_5_奥へと足を.mp3"
    extend "奥へと足を進める。"

    $ renpy.music.set_volume(0.6, channel="music") # 音量を下げる。
    play music "audio/bgm/ENEMY_ENCOUNTER.mp3"
    scene attacking_armored_bone at fullscreen_bg
    voice "audio/voice/a/05/0_6_すると突然.mp3"
    narrator_arrow "すると突然、展示されていた甲冑が動き出した。\n"
    voice "audio/voice/a/05/0_7_恐ろしい音.mp3"
    extend "恐ろしい音を立ててこちらに向かってくるではないか！\n"
    voice "audio/voice/a/05/0_8_心臓が激し.mp3"
    extend "心臓が激しく鼓動する中、何とかしてこの危機を脱出しなければならない。\n"
    voice "audio/voice/a/05/0_9_慎重に行動.mp3"
    extend "慎重に行動しないと命を落とすことになるだろう。\n"
    voice "audio/voice/a/05/0_10_決断を下す.mp3"
    extend "決断を下す時が来た。"

    voice "audio/voice/a/05/0_11_選択肢は三.mp3"
    $ choice_comment = "選択肢は三つ。" 

    menu:

        "１．甲冑の間に隠れて進むことを試みる。しかし、見つかるリスクは大きいだろう。":
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene capturing_armored_bone at fullscreen_bg
            voice "audio/voice/a/05/1_0_甲冑に見つ.mp3"
            narrator_arrow "甲冑に見つかり、逃げる暇もなく腕を掴まれた。\n"
            voice "audio/voice/a/05/1_1_あなたは、.mp3"
            extend "あなたは、また囚われの身となるだろう。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() 

        "２．壁に掛けられた古い剣を手に取る。この剣には何か特別な力があるかもしれない。":
            stop music
            play sound "audio/se/発見.mp3"
            scene stopping_the_armored_bone at fullscreen_bg
            with fade
            voice "audio/voice/a/05/3_0_どうやらこ.mp3"
            narrator_arrow "どうやらこの剣がスイッチになっていたようだ。\n"
            voice "audio/voice/a/05/3_1_止まった甲.mp3"
            extend "止まった甲冑の横を抜け、あなたは慎重に進む。\n"
            scene sword_a at fullscreen_bg
            with fade
            voice "audio/voice/a/05/3_2_何かと物騒.mp3"
            extend "何かと物騒だ。この剣は拝借していこう。"
            $ renpy.music.set_volume(1.0, channel="music") # 音量を戻す。
            scene black
            with Dissolve(1.0)

            jump CH_A_06_Tomb_of_the_Warriors

        "３．近くの盾を使って防御する。攻撃を防げるかどうかは不明だが、試してみようか。":
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene defeated_armored_bone at fullscreen_bg
            voice "audio/voice/a/05/2_0_甲冑の攻撃.mp3"
            narrator_arrow "甲冑の攻撃を防げず、倒されてしまった。\n"
            voice "audio/voice/a/05/2_1_あなたは、.mp3"
            extend "あなたは、そのまま起き上がることはなかった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart()

    $ choice_comment = ""  