# CH_B_09_Confronting_the_devil.rpy

label CH_B_09_Confronting_the_devil:

    window hide
    play music "audio/se/風が吹く1.mp3"

    scene passage at fullscreen_bg
    with fade

    voice "audio/voice/b/09/0_10_運よく隠し.mp3"
    narrator_arrow "運よく隠し通路を見つけることができた。\n"
    voice "audio/voice/b/09/0_11_普段、魔人.mp3"
    extend "普段、魔人が外出に使っているのだろう。\n"
    voice "audio/voice/b/09/0_12_隠し通路を.mp3"
    extend "隠し通路を抜け、あなたとアリアーナは、塔の出口にある巨大な門までたどり着いた。\n"
    scene tower_gate at fullscreen_bg
    voice "audio/voice/b/09/0_13_重厚な扉を.mp3"
    extend "重厚な扉を開けようとあなたが力を込めたその時、塔の内部から冷たい風が吹き抜けた。\n"
    voice "audio/voice/b/09/2_0_「おい、待.mp3"
    $ ctc_mode = "page"
    extend "「おい、待て。お前たち、どこへ行くつもりだ？」\n"

    scene demon_anger at fullscreen_bg

    play sound "audio/se/ゴブリンの鳴き声1.mp3"
    voice "audio/voice/b/09/0_16_振り返ると.mp3"
    narrator_arrow "振り返ると、そこには魔人が立ちはだかっていた。\n"
    voice "audio/voice/b/09/0_17_怒りに満ち.mp3"
    extend "怒りに満ちた目で二人を見据えている。\n"
    voice "audio/voice/b/09/2_1_「留守中に.mp3"
    extend "「留守中にまさか、この私の塔から逃げようとするとはな…」\n"
    voice "audio/voice/b/09/0_19_魔人の声が.mp3"
    extend "魔人の声が低く響き渡り、その場の空気が一層重くなる。\n"
    voice "audio/voice/b/09/2_2_「アリアー.mp3"
    $ ctc_mode = "page"
    extend "「アリアーナ、お前もか！私のもとから逃れられると思ったのか？」\n"

    scene black
    with fade
    voice "audio/voice/b/09/0_22_アリアーナ.mp3"
    narrator_arrow "アリアーナは、恐怖で声を失っている。\n"
    voice "audio/voice/b/09/0_23_あなたは、.mp3"
    extend "あなたは、彼女をかばうように前に立った。\n"
    scene sword_b at fullscreen_bg
    with fade
    voice "audio/voice/b/09/0_24_その時、魔.mp3"
    extend "その時、魔人は主人公の手に握られた剣に気づいた。\n"
    voice "audio/voice/b/09/0_25_魔人の表情.mp3"
    extend "魔人の表情は一変する。\n"
    scene demon_surprised at fullscreen_bg
    voice "audio/voice/b/09/2_3_「その剣….mp3"
    extend "「その剣…それは勇者の剣ではないか！」\n"
    voice "audio/voice/b/09/0_27_魔人は驚愕.mp3"
    extend "魔人は驚愕の表情を浮かべ、一瞬言葉を失ったようだった。\n"
    voice "audio/voice/b/09/2_4_「どこでそ.mp3"
    extend "「どこでそれを手に入れた？答えろ！」\n"
    voice "audio/voice/b/09/0_30_あなたは剣.mp3"
    $ ctc_mode = "page"
    extend "あなたはは剣を握りしめ、魔人に対して構えをとるが、魔人は冷笑を浮かべた。\n"

    scene demon_laugh at fullscreen_bg
    with fade
    voice "audio/voice/b/09/2_5_「勇者の剣.mp3"
    narrator_arrow "「勇者の剣がこの塔のどこかにあることはわかっていた。"
    voice "audio/voice/b/09/2_6_だからこそ.mp3"
    extend "だからこそ、この剣を探して私は長い間この塔に居座っていたのだ。"
    scene demon_anger at fullscreen_bg
    voice "audio/voice/b/09/2_7_お前のよう.mp3"
    extend "お前のような者が手にしていい代物ではない！」\n"
    scene black
    with fade
    voice "audio/voice/b/09/0_34_魔人は一歩.mp3"
    $ ctc_mode = "page"
    extend "魔人は一歩前に踏み出し、挑発的に言い放つ。\n"

    scene demon_laugh at fullscreen_bg
    with fade
    voice "audio/voice/b/09/2_8_「まあよい.mp3"
    narrator_arrow "「まあよい…取引をしてやる。"
    voice "audio/voice/b/09/2_9_剣とアリア.mp3"
    extend "剣とアリアーナを渡せば、お前一人は逃がしてやろう。"
    voice "audio/voice/b/09/2_10_どうする？.mp3"
    $ ctc_mode = "page"
    extend "どうする？私の言うことに従うか、それともここで命を散らすか？」\n"

    voice "audio/voice/b/09/0_39_さあ、どう.mp3"
    $ choice_comment = "さあ、どうする！？"
    menu:

        "１．剣を魔人に渡し、アリアーナを連れて逃げる。":
            jump CH_B_09_Confronting_the_devil_BAD_1         
        "２．剣を渡し、自分だけ逃げる。":
            jump CH_B_09_Confronting_the_devil_BAD_2
        "３．剣を渡さずに戦う。":
            jump CH_B_09_Confronting_the_devil_BAD_3
        "４．姫に相談する。":
            jump CH_B_09_Confronting_the_devil_GOOD_1          
        "５．姫と剣を渡して命乞いをする。":
            jump CH_B_09_Confronting_the_devil_GOOD_2

    $ choice_comment = ""  
