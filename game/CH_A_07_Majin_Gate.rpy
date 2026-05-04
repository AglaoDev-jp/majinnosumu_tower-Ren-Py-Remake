# CH_A_07_Majin_Gate

label CH_A_07_Majin_Gate:

    window hide

    play music "audio/bgm/strange_lullaby.mp3"
    scene forest_entrance_2 at fullscreen_bg
    with fade

    voice "audio/voice/a/07/0_0_あなたは薄.mp3"
    narrator_arrow "あなたは薄暗い森を抜け、ついに魔人の守る門へとたどり着く。\n"
    voice "audio/voice/a/07/0_1_その門は巨.mp3"
    extend "その門は巨大で、堅牢な石造りできており、まるで大地に根を下ろしたかのように、威圧的にそびえ立っている。\n"
    voice "audio/voice/a/07/0_2_門に一歩近.mp3"
    extend "門に一歩近づいた瞬間、冷たい風が吹き抜け、周囲の空気が一変する。\n"
    voice "audio/voice/a/07/0_3_突然、門の.mp3"
    $ ctc_mode = "page"
    extend "突然、門の前に薄暗い霧が立ち込め、徐々に魔人の姿が浮かび上がった。\n"

    scene demon_gate at fullscreen_bg
    with fade
    voice "audio/voice/a/07/0_4_それは、魔.mp3"
    narrator_arrow "それは、魔法によって生み出された偶像であり、まるで生きているかのようにあなたを睨みつける。\n"
    voice "audio/voice/a/07/0_5_魔人の偶像.mp3"
    extend "魔人の偶像が口を開き、低く不気味な声で囁く。\n"
    voice "audio/voice/a/07/0_6_「愚かな者.mp3"
    extend "「愚かな者よ、この門を越えることは許されぬ。」\n"
    voice "audio/voice/a/07/0_7_その言葉に.mp3"
    $ ctc_mode = "page"
    extend "その言葉に圧倒されながらも、あなたは戦士たちから教わった攻略方法を思い出す。\n"

    voice "audio/voice/a/07/0_8_攻略方法を.mp3"
    play music "audio/bgm/奇妙な話.mp3"
    $ choice_comment = "攻略方法を思い出そう。" 

    menu:

        "１．門の両脇にある石碑に隠された呪文を唱える。":
            jump CH_A_07_Majin_Gate_end
        "２．剣を門に向けて掲げ、剣の力を解放する。":
            jump CH_A_07_Majin_Gate_loop_1            
        "３．門を無視して他の道を探す。":
            jump CH_A_07_Majin_Gate_loop_2


    $ choice_comment = "" 

# --------------------------------------------------------------------------------------

label CH_A_07_Majin_Gate_loop_1:

    window hide
    scene sword_a at fullscreen_bg
    play music "audio/bgm/strange_lullaby.mp3"
    voice "audio/voice/a/07/1_0_しかし、剣.mp3"
    narrator_arrow "しかし、剣の力は門の魔力に弾かれ、何も起こらない。\n"
    scene demon_gate at fullscreen_bg
    with fade
    voice "audio/voice/a/07/1_1_「愚かな者.mp3"
    extend "「愚かな者よ、力の使い方を知らぬようだな？」\n"
    voice "audio/voice/a/07/1_2_魔人の偶像.mp3"
    extend "魔人の偶像が嘲笑する。\n"
    voice "audio/voice/a/07/1_3_門の魔力が.mp3"
    extend "門の魔力が逆流し、あなたの体を痺れさせる。\n"
    voice "audio/voice/a/07/1_4_その瞬間、.mp3"
    extend "その瞬間、戦士たちが警告した呪文の重要性を思い出す。\n"
    voice "audio/voice/a/07/1_5_あなたは門.mp3"
    $ ctc_mode = "page"
    extend "あなたは門の前に立ち尽くし、再び戦士たちの言葉を思い出すことになる。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/a/07/1_6_再び戦士た.mp3"
    $ choice_comment = "再び戦士たちの言葉を思い出す。" 

    menu:

        "１．門の両脇にある石碑に隠された呪文を唱える。":
            jump CH_A_07_Majin_Gate_end          
        "２．門を無視して他の道を探す。":
            jump CH_A_07_Majin_Gate_loop_2


    $ choice_comment = ""  

label CH_A_07_Majin_Gate_loop_2:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"
    voice "audio/voice/a/07/2_0_戦士たちの.mp3"
    narrator_arrow "戦士たちの教えを無視し、別の道を探すことを選ぶ。\n"
    voice "audio/voice/a/07/2_1_しかし、す.mp3"
    extend "しかし、すでに魔人の門の強力な魔力が周囲を封じ込め、どこにも逃げ場がない！\n"
    voice "audio/voice/a/07/2_2_「愚か者よ.mp3"
    extend "「愚か者よ…この門を超えようとするなど、無謀の極みだ。」\n"
    voice "audio/voice/a/07/2_3_魔人は冷た.mp3"
    extend "魔人は冷たい笑みを浮かべ、その目には嘲りの光が宿っている。\n"
    voice "audio/voice/a/07/2_4_あなたは門.mp3"
    $ ctc_mode = "page"
    extend "あなたは門の前に立ち尽くし、再び戦士たちの言葉を思い出すことになる。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/a/07/2_5_再び戦士た.mp3"
    $ choice_comment = "再び戦士たちの言葉を思い出す。" 

    menu:

        "１．門の両脇にある石碑に隠された呪文を唱える。":
            jump CH_A_07_Majin_Gate_end          
        "２．剣を門に向けて掲げ、剣の力を解放する。":
            jump CH_A_07_Majin_Gate_loop_1 


    $ choice_comment = ""  