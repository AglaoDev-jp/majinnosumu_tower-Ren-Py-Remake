# CH_C_08_monster_bird_good_end

label CH_C_08_monster_bird_good_end:

    # テキストウインドウを完全に非表示にする。
    window hide
    stop voice
    stop music
    play sound "audio/se/発見.mp3"

    scene monster_bird_1 at fullscreen_bg
    with fade
    voice "audio/voice/c/08e/2_0_怪鳥はしば.mp3"
    narrator_arrow "怪鳥はしばらく考えるように目を閉じた後、少しニヒルな笑みを浮かべた。\n"
    play music "audio/bgm/透明な亡霊.mp3" 
    voice "audio/voice/c/08e/2_1_「お前、地.mp3"
    extend "「お前、地下牢から脱出してここまで来れたんなら、無力な人間じゃないだろう。"
    voice "audio/voice/c/08e/2_2_よし、ワシ.mp3"
    extend "よし、ワシがその魔法ってやつを使ってやろう。"
    voice "audio/voice/c/08e/2_3_なに、理屈.mp3"
    extend "なに、理屈が分かればたやすい魔法だ。"
    voice "audio/voice/c/08e/2_4_その隙にお.mp3"
    extend "その隙にお前が勇者の剣とやらで魔人の弱点をつけ。"
    voice "audio/voice/c/08e/2_5_悪い話では.mp3"
    extend "悪い話ではないだろう？」"

    scene black
    stop music
    play sound "audio/se/怪獣の足音.mp3"
    voice "audio/voice/c/08e/2_6_二人の作戦.mp3"
    narrator_arrow "二人の作戦が整ったところで、階下から重々しい足音が響いてきた。\n"
    voice "audio/voice/c/08e/2_7_魔人が戻っ.mp3"
    extend "魔人が戻ってきたのだ。"

    scene demon_anger at fullscreen_bg
    play sound "audio/se/ゴブリンの鳴き声1.mp3"
    play music "audio/se/魔法使いが空を飛ぶ.mp3" fadein 1.5
    voice "audio/voice/c/08e/2_8_「何をして.mp3"
    narrator_arrow "「何をしている？ここは私の居場所だぞ！」\n"
    voice "audio/voice/c/08e/2_10_怪鳥は冷静.mp3"
    extend "怪鳥は冷静に魔人を見返し、軽く肩をすくめた。\n"
    voice "audio/voice/c/08e/2_11_「おいおい.mp3"
    extend "「おいおい、落ち着けよ。ワシはただの傍観者さ。"
    voice "audio/voice/c/08e/2_13_でもな、お.mp3"
    extend "でもな、お前もそろそろこの塔から出て行く頃合いだろう。」\n"
    voice "audio/voice/c/08e/2_14_魔人は苛立.mp3"
    extend "魔人は苛立ちを隠しきれない。\n"
    voice "audio/voice/c/08e/2_15_「ふざける.mp3"
    extend "「ふざけるな！ここは私の力を集めるための場所だ！お前に邪魔される筋合いはない！」\n"
    voice "audio/voice/c/08e/2_18_怪鳥は冷や.mp3"
    extend "怪鳥は冷ややかな笑みを浮かべ、低く答えた。\n"
    voice "audio/voice/c/08e/2_19_「お前の力.mp3"
    extend "「お前の力がいかに強大だろうと、この塔には限界がある。"
    voice "audio/voice/c/08e/2_20_お前がここ.mp3"
    extend "お前がここで何をしているのかは知っているが、そろそろ潮時だ。」\n"
    voice "audio/voice/c/08e/2_21_魔人はさら.mp3"
    extend "魔人はさらに怒りを募らせ、目を見開いた。\n"
    voice "audio/voice/c/08e/2_22_「黙れ！.mp3"
    extend "「黙れ！"
    voice "audio/voice/c/08e/2_23_私の力はま.mp3"
    extend "私の力はまだ完全ではない。"
    voice "audio/voice/c/08e/2_24_お前ごとき.mp3"
    extend "お前ごときに干渉される筋合いはない！」"

    scene monster_bird_2 at fullscreen_bg
    play music "audio/bgm/ENEMY_ENCOUNTER.mp3"
    voice "audio/voice/c/08e/2_25_怪鳥は肩を.mp3"
    narrator_arrow "怪鳥は肩をすくめてから主人公の方をちらりと見た。\n"
    voice "audio/voice/c/08e/2_26_「まあ、こ.mp3"
    extend "「まあ、こんな調子だ。"
    voice "audio/voice/c/08e/2_27_やるなら今.mp3"
    extend "やるなら今だぞ。」\n"
    play sound "audio/se/オーラ1.mp3"
    voice "audio/voice/c/08e/2_28_その瞬間、.mp3"
    extend "その瞬間、怪鳥が低く呪文を唱え始めた。\n"
    scene demon_surprised at fullscreen_bg
    voice "audio/voice/c/08e/2_29_その呪文の.mp3"
    extend "その呪文の声が響き、魔人の動きが一瞬止まる。\n"
    stop sound
    voice "audio/voice/c/08e/2_30_「なに！.mp3"
    extend "「なに！この呪文は我々を封じ込めた魔法…！」\n"
    play sound "audio/se/弓矢が刺さる.mp3"
    voice "audio/voice/c/08e/2_32_あなたはす.mp3"
    extend "あなたはすぐに剣を取り出し、魔人の胸にある結晶を狙って突き刺した！\n"
    scene demon_pained at fullscreen_bg
    stop music
    play sound "audio/se/ガラスが割れる1.mp3"
    voice "audio/voice/c/08e/2_33_剣は魔人の.mp3"
    extend "剣は魔人の結晶に深く突き刺さり、光が一瞬弾けた。\n"
    voice "audio/voice/c/08e/2_35_「ぐぅ…！.mp3"
    extend "「ぐぅ…！貴様、この私にこんな傷を…！」\n"
    voice "audio/voice/c/08e/2_36_魔人は苦し.mp3"
    extend "魔人は苦しそうに呻いた。\n"
    play sound "audio/se/ゴブリンの鳴き声2.mp3"
    voice "audio/voice/c/08e/2_37_魔人はその.mp3"
    extend "魔人はその場にひざまずきながらも、低い声で呪いの言葉を吐いた。\n"
    scene expression Solid("#ffffff")
    voice "audio/voice/c/08e/2_38_「覚えてお.mp3"
    extend "「覚えておけ…私がこの程度で終わると思うな…いつか必ず復活してみせる…！」"

    voice "audio/voice/c/08e/2_39_その言葉を.mp3"
    narrator_arrow "その言葉を最後に、魔人は煙のように消え去った。"

    scene monster_bird_4 at fullscreen_bg
    with fade
    voice "audio/voice/c/08e/2_40_塔に漂って.mp3"
    narrator_arrow "塔に漂っていた不吉な気配がすっかり消え、静寂が戻った。\n"
    voice "audio/voice/c/08e/2_41_怪鳥は軽く.mp3"
    extend "怪鳥は軽く翼を広げ、あなたを見つめて微笑んだ。\n"
    voice "audio/voice/c/08e/2_42_「やれやれ.mp3"
    extend "「やれやれ、厄介者がいなくなって助かった。"
    voice "audio/voice/c/08e/2_43_これでワシ.mp3"
    extend "これでワシもやっと静かに過ごせるってもんだ。"
    voice "audio/voice/c/08e/2_44_致命傷では.mp3"
    extend "致命傷ではないようだが、あの調子なら300年は復活できまい。」\n"
    voice "audio/voice/c/08e/2_45_怪鳥はしば.mp3"
    extend "怪鳥はしばらくあなたを見つめた後、ふと考え込むような表情を浮かべた。"

    # 現在の文字表示速度を退避（演出後に元へ戻すため）
    $ _old_cps = preferences.text_cps
    # エンディング用文字速度：1文字ずつゆっくり表示
    $ preferences.text_cps = 12

    play music "audio/bgm/プレリュード第2番「名前を入力してください」.mp3" noloop # noloopでループしない。

    scene monster_bird_1 at fullscreen_bg
    with fade
    voice "audio/voice/c/08e/2_46_「ところで.mp3"
    "「ところで、{w=0.6}お前の住む村はどこだ？{w=0.6}{nw}"
    voice "audio/voice/c/08e/2_47_まさか、こ.mp3"
    extend "まさか、{w=0.6}このまま歩いて戻るつもりじゃないだろうな。{w=0.6}{nw}"
    voice "audio/voice/c/08e/2_48_まあ、ワシ.mp3"
    extend "まあ、ワシがここまで助けてやったんだ、{w=0.6}最後まで付き合ってやるさ。」{p=1.2}{nw}"
    voice "audio/voice/c/08e/2_49_怪鳥はそう.mp3"
    extend "怪鳥はそう言うと、{w=0.6}あなたをその広い背中に乗せた。{p=1.2}{nw}"
    voice "audio/voice/c/08e/2_50_あなたへの.mp3"
    extend "あなたへの礼のつもりだろう、{w=1.6}{nw}"
    voice "audio/voice/c/08e/2_51_村まで送っ.mp3"
    extend "村まで送ってくれるようだ。{p=1.2}{nw}"

    scene end_monstrou_bird at fullscreen_bg
    with fade
    voice "audio/voice/c/08e/2_52_翼を広げた.mp3"
    "翼を広げた怪鳥は、{w=0.6}塔の頂上から一気に飛び立ち、{w=0.6}空高く舞い上がった。{p=3.0}{nw}"

    # エンディングCフラグ
    $ mark_ending("C")
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

