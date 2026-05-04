# CH_B_09_Confronting_the_devil_GOOD_1.rpy

label CH_B_09_Confronting_the_devil_GOOD_1 :

    window hide
    stop voice
    play music "audio/bgm/透明な亡霊.mp3"

    scene princess_up at fullscreen_bg
    with fade
    voice "audio/voice/b/09g1/0_0_あなたは魔.mp3"
    narrator_arrow "あなたは魔人の脅迫に対し、アリアーナの意見を聞くことにした。\n"
    voice "audio/voice/b/09g1/0_1_彼女のそば.mp3"
    extend "彼女の側に立ち、そっと耳を傾ける。\n"
    voice "audio/voice/b/09g1/0_2_アリアーナ.mp3"
    extend "アリアーナの瞳には決意の光が宿っている。\n"
    voice "audio/voice/b/09g1/0_3_アリアーナ.mp3"
    extend "アリアーナは一瞬、剣を見つめた後、静かに口を開く。\n"
    voice "audio/voice/b/09g1/1_0_「その剣….mp3"
    extend "「その剣…私に渡して。"
    voice "audio/voice/b/09g1/1_1_わたし、使.mp3"
    $ ctc_mode = "page"
    extend "私、使えるかもしれない。」\n"

    scene princess_and_sword at fullscreen_bg
    with fade
    voice "audio/voice/b/09g1/0_6_驚きと共に.mp3"
    narrator_arrow "驚きと共に、あなたは彼女の言葉に従い、勇者の剣を彼女の手にそっと差し出す。\n"
    voice "audio/voice/b/09g1/0_7_剣を手にし.mp3"
    extend "剣を手にしたアリアーナの姿が、どこか神秘的な輝きを帯びているように見える。\n"
    voice "audio/voice/b/09g1/0_8_彼女は剣を.mp3"
    extend "彼女は剣を両手でしっかりと握りしめ、その刃を静かに構えた。\n"
    voice "audio/voice/b/09g1/0_9_魔人はその.mp3"
    extend "魔人はその様子を見て不敵に笑う。\n"
    voice "audio/voice/b/09g1/3_0_「アリアー.mp3"
    $ ctc_mode = "page"
    extend "「アリアーナ、お前が勇者の剣を使うなど、愚かにも程がある。」\n"

    jump CH_B_09_GOOD_END




