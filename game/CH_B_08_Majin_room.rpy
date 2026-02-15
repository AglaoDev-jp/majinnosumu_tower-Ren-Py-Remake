# CH_B_08_Majin_room.rpy

label CH_B_08_Majin_room:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"

    scene devil_room at fullscreen_bg
    with fade
    voice "audio/voice/b/08/0_3_あなたは、.mp3"
    narrator_arrow "あなたは、無骨な石の柱と石畳のフロアが広がる部屋に足を踏み入れた。\n"
    voice "audio/voice/b/08/0_4_どこか不穏.mp3"
    extend "どこか不穏な空気を感じるが、特に怪しげなものは見当たらない。\n"
    voice "audio/voice/b/08/0_5_部屋の奥に.mp3"
    extend "部屋の奥には、赤い絨毯が敷かれ、古びた玉座が見える。\n"
    voice "audio/voice/b/08/0_6_その光景に.mp3"
    extend "その光景に不思議な感覚を覚えながらも、あなたはさらに奥へと進む。\n"

    scene cage_like_prison at fullscreen_bg
    with fade
    voice "audio/voice/b/08/0_7_すると、巨.mp3"
    narrator_arrow "すると、巨大な鳥かごのような牢屋が目に入る。\n"
    voice "audio/voice/b/08/0_8_鉄の柵が厳.mp3"
    extend "鉄の柵が厳重に張り巡らされ、その中に一人の女性が囚われていた。\n"
    voice "audio/voice/b/08/0_9_彼女はうつ.mp3"
    extend "彼女は美しくも疲れた顔をしており、薄暗い部屋の中でその姿は、はかなげに見える。\n" # 儚げが文字化けする。

    scene princess_up at fullscreen_bg
    with fade
    voice "audio/voice/b/08/0_10_あなたがそ.mp3"
    narrator_arrow "あなたがその姿に気づいた瞬間、彼女もあなたに気づいた。\n"
    voice "audio/voice/b/08/0_11_そして、か.mp3"
    extend "そして、かすかな声で話しかけてくる。\n"
    voice "audio/voice/b/08/1_1_「わたしは.mp3"
    extend "「わたしは、フィオリス王国の王女アリアーナ…"
    voice "audio/voice/b/08/1_1_ここに閉じ.mp3"
    extend "ここに閉じ込められているの…"
    voice "audio/voice/b/08/1_2_お願い、助.mp3"
    extend "お願い、助けて欲しいのです…」\n"
    voice "audio/voice/b/08/0_12_彼女の視線.mp3"
    extend "彼女の視線が、ふとあなたが持つ剣に移る。\n"
    voice "audio/voice/b/08/0_13_驚きの表情.mp3"
    extend "驚きの表情を浮かべるが、その表情はすぐに曇る。"

    scene sword_b at fullscreen_bg
    with fade
    voice "audio/voice/b/08/1_3_「その剣….mp3"
    narrator_arrow "「その剣…それはフィオリス王国に伝わる伝説の勇者の剣！"
    voice "audio/voice/b/08/1_4_でも、あな.mp3"
    extend "でも、あなたは…違うんですね。"
    voice "audio/voice/b/08/1_5_勇者ではな.mp3"
    extend "勇者ではない…"
    voice "audio/voice/b/08/1_6_それでも、.mp3"
    extend "それでも、その剣を持っているということは、何かの運命かもしれません…」\n"
    voice "audio/voice/b/08/0_14_彼女は一瞬.mp3"
    extend "彼女は一瞬考え込んだ後、再び口を開く。"

    scene devil_room at fullscreen_bg
    with fade
    voice "audio/voice/b/08/1_7_「ここは、.mp3"
    narrator_arrow "「ここは、恐ろしい魔人が住む部屋なのです…"
    voice "audio/voice/b/08/1_8_幸い、今は.mp3"
    extend "幸い、今は魔人がいないようですが、いつ戻るかわかりません…"
    voice "audio/voice/b/08/1_9_お願いです.mp3"
    extend "お願いです、助けてください…"
    voice "audio/voice/b/08/1_10_あなたがそ.mp3"
    extend "あなたがその剣を持つならば、わたしはあなたをフィオリス王国へお連れせねばなりません。」"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/b/08/0_16_あなたは彼.mp3"
    $ choice_comment = "あなたは彼女の頼みに対して、どのように応えるだろうか？"
    menu:

        "１．助ける。":
            jump CH_B_08_Majin_room_loop_1          
        "２．助けない。":
            jump CH_B_08_Majin_room_loop_2
        "３．周囲を調べる。":
            jump CH_B_08_Majin_room_Clear


    $ choice_comment = ""  

