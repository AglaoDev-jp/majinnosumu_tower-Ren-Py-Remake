# CH_C_08_monster_bird

label CH_C_08_monster_bird:

    window hide
    play music "audio/se/魔法使いが空を飛ぶ.mp3" 
    scene bright_corridor at fullscreen_bg
    with fade
    voice "audio/voice/c/08/0_19_暗い通路を.mp3"
    $ ctc_mode = "page"
    narrator_arrow "暗い通路を抜け扉を開けると、目の前には予想外の光景が広がっていた。\n"
    scene rooftop at fullscreen_bg
    with fade
    voice "audio/voice/c/08/0_20_そこは屋上.mp3"
    narrator_arrow "そこは屋上だった。\n"
    voice "audio/voice/c/08/0_21_どうやら、.mp3"
    extend "どうやら、ここが塔の最上階のようだ。\n"
    voice "audio/voice/c/08/0_22_広がる青空.mp3"
    extend "広がる青空と吹き抜ける風に一瞬で心が解き放たれる。\n"
    voice "audio/voice/c/08/0_23_閉塞感のあ.mp3"
    extend "閉塞感のある迷宮を彷徨ってきたため、外気を感じることができた喜びは言葉にできない。\n"
    voice "audio/voice/c/08/0_24_やっとおも.mp3"
    $ ctc_mode = "page"
    extend "やっと表に出られたという安堵感が全身を包み込む。\n"

    scene black
    voice "audio/voice/c/08/0_25_ふと、強烈.mp3"
    narrator_arrow "ふと、強烈な視線を感じた。\n"
    voice "audio/voice/c/08/0_26_その静寂を.mp3"
    extend "その静寂を破るかのように、巨大な影がゆっくりと動き出した。\n"

    scene monster_bird_1 at fullscreen_bg
    with fade
    voice "audio/voice/c/08/0_27_目を向ける.mp3"
    extend "目を向けると、３ｍ程の巨大な怪鳥がこちらをじっと見つめているではないか。\n"
    voice "audio/voice/c/08/0_28_怪鳥はゆっ.mp3"
    $ ctc_mode = "page"
    extend "怪鳥はゆっくりと翼を広げ、その鋭い目であなたを捉えた。\n"

    voice "audio/voice/c/08/0_29_「ほう…人.mp3"
    narrator_arrow "「ほう…人間がここまでたどり着くとは…珍しいなぁ。」\n"
    voice "audio/voice/c/08/0_30_怪鳥はあな.mp3"
    extend "怪鳥はあなたに興味を示しながら、軽く首をかしげた。\n"
    stop music
    play sound "audio/se/発見.mp3"
    scene black
    voice "audio/voice/c/08/0_31_あなたはこ.mp3"
    extend "あなたはこの怪鳥に、経緯を話してみようと思った。\n"
    voice "audio/voice/c/08/0_32_塔の魔人に.mp3"
    extend "塔の魔人に村から連れ去られ地下牢に囚われていたこと、"
    voice "audio/voice/c/08/0_33_そこからな.mp3"
    $ ctc_mode = "page"
    extend "そこからなんとか脱出し、最上階まで上がってきたことを伝えた。\n"

    scene monster_bird_2 at fullscreen_bg
    with fade
    play music "audio/bgm/strange_lullaby.mp3"
    voice "audio/voice/c/08/0_34_この怪鳥は.mp3"
    narrator_arrow "この怪鳥は、意外なほど同情的に耳を傾けてくれた。\n"
    voice "audio/voice/c/08/0_35_「なるほど.mp3"
    extend "「なるほど…あの忌々しい魔人にそんな仕打ちを…そいつぁ災難だったなぁ。」\n"
    voice "audio/voice/c/08/0_36_怪鳥は軽く.mp3"
    extend "怪鳥は軽くため息をつき、あなたを見つめた。\n"
    scene monster_bird_2 at fullscreen_bg
    voice "audio/voice/c/08/0_37_「本来ワシ.mp3"
    extend "「本来ワシこそが、この塔の主なのだ。"
    voice "audio/voice/c/08/0_38_しばらく留.mp3"
    extend "しばらく留守にしている間に、その魔人が住み着いて…面倒なことになっていてな。"
    voice "audio/voice/c/08/0_39_お前も地下.mp3"
    extend "お前も地下で酷い目に遭ったようだが、ワシも奴には手を焼いていてな。"
    voice "audio/voice/c/08/0_40_いっそ、追.mp3"
    $ ctc_mode = "page"
    extend "いっそ、追い払ってしまいたいんだが、やつも中々手強くてな…。」\n"

    scene monster_bird_3 at fullscreen_bg
    with fade
    voice "audio/voice/c/08/0_41_怪鳥は、し.mp3"
    narrator_arrow "怪鳥は、しばらく考えるように目を閉じた後、笑みを浮かべた。\n"
    voice "audio/voice/c/08/0_42_「お前、地.mp3"
    extend "「お前、地下牢から脱出してここまで来たってんなら、途中で書庫に寄らなかったか？"
    voice "audio/voice/c/08/0_43_あそこには.mp3"
    $ ctc_mode = "page"
    extend "あそこには、魔人を封じる魔法書があったはずだ…何て名前の本だったかなぁ？」\n"

    play music "audio/bgm/奇妙な話.mp3"

    voice "audio/voice/c/08/0_44_魔人を封じ.mp3"
    $ choice_comment = "魔人を封じる魔法書の名前は？"

    menu:

        "１．古代の魔法書から学んだ魔人の秘密":
            jump monster_bird_q_Correct_1  

        "２．失われた王国の魔人の記録":
            jump monster_bird_q_Incorrect_1

        "３．影の中の魔人に関する研究書":
            jump monster_bird_q_Incorrect_1


    $ choice_comment = ""  

