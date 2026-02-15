# CH_B_09_Confronting_the_devil_GOOD_2.rpy

label CH_B_09_Confronting_the_devil_GOOD_2 :

    window hide
    stop voice
    play music "audio/bgm/透明な亡霊.mp3"

    scene princess_up at fullscreen_bg
    with fade
    voice "audio/voice/b/09g2/0_0_魔人の脅迫.mp3"
    narrator_arrow "魔人の脅迫に対して、あなたはどうするべきか迷っていた。\n"
    voice "audio/voice/b/09g2/0_1_そんなあな.mp3"
    extend "そんなあなたの耳元で、アリアーナが静かにささやく。\n"
    voice "audio/voice/b/09g2/2_0_わたしと剣.mp3"
    extend "「私と剣を魔人に渡して。"
    voice "audio/voice/b/09g2/2_1_どうかわた.mp3"
    extend "どうか私のことは気にせずに、逃げてください。」\n"
    voice "audio/voice/b/09g2/0_4_アリアーナ.mp3"
    extend "アリアーナの言葉に驚き、あなたは彼女を見つめる。\n"
    voice "audio/voice/b/09g2/0_5_彼女は真剣.mp3"
    extend "彼女は真剣な表情で頷く。\n"
    voice "audio/voice/b/09g2/0_6_絶望的な状.mp3"
    extend "絶望的な状況に追い込まれていたあなたは、提案を受け入れることを決意した。\n"
    voice "audio/voice/b/09g2/0_7_アリアーナ.mp3"
    extend "アリアーナを見つめ、申し訳ない気持ちで彼女と剣を魔人に差し出した。\n"

    scene black
    with fade
    voice "audio/voice/b/09g2/0_8_剣を手にし.mp3"
    narrator_arrow "剣を手にしたアリアーナの姿が、どこか神秘的な輝きを帯びているように見える。\n"
    voice "audio/voice/b/09g2/0_9_魔人は満足.mp3"
    extend "魔人は満足げに冷笑しながら剣を受け取り、アリアーナを引き寄せた。\n"
    scene demon_laugh at fullscreen_bg
    voice "audio/voice/b/09g2/2_0_「これでお.mp3"
    extend "「これでお前には用はない。」\n"
    stop music 
    play sound "audio/se/重力魔法2.mp3"    
    voice "audio/voice/b/09g2/0_11_魔人は、あ.mp3"
    extend "魔人は、あなたに向けて手から暗黒のエネルギーを放つ！"

    jump CH_B_09_GOOD_END



