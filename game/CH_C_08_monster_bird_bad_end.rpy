# CH_C_08_monster_bird_bad_end

label CH_C_08_monster_bird_bad_end:

    window hide
    stop music
    scene black
    play sound "audio/se/怪獣の足音.mp3"
    voice "audio/voice/c/08e/3_6_二人の話が.mp3"
    narrator_arrow "二人の話が終わったところで、階下から重々しい足音が響いてきた。\n"
    voice "audio/voice/c/08e/2_7_魔人が戻っ.mp3"
    $ ctc_mode = "page"
    extend "魔人が戻ってきたのだ。\n"

    scene demon_anger at fullscreen_bg
    play sound "audio/se/ゴブリンの鳴き声1.mp3"
    play music "audio/se/魔法使いが空を飛ぶ.mp3"
    voice "audio/voice/c/08e/2_8_「何をして.mp3"
    narrator_arrow "「何をしている？ここは私の居場所だぞ！」\n"
    voice "audio/voice/c/08e/2_10_怪鳥は冷静.mp3"
    extend "怪鳥は冷静に魔人を見返し、軽く肩をすくめた。\n"
    voice "audio/voice/c/08e/2_11_「おいおい.mp3"
    extend "「おいおい、落ち着けよ。ワシはただの傍観者さ。"
    voice "audio/voice/c/08e/2_13_でもな、お.mp3"
    extend "でもな、お前もそろそろこの塔から出て行く頃合いだろう。」\n"
    voice "audio/voice/c/08e/2_14_魔人は苛立.mp3"
    $ ctc_mode = "page"
    extend "魔人は苛立ちを隠しきれない。\n"


    voice "audio/voice/c/08e/2_15_「ふざける.mp3"
    narrator_arrow "「ふざけるな！ここは私の力を集めるための場所だ！お前に邪魔される筋合いはない！」\n"
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
    $ ctc_mode = "page"
    extend "お前ごときに干渉される筋合いはない！」\n"

    scene monster_bird_2 at fullscreen_bg
    voice "audio/voice/c/08e/2_25_怪鳥は肩を.mp3"   
    narrator_arrow "怪鳥は肩をすくめてから主人公の方をちらりと見た。\n"
    voice "audio/voice/c/08e/2_26_「まあ、こ.mp3"
    extend "「まあ、こんな調子だ。"
    voice "audio/voice/c/08e/2_27_やるなら今.mp3"
    extend "やるなら今だぞ。」\n"
    scene black
    stop music
    play sound "audio/se/剣の素振り1.mp3"
    voice "audio/voice/c/08e/3_28_あなたは、.mp3"
    extend "あなたは、魔人の胸に剣を突き刺した！\n"
    voice "audio/voice/c/08e/3_29_しかし剣は.mp3"
    extend "しかし剣は魔人の体をすり抜けるように通り抜けた。\n"

    play sound "audio/se/ゴブリンの鳴き声1.mp3"
    scene demon_laugh at fullscreen_bg
    voice "audio/voice/c/08e/3_30_「愚か者め.mp3"
    extend "「愚か者め、そんな攻撃が私に効くとでも思ったか？」\n"
    play sound "audio/se/重力魔法2.mp3"
    voice "audio/voice/c/08e/3_31_魔人は冷笑.mp3"
    $ ctc_mode = "page"
    extend "魔人は冷笑し、暗黒のエネルギーがその周りに渦巻き始めた。\n"

    scene chains_trapping_protagonist at fullscreen_bg
    play music "audio/se/締め付ける2.mp3"
    voice "audio/voice/c/08e/3_32_突然、床の.mp3"
    narrator_arrow "突然、床の下から無数の鎖が飛び出し、あなたの手足に絡みついた。"
    voice "audio/voice/c/08e/3_33_あなたは必.mp3"
    $ ctc_mode = "page"
    extend "あなたは必死に抵抗するが、鎖はどんどんきつく締まり、身動きが取れなくなった。\n"

    stop music
    play sound "audio/se/怖い系リプレイ音.mp3"
    voice "audio/voice/c/08e/3_34_魔人は高ら.mp3"
    narrator_arrow "魔人は高らかに笑い声を上げた。\n"
    show black at fullscreen_bg with {"master": dissolve}
    voice "audio/voice/c/08e/3_35_周囲の闇が.mp3"
    extend "周囲の闇がさらに濃くなり、視界は真っ暗になった。\n"
    voice "audio/voice/c/08e/3_36_「何もでき.mp3"
    extend "「何もできない無力な存在として、この場所で永遠に過ごすがいい…」\n"
    voice "audio/voice/c/08e/3_37_魔人の冷た.mp3"
    extend "魔人の冷たい声が響き渡り、あなたの意識は闇の中へと沈んでいった。\n"
    scene demon_laugh at fullscreen_bg
    with fade
    voice "audio/voice/ゲームオーバー.mp3"
    $ ctc_mode = "page"
    narrator_arrow "ゲームオーバー。\n"
    # タイトル画面へ
    $ renpy.full_restart()

