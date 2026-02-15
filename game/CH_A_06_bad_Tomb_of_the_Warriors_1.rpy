# CH_A_06_bad_Tomb_of_the_Warriors_1

label CH_A_06_bad_Tomb_of_the_Warriors_1:

    window hide

    play music "audio/bgm/透明な亡霊.mp3"
    scene ghosts_1 at fullscreen_bg
    with fade

    voice "audio/voice/a/06b/0_0_あなたは戦.mp3"
    narrator_arrow "あなたは戦士たちの前に立ち、覚悟を決めて勇者だと名乗る。\n"
    voice "audio/voice/a/06b/0_1_胸の内では.mp3"
    extend "胸の内では、真実を隠すことへの罪悪感が渦巻いていたが、それでも彼らの期待に応えるために、あなたは嘘をつくことを選んだ。\n"
    voice "audio/voice/a/06b/0_2_戦士たちは.mp3"
    extend "戦士たちは歓喜の声を上げ、あなたにひざまずいて忠誠を誓った"

    voice "audio/voice/a/06b/0_3_「やっと….mp3"
    narrator_arrow "「やっと…やっと我らの待ち望んだ勇者が現れた！」\n"
    voice "audio/voice/a/06b/0_4_「この地に.mp3"
    extend "「この地に安寧をもたらしてくれるのだ！」\n"
    voice "audio/voice/a/06b/0_5_彼らの顔に.mp3"
    extend "彼らの顔には安堵と感謝の色が浮かび、あなたを神聖な存在として崇め始める。\n"
    voice "audio/voice/a/06b/0_6_戦士たちは.mp3"
    extend "戦士たちはあなたを中心に、儀式を始めた。\n"
    voice "audio/voice/a/06b/0_7_彼らの霊魂.mp3"
    extend "彼らの霊魂は一つに結びつき、まばゆい光を放ち始める。\n"
    scene sword_a at fullscreen_bg
    with fade
    voice "audio/voice/a/06b/0_8_その光の中.mp3"
    extend "その光の中で、あなたの剣も一層強く輝きを増していく。\n"
    play music "audio/se/風が吹く1.mp3"
    scene ghosts_1 at fullscreen_bg
    with fade
    voice "audio/voice/a/06b/0_9_しかし、そ.mp3"
    narrator_arrow "しかし、その瞬間、剣が震え、やがてその光が不自然に揺れ動き始める。\n"
    voice "audio/voice/a/06b/0_10_戦士たちの.mp3"
    extend "戦士たちの中の一人が不安そうに顔を上げ、あなたを見つめる。\n"
    voice "audio/voice/a/06b/0_11_「…おかし.mp3"
    extend "「…おかしい。何かが違う…」\n"
    voice "audio/voice/a/06b/0_12_彼の声に呼.mp3"
    extend "彼の声に呼応するように、他の戦士たちもざわめき始める。\n"
    voice "audio/voice/a/06b/0_13_やがて、一.mp3"
    extend "やがて、一人の戦士があなたに向かって叫んだ。\n"
    voice "audio/voice/a/06b/0_14_「お前は….mp3"
    extend "「お前は…本当に勇者なのか！？剣の輝きが、かつての勇者とは違う…！」\n"
    voice "audio/voice/a/06b/0_15_戦士たちの.mp3"
    extend "戦士たちの目は次第に疑念に満ち、その視線は冷たくなっていく。\n"

    stop music
    play sound "audio/se/重力魔法2.mp3"
    scene ghosts_2 at fullscreen_bg
    voice "audio/voice/a/06b/0_16_「この者は.mp3"
    narrator_arrow "「この者は偽物だ！我らを欺いていたのだ！」\n"
    voice "audio/voice/a/06b/0_17_怒りと失望.mp3"
    extend "怒りと失望に満ちた声が響き渡る。\n"
    voice "audio/voice/a/06b/0_18_戦士たちは.mp3"
    extend "戦士たちは一斉に立ち上がり、その霊体が不気味に膨れ上がり始める。\n"

    voice "audio/voice/a/06b/0_19_「許すこと.mp3"
    narrator_arrow "「許すことはできぬ…偽りの者よ、ここで永遠に朽ち果てるがいい！」\n"
    play sound "audio/se/怖い系リプレイ音.mp3"
    voice "audio/voice/a/06b/0_20_その言葉と.mp3"
    extend "その言葉と共に、彼らの霊魂があなたに襲いかかる。\n"
    voice "audio/voice/a/06b/0_21_無数の手が.mp3"
    extend "無数の手があなたを絡め取り、逃げ場を奪い取る。\n"
    voice "audio/voice/a/06b/0_22_あなたは剣.mp3"
    extend "あなたは剣を振りかざすが、力が抜けてまともに動かせない。\n"
    voice "audio/voice/a/06b/0_23_やがて、冷.mp3"
    extend "やがて、冷たい霊魂に体を包まれ、意識が遠のいていく。\n"

    voice "audio/voice/a/06b/0_24_最後に見た.mp3"
    narrator_arrow "最後に見たのは、戦士たちの無情な顔と、闇に飲み込まれていく光景だった。\n"
    voice "audio/voice/a/06b/0_25_こうして、.mp3"
    extend "こうして、あなたは偽りの勇者として、永遠に囚われることになった。\n"
    voice "audio/voice/a/06b/0_26_あなたが選.mp3"
    extend "あなたが選んだ道は、勇者の名を冒涜する者としての哀れな末路だった。\n"
    scene skeleton_bad at fullscreen_bg
    voice "audio/voice/ゲームオーバー.mp3"
    extend "ゲームオーバー。"
    scene black
    with Dissolve(1.0)

    $ renpy.full_restart()
