# CH_B_09_Confronting_the_devil_BAD_1.rpy

label CH_B_09_Confronting_the_devil_BAD_1:

    window hide
    stop voice
    play music "audio/se/風に揺れる草木1.mp3"
    scene black

    voice "audio/voice/b/09b1/0_0_あなたは、.mp3"
    narrator_arrow "あなたは、アリアーナの命を守るために勇者の剣を魔人に差し出すことを決断した。\n"
    voice "audio/voice/b/09b1/0_1_魔人は冷笑.mp3"
    extend "魔人は冷笑を浮かべながら手を伸ばし、ゆっくりと剣を受け取る。\n"
    scene sword_b at fullscreen_bg
    with fade
    voice "audio/voice/b/09b1/3_0_「ついに手.mp3"
    extend "「ついに手に入れたぞ、勇者の剣を！"
    voice "audio/voice/b/09b1/3_1_これで世界.mp3"
    $ ctc_mode = "page"
    extend "これで世界を支配する力を持つことができる！」\n"

    show black at fullscreen_bg with {"master": dissolve}
    voice "audio/voice/b/09b1/0_4_その瞬間、.mp3"
    narrator_arrow "その瞬間、あなたとアリアーナの心には不安が広がる。\n"
    voice "audio/voice/b/09b1/0_5_アリアーナ.mp3"
    $ ctc_mode = "page"
    extend "アリアーナはあなたを見つめ、悲しみと絶望の表情を浮かべている。\n"

    stop music
    scene demon_laugh at fullscreen_bg
    with fade
    play sound "audio/se/重力魔法2.mp3"
    voice "audio/voice/b/09b1/0_6_魔人が剣を.mp3"
    narrator_arrow "魔人が剣を手に入れたことで彼の力はさらに増大し、周囲の空気が重く、冷たくなっていくのが感じられる。\n"
    voice "audio/voice/b/09b1/0_8_魔人は再び.mp3"
    extend "魔人は再びあなたに目を向ける。\n"
    voice "audio/voice/b/09b1/3_1_「お前たち.mp3"
    $ ctc_mode = "page"
    extend "「お前たちは、もう価値はない。」\n"

    scene black
    play sound "audio/se/雷魔法4.mp3"
    voice "audio/voice/b/09b1/0_10_魔人の手か.mp3"
    narrator_arrow "魔人の手から暗黒のエネルギーが放たれ、あなたとアリアーナを飲み込む。\n"
    voice "audio/voice/b/09b1/0_11_目の前が暗.mp3"
    extend "目の前が暗転し、あなたは意識を失った。\n"
    voice "audio/voice/b/09b1/0_12_そのまま何.mp3"
    $ ctc_mode = "page"
    extend "そのまま何もかもが無に帰し、二度と目覚めることはなかった。\n"
    scene demon_laugh at fullscreen_bg
    with fade
    voice "audio/voice/ゲームオーバー.mp3"
    $ ctc_mode = "page"
    narrator_arrow "ゲームオーバー。\n"

    scene black
    with Dissolve(1.0)

    $ renpy.full_restart()