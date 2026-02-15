# CH_B_09_Confronting_the_devil_BAD_2.rpy

label CH_B_09_Confronting_the_devil_BAD_2:

    window hide
    stop voice
    play music "audio/se/風に揺れる草木1.mp3"

    scene sword_b at fullscreen_bg
    with fade
    voice "audio/voice/b/09b2/4_0_「ようやく.mp3"
    narrator_arrow "「ようやく手に入れたぞ、勇者の剣を！」\n"
    voice "audio/voice/b/09b2/1_1_魔人は歓喜.mp3"
    extend "魔人は歓喜の声を上げ、剣を高く掲げる。\n"
    scene black
    stop music fadeout 1.5
    play sound "audio/se/地響き.mp3"
    voice "audio/voice/b/09b2/1_2_その剣から.mp3"
    extend "その剣から放たれる力が増幅され、彼の邪悪な力と融合するように塔全体が震え始めた。\n"
    scene demon_laugh at fullscreen_bg
    stop sound fadeout 1.5
    voice "audio/voice/b/09b2/1_3_魔人は満足.mp3"
    extend "魔人は満足げに剣を受け取り、その力を得たことで邪悪な笑みを浮かべた。\n"
    voice "audio/voice/b/09b2/4_1_「これでお.mp3"
    extend "「これでお前には用はない。さっさと消え失せろ！」\n"


    scene black
    play sound "audio/se/小キック.mp3"
    voice "audio/voice/b/09b2/1_6_魔人はそう.mp3"
    narrator_arrow "魔人はそう言い放ち、片手であなたを払いのけるように振った。\n"
    voice "audio/voice/b/09b2/1_7_猛烈な力で.mp3"
    extend "猛烈な力であなたの体は宙を舞い、そのまま塔の出口へと飛ばされた。\n"
    play sound "audio/se/全力で踏み込む.mp3"
    voice "audio/voice/b/09b2/1_8_あなたは地.mp3"
    extend "あなたは地面にたたきつけられ、意識を失いそうになる。"

    scene stone_gate at fullscreen_bg
    stop music
    play sound "audio/se/「ギャアアアア！」.mp3"
    voice "audio/voice/b/09b2/1_9_しかし、塔.mp3"
    narrator_arrow "しかし、塔の中から響く、アリアーナの悲痛な叫び声がそうさせなかった。\n"
    voice "audio/voice/b/09b2/1_10_あなたは、.mp3"
    extend "あなたは、恐怖と絶望に駆られて、その場を逃げ出すことしかできなかった。\n"
    voice "audio/voice/ゲームオーバー.mp3"
    extend "ゲームオーバー"

    scene black
    with Dissolve(1.0)

    $ renpy.full_restart()