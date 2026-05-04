# CH_B_09_Confronting_the_devil_BAD_2.rpy

label CH_B_09_Confronting_the_devil_BAD_3:

    window hide
    stop voice
    play music "audio/se/風に揺れる草木1.mp3"

    scene sword_b at fullscreen_bg
    with fade
    voice "audio/voice/b/09b3/2_0_魔人の脅し.mp3"
    narrator_arrow "魔人の脅しに対して、あなたは決して剣を渡さないと心に決める。\n"
    voice "audio/voice/b/09b3/2_1_アリアーナ.mp3"
    extend "アリアーナを守るため、この剣を手放すわけにはいかない。\n"
    voice "audio/voice/b/09b3/2_2_強い決意を.mp3"
    $ ctc_mode = "page"
    extend "強い決意を胸に、魔人に立ち向かう。\n"

    scene demon_anger at fullscreen_bg
    play sound "audio/se/ゴブリンの鳴き声1.mp3"
    voice "audio/voice/b/09b3/2_3_魔人はあな.mp3"
    narrator_arrow "魔人はあなたの姿を見て嘲笑を浮かべる。\n"
    voice "audio/voice/b/09b3/5_0_「お前のよ.mp3"
    extend "「お前のような者が、勇者の剣を使いこなせるとでも思ったか？"
    voice "audio/voice/b/09b3/5_1_無駄な抵抗.mp3"
    extend "無駄な抵抗だ！」\n"
    show black at fullscreen_bg with {"master": dissolve}
    voice "audio/voice/b/09b3/2_6_あなたは剣.mp3"
    extend "あなたは剣を抜こうとする。\n"
    voice "audio/voice/b/09b3/2_7_しかし、ど.mp3"
    extend "しかし、どんなに力を込めても、その刃はわずかに動くだけで、それ以上進まない。\n"
    voice "audio/voice/b/09b3/2_8_必死に剣を.mp3"
    extend "必死に剣を抜こうとするが、剣はまるで主人の指示を拒むように動かない。\n"
    voice "audio/voice/b/09b3/2_9_汗がひたい.mp3"
    $ ctc_mode = "page"
    extend "汗が額から流れ落ち、焦りが心を蝕んでいく。\n"

    scene demon_laugh at fullscreen_bg
    stop music
    play sound "audio/se/重力魔法2.mp3"
    voice "audio/voice/b/09b3/5_1_「そうか、.mp3"
    narrator_arrow "「そうか、お前が本当の勇者ではないことを、この剣もよく知っているのだ。」\n"
    voice "audio/voice/b/09b3/2_11_魔人は手を.mp3"
    extend "魔人は手を伸ばし、あなたの持つ剣を掴む。\n"
    scene sword_b at fullscreen_bg
    with fade
    voice "audio/voice/b/09b3/2_12_魔人は満足.mp3"
    extend "魔人は満足そうに笑いながら剣を掲げる。\n"
    voice "audio/voice/b/09b3/5_3_「これで終.mp3"
    extend "「これで終わりだ。"
    voice "audio/voice/b/09b3/5_4_勇者の剣は.mp3"
    $ ctc_mode = "page"
    extend "勇者の剣は私のもの、そしてお前たちの命も私の手の中にある。」\n"

    play sound "audio/se/雷魔法4.mp3"
    scene expression Solid("#000000")
    voice "audio/voice/b/09b3/2_15_一瞬のうち.mp3"
    narrator_arrow "一瞬のうちに、魔人の手から暗黒のエネルギーが放たれる。\n"
    voice "audio/voice/b/09b3/2_16_そのまま何.mp3"
    extend "そのまま何もかもが無に帰し、あなたは二度と目覚めることはなかった。\n"
    scene demon_laugh at fullscreen_bg
    with fade
    voice "audio/voice/ゲームオーバー.mp3"
    $ ctc_mode = "page"
    narrator_arrow "ゲームオーバー。\n"

    scene black
    with Dissolve(1.0)

    $ renpy.full_restart()