# CH_C_07_Heros_Statu


label CH_C_07_Heros_Statue:

    window hide
    stop sound fadeout 0.5
    play music "audio/bgm/strange_lullaby.mp3"
    scene hero_stone_statue at fullscreen_bg
    with fade
    voice "audio/voice/c/07/0_5_階段を重い.mp3"
    narrator_arrow "階段を重い足取りで登り切ると、そこは異様な静けさに包まれた広間だった。\n"
    voice "audio/voice/c/07/0_6_部屋の中央.mp3"
    extend "部屋の中央には、威厳と恐怖を兼ね備えた巨大な石像が立っている。\n"
    voice "audio/voice/c/07/0_7_その石像は.mp3"
    extend "その石像は、今にも動き出しそうなほど精巧に作られており、戦士の姿をしている。\n"
    voice "audio/voice/c/07/0_8_部屋に漂う.mp3"
    $ ctc_mode = "page"
    extend "部屋に漂う冷たい空気は、過去にここで何か恐ろしいことが起こったことを示唆している。\n"

    voice "audio/voice/c/07/0_9_あなたが石.mp3"
    narrator_arrow "あなたが石像に近づくと、どこからともなく声が響く。\n"
    voice "audio/voice/c/07/0_10_「この勇者.mp3"
    extend "「この勇者は、かつてこの地を守り抜いた英雄だ。"
    voice "audio/voice/c/07/0_11_しかし、彼.mp3"
    extend "しかし、彼は裏切りに遭い、永遠に石となって封じられた。"
    voice "audio/voice/c/07/0_12_今、この地.mp3"
    $ ctc_mode = "page"
    extend "今、この地は新たな英雄を待ち続けている…」\n"

    voice "audio/voice/c/07/0_13_声はそこで.mp3"
    narrator_arrow "声はそこで途切れ、再び静寂が戻った。\n"
    voice "audio/voice/c/07/0_14_だが、部屋.mp3"
    $ ctc_mode = "page"
    extend "だが、部屋の雰囲気は明らかに変わり、何かが起ころうとしているようだ。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/c/07/0_16_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？" 

    menu:

        "１．石像に向かって「自分が新たな英雄だ」と名乗り出る。":
            stop voice
            stop music
            voice "audio/voice/c/07/1_0_あなたは勇.mp3"
            narrator_arrow "あなたは勇気を振り絞り、自信を持って言い放つ。\n"
            voice "audio/voice/c/07/1_1_「私が、そ.mp3"
            $ ctc_mode = "page"
            extend "「私が、その新たな英雄だ！」\n"

            scene black
            voice "audio/voice/c/07/1_2_声が部屋中.mp3"
            narrator_arrow "声が部屋中に響き渡り、石像がゆっくりと動き始めた。\n"
            voice "audio/voice/c/07/1_3_石像の目が.mp3"
            extend "石像の目が突然赤く輝き出し、その剣を高々と掲げる。\n"
            voice "audio/voice/c/07/1_4_だが、その.mp3"
            $ ctc_mode = "page"
            extend "だが、その光景は恐ろしいほどに威圧的で、祝福の時とはまったく異なっている。\n"

            stop music
            play sound "audio/se/重力魔法2.mp3"
            scene fallen_hero_wrath at fullscreen_bg
            voice "audio/voice/c/07/1_5_「愚か者….mp3"
            narrator_arrow "「愚か者…」\n"
            voice "audio/voice/c/07/1_6_石像の口が.mp3"
            extend "石像の口が動いたかのように、その声が再び響く。\n"
            voice "audio/voice/c/07/1_7_「真の英雄.mp3"
            $ ctc_mode = "page"
            extend "「真の英雄でない者が、この地を救うことは許されない…」\n"

            scene black
            play sound "audio/se/岩にヒビが入る.mp3"          
            voice "audio/voice/c/07/1_8_突然、あな.mp3"
            narrator_arrow "突然、あなたの体は動かなくなり、全身が徐々に冷たく硬直していく。\n"
            voice "audio/voice/c/07/1_9_まるで石像.mp3"
            play sound "audio/se/岩にヒビが入る.mp3"
            extend "まるで石像と同じ運命を辿るかのように、あなたの肌は石化し始めた。\n"
            voice "audio/voice/c/07/1_10_必死にもが.mp3"
            $ ctc_mode = "page"
            extend "必死にもがくが、無情にも石像の力は止まらない。\n"

            scene escaping_prisoner_petrified at fullscreen_bg   
            play sound "audio/se/怖い系リプレイ音.mp3"     
            voice "audio/voice/c/07/1_11_最後に見た.mp3"    
            narrator_arrow "最後に見たのは、石像の目に宿る冷酷な光。\n"
            voice "audio/voice/c/07/1_12_その瞬間、.mp3"
            extend "その瞬間、あなたの意識は闇に飲み込まれ、体は完全に石と化してしまった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart()

        "２．石像の周囲を詳しく調べてみる。":
            stop voice
            jump sage_ghost_appearance

        "３．すぐにその場を離れて逃げ出す。":
            stop voice
            scene dark_corridor_6 at fullscreen_bg
            play music "audio/se/風が吹く1.mp3"
            with fade
            voice "audio/voice/c/07/2_0_不気味な気.mp3"
            narrator_arrow "不気味な気配を感じ取ったあなたは、すぐにその場を離れたくなった。\n"
            voice "audio/voice/c/07/2_1_階段を降り.mp3"
            extend "階段を降りるために一歩踏み出すと、背後から冷たい風が吹き付けた。\n"
            voice "audio/voice/c/07/2_2_まるで何か.mp3"
            extend "まるで何かがあなたを逃がさないようにしているかのようだ。\n"
            voice "audio/voice/c/07/2_3_焦りと恐怖.mp3"
            $ ctc_mode = "page"
            extend "焦りと恐怖で胸が高鳴るが、あなたはそれを振り払い、なんとか階段までたどり着いた。\n"

            show black at fullscreen_bg with {"master": dissolve}
            play music "audio/se/地響き.mp3"
            voice "audio/voice/c/07/2_4_しかし、階.mp3"
            narrator_arrow "しかし、階段を降り始めると、突然足元がぐらつき、石の階段が崩れ落ち始めた。\n"
            voice "audio/voice/c/07/2_5_勢いをつけ.mp3"
            extend "勢いをつけて崩れる階段に引きずられるようにして転落してしまう。\n"
            voice "audio/voice/c/07/2_6_暗闇の中で.mp3"
            extend "暗闇の中で果てしなく続く落下。\n"
            voice "audio/voice/c/07/2_7_恐怖に凍り.mp3"
            $ ctc_mode = "page"
            extend "恐怖に凍りついたあなたは、何度も石に体を打ち付け、最後には全身が激痛に包まれ、意識が遠のいていく。\n"
            
            stop music fadeout 1.5
            play sound "audio/se/怖い系リプレイ音.mp3"            
            scene solitary_cell at fullscreen_bg
            voice "audio/voice/c/07/2_9_目を覚ます.mp3"
            narrator_arrow "目を覚ますと、そこは冷たく湿ったあの地下の牢獄だった。\n"
            voice "audio/voice/c/07/2_10_視界の隅に.mp3"
            extend "視界の隅に、あなたを見下ろす不気味な影が映る。\n"
            voice "audio/voice/c/07/2_11_その影は、.mp3"
            extend "その影は、低い声でささやく。\n"
            voice "audio/voice/c/07/2_12_「逃げる者.mp3"
            extend "「逃げる者に未来はない…お前はここで永遠に囚われるのだ。」\n"
            voice "audio/voice/c/07/2_13_あなたの運.mp3"
            extend "あなたの運命は完全に閉ざされた。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart()


    $ choice_comment = ""  