label CH_B_08_Majin_room_loop_1:
    play music "audio/se/オーラ1.mp3"
    scene sword_b at fullscreen_bg
    voice "audio/voice/b/08/0_5_牢屋を打ち.mp3"
    narrator_arrow "牢屋を打ち破ろうと、あなたは剣を抜こうとする。\n"
    voice "audio/voice/b/08/0_6_剣はまるで.mp3"
    extend "剣はまるで石のように動かない。\n"

    stop music fadeout 2.0
    scene princess_up at fullscreen_bg
    with fade
    voice "audio/voice/b/08/0_7_アリアーナ.mp3"
    extend "アリアーナ王女が、悲しげに口を開く。\n"
    voice "audio/voice/b/08/1_1_「やはり….mp3"
    extend "「やはり…あなたは正統な後継者ではないのですね…"
    voice "audio/voice/b/08/1_2_この剣は、.mp3"
    extend "この剣は、真の勇者でなければ抜くことができないのです…」\n"
    voice "audio/voice/b/08/0_8_このままで.mp3"
    extend "このままでは助けられない。"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/b/08/0_11_あなたは再.mp3"
    $ choice_comment = "あなたは再び考え直すことになる。"
    menu:
        "１．助けない。":
            jump CH_B_08_Majin_room_loop_2

        "２．周囲を調べる。":
            jump CH_B_08_Majin_room_Clear

    $ choice_comment = ""  

label CH_B_08_Majin_room_loop_2:
    stop music
    play sound "audio/se/怖い系リプレイ音.mp3"
    scene princess_up at fullscreen_bg
    voice "audio/voice/b/08/0_0_あなたが助.mp3"
    narrator_arrow "あなたが助けるのを躊躇すると、アリアーナ王女は悲しそうな顔をして言葉を発する。\n"
    voice "audio/voice/b/08/1_0_「そんな….mp3"
    extend "「そんな…どうして…"
    voice "audio/voice/b/08/1_1_私にはもう.mp3"
    extend "私にはもう、誰も助けてくれる人がいないのですか…」\n"
    voice "audio/voice/b/08/0_1_アリアーナ.mp3"
    extend "アリアーナ王女が、悲しげに口を開く。\n"
    voice "audio/voice/b/08/0_2_彼女の言葉.mp3"
    extend "彼女の言葉に胸が痛んだあなたは、再び考え直すことにする。"
    voice "audio/voice/b/08/0_3_考え直そう.mp3"
    play music "audio/bgm/奇妙な話.mp3"

    $ choice_comment = "考え直そう。"
    menu:
        "１．助ける。":
            jump CH_B_08_Majin_room_loop_1

        "２．周囲を調べる。":
            jump CH_B_08_Majin_room_Clear

    $ choice_comment = ""  

label CH_B_08_Majin_room_Clear:
    play music "audio/bgm/strange_lullaby.mp3"
    scene devil_room at fullscreen_bg
    with fade
    voice "audio/voice/b/08/0_0_あなたは何.mp3"
    narrator_arrow "あなたは何か見落としているのではないかと感じ、部屋の周囲を慎重に調べ始める。\n"
    voice "audio/voice/b/08/0_1_石柱の隙間.mp3"
    extend "石柱の隙間や床の裂け目、古びた玉座の裏側まで、目を凝らして探し回る。\n"
    voice "audio/voice/b/08/0_2_すると、あ.mp3"
    extend "すると、あなたは玉座の後ろに目立たないレバーが埋め込まれているのを発見した。\n"
    voice "audio/voice/b/08/0_3_レバーの表.mp3"
    extend "レバーの表面は年月を経て錆びついているが、触れると確かな感触が伝わってくる。\n"
    voice "audio/voice/b/08/0_4_ためらいな.mp3"
    extend "ためらいながらも、あなたはレバーを引くことを決意する。\n"

    play sound "audio/se/鉄の扉を閉める.mp3"
    voice "audio/voice/b/08/0_5_ギシギシと.mp3"
    extend "ギシギシと音を立てて、レバーが動くと、部屋全体が微かに震えた。\n"
    stop music
    play sound "audio/se/発見.mp3"
    voice "audio/voice/b/08/0_6_すると、ア.mp3"
    extend "すると、アリアーナ王女が囚われている牢屋の鉄柵がゆっくりと開き始める。"

    scene princess_up at fullscreen_bg
    with fade
    voice "audio/voice/b/08/1_0_「…これで.mp3"
    "「…これで自由に…！」\n"
    voice "audio/voice/b/08/0_8_アリアーナ.mp3"
    extend "アリアーナ王女の顔に安堵の表情が浮かぶ。\n"
    voice "audio/voice/b/08/0_9_あなたは魔.mp3"
    extend "あなたは魔人の不在を祈りつつ、アリアーナ王女と共に次のフロアへと向かった。"
    scene black
    with Dissolve(1.0)
    jump CH_B_09_Confronting_the_devil