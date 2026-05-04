# CH_B_09_GOOD_END.rpy

label CH_B_09_GOOD_END:

    window hide

    scene expression Solid("#ffffff")
    play music "audio/se/オーラ1.mp3"
    voice "audio/voice/b/09ge/0_11_しかし、次.mp3"
    narrator_arrow "しかし、次の瞬間、剣が強烈な光を放ち始めた。\n"
    voice "audio/voice/b/09ge/0_12_剣の光はま.mp3"
    $ ctc_mode = "page"
    extend "剣の光はまるで生きているかのように輝き、あたり一面に広がる。\n"
    stop music fadeout 2.0

    scene princess_and_dvil at fullscreen_bg
    with fade
    play music "audio/bgm/透明な亡霊.mp3"
    voice "audio/voice/b/09ge/0_13_魔人はその.mp3"
    narrator_arrow "魔人はその光を直視することができず、手で顔を覆った。\n"
    voice "audio/voice/b/09ge/3_1_「なんだ、.mp3"
    extend "「なんだ、これは…！？」\n"
    voice "audio/voice/b/09ge/0_16_魔人は目を.mp3"
    extend "魔人は目を見開き、驚愕の表情を浮かべている。\n"
    voice "audio/voice/b/09ge/0_17_アリアーナ.mp3"
    extend "アリアーナは強い声で叫ぶ。\n"
    voice "audio/voice/b/09ge/3_0_「私の祖先.mp3"
    extend "「私の祖先はかつて、この剣を託された者たちだった。"
    voice "audio/voice/b/09ge/3_1_この剣の力.mp3"
    $ ctc_mode = "page"
    extend "この剣の力は、私の血にも宿っているのです！」\n"

    scene expression Solid("#ffffff")

    play music "audio/se/オーラ1.mp3"
    voice "audio/voice/b/09ge/0_19_アリアーナ.mp3"
    narrator_arrow "アリアーナは剣を高く掲げ、その光を魔人に向けて放った。"
    voice "audio/voice/b/09ge/0_20_強烈な光が.mp3"
    $ ctc_mode = "page"
    extend "強烈な光が魔人を貫き、彼の邪悪な力を浄化していく。\n"

    scene demon_pained at fullscreen_bg
    voice "audio/voice/b/09ge/3_2_「やめろ….mp3"
    narrator_arrow "「やめろ…！やめろぉぉ…！」\n"
    voice "audio/voice/b/09ge/0_24_魔人は苦し.mp3"
    extend "魔人は苦しみながら叫ぶ。\n"
    stop music
    play sound "audio/se/雷魔法4.mp3"
    scene expression Solid("#ffffff")
    with fade
    voice "audio/voice/b/09ge/0_25_魔人の姿は.mp3"
    $ ctc_mode = "page"
    extend "魔人の姿は光の中で消え去り、塔の中には静寂が訪れた。\n"

    scene tower_gate at fullscreen_bg
    with fade
    play music "audio/se/風が吹く1.mp3" fadein 1.5
    voice "audio/voice/b/09ge/0_26_アリアーナ.mp3"
    narrator_arrow "アリアーナは深呼吸をし、剣を静かに降ろす。\n" 
    voice "audio/voice/b/09ge/1_2_「あなたの.mp3"
    extend "「あなたのおかげで、魔人を倒すことができました。"
    voice "audio/voice/b/09ge/1_2_感謝します.mp3"
    extend "感謝します。」\n"
    voice "audio/voice/b/09ge/1_3_「これから.mp3"
    extend "「これから、あなたをフィオリス王国にお連れします。"
    voice "audio/voice/b/09ge/1_4_フィオリス.mp3"
    extend "フィオリス王国の民は、あなたを勇者として迎え、心から感謝と敬意を示すでしょう。"
    voice "audio/voice/b/09ge/1_5_また、あな.mp3"
    extend "また、あなたは我が国に伝わる勇者の剣を託された者。"
    voice "audio/voice/b/09ge/1_6_これも天命.mp3"
    $ ctc_mode = "page"
    extend "これも天命ならば、フィオリス王国にあなたの重要な役割があるはずです。」\n"

    scene end_grassland_princess_up at fullscreen_bg
    with fade
    voice "audio/voice/b/09ge/0_32_彼女はあな.mp3"
    narrator_arrow "彼女はあなたの方を振り向き、微笑んで言う。\n" 
    voice "audio/voice/b/09ge/1_7_「あなたが.mp3"
    extend "「あなたがいなければ、きっと私はここまでたどり着けなかった。"
    voice "audio/voice/b/09ge/1_8_先祖の血に.mp3"
    extend "先祖の血に宿る、自分の力を信じることもできなかったでしょう。\n"
    voice "audio/voice/b/09ge/1_9_ありがとう.mp3"
    $ ctc_mode = "page"
    extend "ありがとう。{w=0.6}私に勇気を与えてくれて。」\n"

    play music "audio/bgm/プレリュード第2番「名前を入力してください」.mp3" noloop # noloopでループしない。

    scene end_grassland_princess at fullscreen_bg
    with fade

    # 現在の文字表示速度を退避（演出後に元へ戻すため）
    $ _old_cps = preferences.text_cps
    # エンディング用文字速度：1文字ずつゆっくり表示
    $ preferences.text_cps = 8

    # ============================================================
    # よく考えたら、それっぽく自動的に文章を流すのに特別なことは必要なかった。
    # ・{w=} で文章途中に間を入れる（息継ぎ／情景描写）
    # ・{p=} で行末の余韻を演出
    # ・{nw} によりクリック待ちせず自動で次の文章へ
    # ============================================================
    voice "audio/voice/b/09ge/0_37_塔の外では.mp3"
    "塔の外では、{w=0.6}曇っていた空が晴れ渡り、{w=0.6}太陽の光が新しい朝を告げている。{p=1.2}{nw}"
    voice "audio/voice/b/09ge/0_38_あなたとア.mp3"
    extend "あなたとアリアーナは塔を後にし、{w=0.6}平和な世界へと足を踏み出した。{p=1.2}{nw}"
    voice "audio/voice/b/09ge/0_39_魔人の脅威.mp3"
    extend "魔人の脅威は消え去り、{w=0.6}あなたたちの旅は無事に終わりを迎えたのだ。{p=3.0}{nw}"

    # エンディングBフラグ
    $ mark_ending("B")
    # 演出終了後、文字表示速度を元に戻す
    $ preferences.text_cps = _old_cps

    # スタッフロール（背景は残る／ENDで停止／クリックでフェードアウト＆音楽フェードアウト）
    call screen credits_scroll(scroll_time=40.0, fade_time=1.0, music_fade=2.0)

    # 余韻：必要ならここで黒に落としてからタイトルへ
    scene black
    with Dissolve(1.0)
    pause 0.8

    # タイトル画面へ
    $ renpy.full_restart()