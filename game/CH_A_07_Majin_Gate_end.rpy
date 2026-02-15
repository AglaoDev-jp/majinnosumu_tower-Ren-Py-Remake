# CH_A_07_Majin_Gate_end

label CH_A_07_Majin_Gate_end:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"
    scene demon_gate at fullscreen_bg
    with fade

    voice "audio/voice/a/07e/0_0_あなたは門.mp3"
    narrator_arrow "あなたは門の両脇を注意深く観察する。\n"
    voice "audio/voice/a/07e/0_1_すると、そ.mp3"
    extend "すると、そこには戦士たちの亡霊に教わった、古い石碑らしきものを発見した。\n"
    voice "audio/voice/a/07e/0_2_確かにその.mp3"
    extend "確かにその石碑には、古代の言葉が刻まれていた。\n"
    voice "audio/voice/a/07e/0_3_戦士たちの.mp3"
    extend "戦士たちの教えに従い、静かにその言葉を唱え始める。\n"
    stop music
    play sound "audio/se/オーラ1.mp3"
    voice "audio/voice/a/07e/0_4_「Zara.mp3"
    extend "「Zarath ul'nevar, kashan ma'lor veshar...」\n"
    voice "audio/voice/a/07e/0_5_心を鎮め、.mp3"
    extend "心を鎮め、言葉を口にするたび、門の魔力が少しずつ弱まっていくのを感じる。\n"

    voice "audio/voice/a/07e/0_6_「貴様、何.mp3"
    narrator_arrow "「貴様、何をする！その言葉をやめろ！」\n"
    voice "audio/voice/a/07e/0_7_魔人の偶像.mp3"
    extend "魔人の偶像が叫び、怒りに震える。\n"
    voice "audio/voice/a/07e/0_8_しかし、あ.mp3"
    extend "しかし、あなたは動じることなく、呪文を続ける。\n"

    play sound "audio/se/オーラ1.mp3"
    voice "audio/voice/a/07e/0_9_「Arth.mp3"
    extend "「Arthan veranash, ilen'thar volos...」\n"
    voice "audio/voice/a/07e/0_10_魔人の偶像.mp3"
    extend "魔人の偶像はふたたび叫び声を上げるが、すでに遅い。\n"
    scene sword_a at fullscreen_bg
    voice "audio/voice/a/07e/0_11_魔力が弱ま.mp3"
    extend "魔力が弱まったのを見計らい、あなたは剣を高く掲げる。\n"
    voice "audio/voice/a/07e/0_12_「それは勇.mp3"
    extend "「それは勇者の剣！ま、待て！やめろ！」"

    voice "audio/voice/a/07e/0_13_その鋒から.mp3"
    narrator_arrow "その鋒から光が溢れ出し、門に向けて放たれる。\n"
    play sound "audio/se/地響き.mp3"
    voice "audio/voice/a/07e/0_14_剣の力が門.mp3"
    extend "剣の力が門を包み込むと、門全体が震え始めた。\n"
    play sound "audio/se/雷魔法4.mp3"
    show black at fullscreen_bg with {"master": dissolve}
    voice "audio/voice/a/07e/0_15_「ぐあああ.mp3"
    extend "「ぐああああっ！」\n"
    voice "audio/voice/a/07e/0_16_魔人の偶像.mp3"
    extend "魔人の偶像は断末魔の叫び声を上げ、次第に消え去っていった。\n"

    play music "audio/se/風が吹く1.mp3" fadein 1.5
    scene end_grassland at fullscreen_bg
    with fade
    voice "audio/voice/a/07e/0_17_魔人の守護.mp3"
    narrator_arrow "魔人の守護する門が開くと、あなたの前には広々とした平野が広がっていた。\n"
    voice "audio/voice/a/07e/0_18_門を通り抜.mp3"
    extend "門を通り抜けた瞬間、冷たい風が吹き抜け、魔力の残り香が消えていく。\n"
    voice "audio/voice/a/07e/0_19_門を出たあ.mp3"
    extend "門を出たあなたの前に、一人の戦士の霊がふわりと現れた。\n"
    voice "audio/voice/a/07e/0_20_穏やかな表.mp3"
    extend "穏やかな表情であなたに語りかける。"

    scene ghosts_3 at fullscreen_bg
    with fade
    voice "audio/voice/a/07e/0_21_「貴殿が魔.mp3"
    narrator_arrow "「貴殿が塔から勇者の剣を見つけ出し、魔人の門の魔力を打ち破ったおかげで我々の魂もようやくその役割を終えることができそうだ。"
    voice "audio/voice/a/07e/0_23_感謝する。.mp3"
    extend "感謝する。」\n"
    voice "audio/voice/a/07e/0_24_戦士の霊は.mp3"
    extend "戦士の霊は少しの間、遠くを見つめるように視線を向けた後、再びあなたに目を向ける。\n"
    voice "audio/voice/a/07e/0_25_「だが、魔.mp3"
    extend "「だが、魔人はまだどこかに潜んでいるはずだ。"
    voice "audio/voice/a/07e/0_26_この地に完.mp3"
    extend "この地に完全な平和が戻るには、まだ時間がかかるだろう。"
    voice "audio/voice/a/07e/0_27_しかし今、.mp3"
    extend "しかし今、まずはこの剣をフィオリス王国へ届けることが先決だ。"
    voice "audio/voice/a/07e/0_28_我らの使命.mp3"
    extend "我らの使命を果たすために、どうか無事に剣を届けてくれ。」"

    # 現在の文字表示速度を退避（演出後に元へ戻すため）
    $ _old_cps = preferences.text_cps
    # エンディング用文字速度：1文字ずつゆっくり表示
    $ preferences.text_cps = 9

    play music "audio/bgm/プレリュード第2番「名前を入力してください」.mp3" noloop # noloopでループしない。

    scene end_grassland at fullscreen_bg
    with fade
    voice "audio/voice/a/07e/0_29_戦士の霊は.mp3"
    "戦士の霊は、{w=0.6}あなたに深い感謝の意を示し、{w=0.6}静かに消えていった。{p=1.2}{nw}"
    voice "audio/voice/a/07e/0_30_あなたは剣.mp3"
    extend "あなたは剣をしっかりと握りしめ、フィオリス王国への道を進む決意を固める。{p=1.2}{nw}"
    voice "audio/voice/a/07e/0_31_剣を王国へ.mp3"
    extend "剣を王国へ届けるという新たな使命を胸に、{w=0.6}あなたの冒険の旅が再び始まる。{p=1.2}{nw}"
    voice "audio/voice/a/07e/0_32_広がる平野.mp3"
    extend "広がる平野の先にある、未知の道へと足を踏み出した。{p=1.2}{nw}"
    voice "audio/voice/a/07e/0_33_これからど.mp3"
    extend "これからどのような試練が待ち受けているかはわからない。{p=0.6}{nw}"
    voice "audio/voice/a/07e/0_34_しかし、あ.mp3"
    extend "しかし、あなたならば、きっとその使命を果たすことができるだろう。{p=3.0}{nw}"

    # エンディングCフラグ
    $ mark_ending("A")
    # 演出終了後、文字表示速度を元に戻す
    $ preferences.text_cps = _old_cps

    # スタッフロール（背景は残る／ENDで停止／クリックでフェードアウト＆音楽フェードアウト）
    call screen credits_scroll(scroll_time=28.0, fade_time=1.0, music_fade=2.0)

    # 余韻：必要ならここで黒に落としてからタイトルへ
    scene black
    with Dissolve(1.0)
    pause 0.8

    # タイトル画面へ
    $ renpy.full_restart()