label monster_bird_q_Correct_1:

    window hide
    scene monster_bird_1 at fullscreen_bg

    play sound "audio/se/発見.mp3"
    voice "audio/voice/c/08/1_0_「ほうほう.mp3"
    narrator_arrow "「ほうほう、見つけてたか。」\n"
    voice "audio/voice/c/08/1_1_少し首をか.mp3"
    extend "少し首をかしげてみせる。\n"
    voice "audio/voice/c/08/1_2_怪鳥は鋭い.mp3"
    extend "怪鳥は鋭い目であなたを見つめながら問いかけた。\n"
    voice "audio/voice/c/08/1_3_「じゃあお.mp3"
    $ ctc_mode = "page"
    extend "「じゃあお前、その魔法書を開いたか？何が書かれてあった？」\n"

    voice "audio/voice/c/08/1_3_魔法書には.mp3"
    $ choice_comment = "魔法書には何が書かれていた？" 

    menu:

        "１．魔人を封じるための魔法と、その詠唱の詳細が書かれていたと答える。":
            jump monster_bird_q_Correct_2  

        "２．魔人を石化する魔法と、その詠唱の詳細が書かれていたと答える。":
            jump monster_bird_q_Incorrect_2

        "３．魔人を眠らせる魔法と、その詠唱の詳細が書かれていたと答える。":
            jump monster_bird_q_Incorrect_2


    $ choice_comment = ""  

label monster_bird_q_Correct_2:

    
    window hide
    scene monster_bird_1 at fullscreen_bg

    play sound "audio/se/発見.mp3"
    voice "audio/voice/c/08/1_4_「なるほど.mp3"
    narrator_arrow "「なるほど、では封印の方法を知っているのか。」\n"
    voice "audio/voice/c/08/1_1_怪鳥は少し.mp3"
    extend "怪鳥は少し考えるように目を閉じ、そしてふと何かを思い出したように目を開いた。\n"
    voice "audio/voice/c/08/1_6_「そういえ.mp3"
    extend "「そういえば、お前がこの塔を上ってくる途中で、石像を見ただろう？\n"
    voice "audio/voice/c/08/1_7_「その石像.mp3"
    $ ctc_mode = "page"
    extend "その石像、何か話しかけてこなかったか？」\n"

    voice "audio/voice/c/08/1_8_石像に、good.mp3"
    $ choice_comment = "石像に、何と話しかけられた？" 

    menu:

        "１．「はい、石像が『守護の言葉を唱えよ』と言いました。」":
            jump CH_C_08_monster_bird_bad_end

        "２．「はい、石像が、『何かを解き明かせ』と言っていたようでした。」":
            jump CH_C_08_monster_bird_bad_end

        "３．「いいえ、石像は何も話しかけませんでした。」":
            jump CH_C_08_monster_bird_good_end


    $ choice_comment = ""  

# --------　はずれルート　-------------------------------------------------------------------------------

label monster_bird_q_Incorrect_1:

    
    window hide
    scene monster_bird_1 at fullscreen_bg

    voice "audio/voice/c/08/1_0_「はて、そ.mp3"
    narrator_arrow "「はて、そのような本だったかなあ？」\n"
    voice "audio/voice/c/08/1_5_怪鳥は、少.mp3"
    extend "怪鳥は、少し首をかしげた。\n"
    voice "audio/voice/c/08/1_2_怪鳥は鋭い.mp3"
    extend "怪鳥は鋭い目であなたを見つめながら問いかけた。\n"
    voice "audio/voice/c/08/1_3_「じゃあお.mp3"
    $ ctc_mode = "page"
    extend "「じゃあお前、その魔法書を開いたか？何が書かれてあった？」\n"

    voice "audio/voice/c/08/1_3_魔法書には.mp3"
    $ choice_comment = "魔法書には何が書かれていた？" 

    menu:

        "１．魔人を封じるための魔法と、その詠唱の詳細が書かれていたと答える。":
            jump monster_bird_q_Incorrect_2  

        "２．魔人を石化する魔法と、その詠唱の詳細が書かれていたと答える。":
            jump monster_bird_q_Incorrect_2

        "３．魔人を眠らせる魔法と、その詠唱の詳細が書かれていたと答える。":
            jump monster_bird_q_Incorrect_2


    $ choice_comment = ""  

label monster_bird_q_Incorrect_2:

    
    window hide
    scene monster_bird_1 at fullscreen_bg

    voice "audio/voice/c/08/1_4_「そうか….mp3"
    narrator_arrow "「そうか…残念だなぁ」\n"
    voice "audio/voice/c/08/1_1_怪鳥は少し.mp3"
    extend "怪鳥は少し考えるように目を閉じ、そしてふと何かを思い出したように目を開いた。\n"
    voice "audio/voice/c/08/1_6_「そういえ.mp3"
    extend "「そういえば、お前がこの塔を上ってくる途中で、石像を見ただろう？\n"
    voice "audio/voice/c/08/1_7_「その石像.mp3"
    $ ctc_mode = "page"
    extend "その石像、何か話しかけてこなかったか？」\n"

    voice "audio/voice/c/08/1_9_石像に、bad.mp3"
    $ choice_comment = "石像に、何と話しかけられた？" 

    menu:

        "１．「はい、石像が『守護の言葉を唱えよ』と言いました。」":
            jump CH_C_08_monster_bird_bad_end

        "２．「はい、石像が、『何かを解き明かせ』と言っていたようでした。」":
            jump CH_C_08_monster_bird_bad_end

        "３．「はい、石像が『注意深く進め』と言いました。」":
            jump CH_C_08_monster_bird_bad_end


    $ choice_comment = ""  