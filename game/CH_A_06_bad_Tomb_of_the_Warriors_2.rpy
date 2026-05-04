# CH_A_06_bad_Tomb_of_the_Warriors_2

label CH_A_06_bad_Tomb_of_the_Warriors_2:

    window hide

    play music "audio/se/風が吹く1.mp3"
    scene ghosts_1 at fullscreen_bg
    with fade

    voice "audio/voice/a/06b/1_0_あなたは、.mp3"
    narrator_arrow "あなたは、勇者でもないのに戦士たちの霊に囲まれた状況に嫌気がさした。\n"
    voice "audio/voice/a/06b/1_1_握りしめた.mp3"
    extend "握りしめた剣をしっかりと構える。\n"
    play sound "audio/se/剣の素振り1.mp3"
    voice "audio/voice/a/06b/1_2_そして、思.mp3"
    extend "そして、思い切って戦士たちの霊に向かって剣を振り下ろした！\n"
    play sound "audio/se/剣の素振り1.mp3"
    voice "audio/voice/a/06b/1_3_剣わくうを.mp3"
    extend "剣は空を切り裂き、霊の体に触れる。\n"
    play sound "audio/se/剣の素振り1.mp3"
    voice "audio/voice/a/06b/1_4_しかし、手.mp3"
    extend "しかし、手ごたえはまったくない。\n"
    play sound "audio/se/剣の素振り1.mp3"
    voice "audio/voice/a/06b/1_5_むしろ、剣.mp3"
    $ ctc_mode = "page"
    extend "むしろ、剣が霊の体を貫通した瞬間、霊たちの表情が恐ろしい怒りに変わった。\n"

    stop music
    play sound "audio/se/重力魔法2.mp3"
    scene ghosts_2 at fullscreen_bg
    voice "audio/voice/a/06b/1_6_「なんとい.mp3"
    narrator_arrow "「何という愚行…！」\n"
    voice "audio/voice/a/06b/1_7_「この剣の.mp3"
    extend "「この剣の持ち主でありながら、我らを攻撃するとは…許されざる罪だ…！」\n"
    voice "audio/voice/a/06b/1_8_「貴様は我.mp3"
    extend "「貴様は我らの信頼を裏切った。この剣に宿る力を汚し、我らを冒涜した…」\n"
    voice "audio/voice/a/06b/1_9_戦士たちの.mp3"
    $ ctc_mode = "page"
    extend "戦士たちの霊は、激しく怒り、あなたの周りに増え続ける。\n"

    show black at fullscreen_bg with {"master": dissolve}
    voice "audio/voice/a/06b/1_10_「貴様には.mp3"
    narrator_arrow "「貴様には相応の罰を与えよう！」\n"
    voice "audio/voice/a/06b/1_11_「…貴様に.mp3"
    extend "「…貴様にこの剣を持つ資格はない！」\n"
    voice "audio/voice/a/06b/1_12_戦士たちの.mp3"
    extend "戦士たちの霊が一斉に怒号を放ち、その声が耳をつんざく。\n"
    voice "audio/voice/a/06b/1_13_目の前が真.mp3"
    $ ctc_mode = "page"
    extend "目の前が真っ暗になり、あなたの意識は急速に奪われていく。\n"

    play sound "audio/se/怖い系リプレイ音.mp3"
    voice "audio/voice/a/06b/1_14_最後に感じ.mp3"
    narrator_arrow "最後に感じたのは、無限の闇に引きずり込まれる感覚だった。\n"
    voice "audio/voice/a/06b/1_15_あなたは戦.mp3"
    extend "あなたは戦士たちの墓で、永遠の闇に囚われることとなる。\n"
    voice "audio/voice/a/06b/1_16_こうして、.mp3"
    extend "こうして、あなたの冒険は無残な結末を迎え、戦士たちの怒りによって永遠に罰せられることになった。\n"
    scene skeleton_bad at fullscreen_bg
    voice "audio/voice/ゲームオーバー.mp3"
    $ ctc_mode = "page"
    extend "ゲームオーバー。\n"
    scene black
    with Dissolve(1.0)

    $ renpy.full_restart()