label sage_ghost_appearance:

    window hide
    play music "audio/bgm/透明な亡霊.mp3"
    scene ghostly_sage_appearance at fullscreen_bg
    with fade
    voice "audio/voice/c/07/3_0_石像を詳し.mp3"
    narrator_arrow "石像を詳しく調べたあなたの前に、かつてこの地を守った賢者の亡霊が現れた。\n"
    voice "audio/voice/c/07/3_1_彼の姿は穏.mp3"
    $ ctc_mode = "page"
    extend "彼の姿は穏やかで、あなたに向けて導くような声で語りかける。\n"

    voice "audio/voice/c/07/3_2_「君は真実.mp3"
    narrator_arrow "「君は真実を求め、慎重に歩を進めてきた。"
    voice "audio/voice/c/07/3_3_そのおかげ.mp3"
    extend "そのおかげで、私の魂は君に助言を与えることができるようになった。"
    voice "audio/voice/c/07/3_4_私が封じ込.mp3"
    extend "私が封じ込められたこの塔は今、恐るべき魔人が支配している。"
    voice "audio/voice/c/07/3_5_その魔人を.mp3"
    extend "その魔人を倒すには、ただの力では足りない。"
    voice "audio/voice/c/07/3_6_その昔、魔.mp3"
    $ ctc_mode = "page"
    extend "その昔、魔力を持つ者として私は、勇者と協力することで魔人達を倒してきた。」\n"

    scene sword_c at fullscreen_bg
    with fade
    voice "audio/voice/c/07/3_7_賢者は、石.mp3"
    narrator_arrow "賢者は、石像の手にある剣を指し示しながら続けた。\n"
    voice "audio/voice/c/07/3_8_「この勇者.mp3"
    extend "「この勇者の剣ならば魔人を倒せるだろう。"
    voice "audio/voice/c/07/3_9_魔人の弱点.mp3"
    extend "魔人の弱点はその心臓にある結晶だが、武力だけでは破壊できない。"
    voice "audio/voice/c/07/3_11_魔力を持つ.mp3"
    $ ctc_mode = "page"
    extend "魔力を持つ者に勇者の魔法の言葉を唱えさせ、その力を借りて初めて、その結晶は脆くなる。」\n"

    scene ghostly_sage_appearance at fullscreen_bg
    with fade
    voice "audio/voice/c/07/3_12_亡霊の賢者.mp3"
    narrator_arrow "亡霊の賢者は、さらに重要なことを語り始めた。\n"
    voice "audio/voice/c/07/3_13_「塔の最上.mp3"
    extend "「塔の最上階には、どうやら魔力を持つ者がいるようだ。"
    voice "audio/voice/c/07/3_13_その者に勇.mp3"
    extend "その者に勇者の魔法を伝えなさい。"
    voice "audio/voice/c/07/3_15_その言葉は.mp3"
    extend "その言葉は、勇者の魂を宿し、結晶の防御を破壊する。"
    voice "audio/voice/c/07/3_16_その瞬間に.mp3"
    $ ctc_mode = "page"
    extend "その瞬間に、この剣で魔人の結晶を突き、魔人を倒すのです。」\n"

    scene sword_c at fullscreen_bg
    with fade
    voice "audio/voice/c/07/3_17_賢者の亡霊.mp3"
    narrator_arrow "賢者の亡霊は、石像の手から剣を取り出すよう促すと、静かに姿を消した。\n"
    voice "audio/voice/c/07/3_18_あなたはそ.mp3"
    $ ctc_mode = "page"
    extend "あなたはその剣を手にし、塔の最上階へと向かう決意を固めた。\n"

    jump CH_C_08_monster_bird
