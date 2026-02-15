# CH_C_05_hidden_library

label CH_C_05_hidden_library:

    window hide
    stop music
    play sound "audio/se/発見.mp3"
    scene hidden_library at fullscreen_bg
    with fade
    voice "audio/voice/c/05/0_0_あなたは奥.mp3"
    narrator_arrow "あなたは奥深くまで足を進めると、古びた書庫を見つけた。\n"
    play music "audio/bgm/strange_lullaby.mp3"
    voice "audio/voice/c/05/0_1_扉を静かに.mp3"
    extend "扉を静かに押し開けると、無数の古書や巻物がぎっしりと詰まった棚が現れる。\n"
    voice "audio/voice/c/05/0_2_書庫の中は.mp3"
    extend "書庫の中は、まるで時間が止まったかのような静寂が支配しており、古い紙とインクの独特な匂いが漂っている。\n"
    voice "audio/voice/c/05/0_4_かすかな光.mp3"
    extend "かすかな光が、天井の小さな隙間から差し込み、舞い上がった埃がその光を浴びてきらきらと輝いている。"

    voice "audio/voice/c/05/0_6_この書庫に.mp3"
    narrator_arrow "この書庫には、脱出の手がかりとなる重要な情報が隠されているかもしれない。\n"
    voice "audio/voice/c/05/0_7_だが同時に.mp3"
    extend "だが同時に、この場所には未知の危険が潜んでいるような気配も感じる。\n"
    voice "audio/voice/c/05/0_8_軽.mp3"
    extend "軽はずみに動くことはできない。"

    voice "audio/voice/c/05/0_9_書棚を見渡.mp3"
    narrator_arrow "書棚を見渡していると、突然、背後にひやりとするような異様な気配を感じた。\n"
    voice "audio/voice/c/05/0_10_あなたは直.mp3"
    extend "あなたは直感的に、特定の古書に手を伸ばす。\n"
    voice "audio/voice/c/05/0_11_書物に触れ.mp3"
    extend "書物に触れたその瞬間、書庫全体がわずかに揺れ始めた。\n"
    voice "audio/voice/c/05/0_12_この書庫に.mp3"
    extend "この書庫には、何かが隠されているのは確かだ。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/c/05/0_14_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？" 

    menu:

        "１．手に取った書物を開く。":
            stop voice
            scene dark_magical_book_1 at fullscreen_bg
            with fade
            play music "audio/bgm/strange_lullaby.mp3"
            voice "audio/voice/c/05/1_0_あなたは強.mp3"
            narrator_arrow "あなたは強く引き寄せられるように、その古びた書物を手に取った。\n"
            voice "audio/voice/c/05/1_1_慎重にペー.mp3"
            extend "慎重にページをめくる。\n"
            voice "audio/voice/c/05/1_2_ページには.mp3"
            extend "ページには魔人の弱点に関する古代の文字がびっしりと書かれていた。\n"
            voice "audio/voice/c/05/1_3_それらの文.mp3"
            extend "それらの文字を読み進めることで、あなたは魔人を倒すための貴重な情報を手に入れることができた。\n"

            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            play music "audio/se/風が吹く1.mp3"
            scene dark_magical_book_2 at fullscreen_bg           
            voice "audio/voice/c/05/1_5_しかし、読.mp3"
            narrator_arrow "しかし、読み進めるにつれて、ページから漂う冷たい風が部屋全体に広がり、書庫内の空気が一変する。\n"
            voice "audio/voice/c/05/1_8_気づいたと.mp3"
            extend "気づいたときには、あなたの身体が重くなり、まぶたが重く下がっていく。"
            voice "audio/voice/c/05/1_7_書物から黒.mp3"
            extend "書物から黒い霧が立ち上がり、あなたの周囲に重々しい呪文が響きだした。\n"
            voice "audio/voice/c/05/1_9_必死に抵抗.mp3"
            extend "必死に抵抗しようとするが、呪いの力が強すぎる。\n"
            show black at fullscreen_bg with {"master": dissolve}
            stop music fadeout 2.0
            voice "audio/voice/c/05/1_10_目を閉じた.mp3"
            narrator_arrow "目を閉じた瞬間、深い眠りに引き込まれ、意識は闇の中へと沈んでいった。\n"
            voice "audio/voice/c/05/1_11_この呪いは.mp3"
            extend "この呪いは、魔人に挑む者を永遠の眠りに閉じ込めるものだった。\n"
            voice "audio/voice/c/05/1_12_あなたは魔.mp3"
            extend "あなたは魔人の秘密に迫りすぎたがゆえに、二度と目を覚ますことはなかった。\n" 
                        
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() 

        "２．書庫の中をさらに探索する。":
            stop voice
            scene hidden_library_book_deep at fullscreen_bg
            with fade
            play music "audio/bgm/strange_lullaby.mp3"
            voice "audio/voice/c/05/3_0あなたは、.mp3"
            narrator_arrow "あなたは、慎重に書庫の中を探索することに決めた。\n"
            voice "audio/voice/c/05/3_1_棚と棚の間.mp3"
            extend "棚と棚の間を歩き回り、古びた本の表紙に目を走らせる。\n"
            voice "audio/voice/c/05/3_2_ふと、一つ.mp3"
            extend "ふと、一つの棚の奥深くに他と異なる、きらびやかな装丁の本があることに気付いた。\n"
            voice "audio/voice/c/05/3_3_その本は他.mp3"
            extend "その本は他の古書とは明らかに違う存在感を放っている。"

            scene hidden_library_book at fullscreen_bg
            with fade
            voice "audio/voice/c/05/3_4_あなたは慎.mp3"
            narrator_arrow "あなたは慎重にその本を引き出し、表紙に刻まれた文字を読み取ろうとした。\n"     
            voice "audio/voice/c/05/3_5_そこには、.mp3"
            extend "そこには、「古代の魔法書から学んだ魔人の秘密」と古代の文字で記されていた。\n"      
            voice "audio/voice/c/05/3_6_心臓が高鳴.mp3" 
            extend "心臓が高鳴るのを感じながら、そっとその本を開く。"
            
            voice "audio/voice/c/05/3_7_本の中には.mp3"            
            narrator_arrow "本の中には、魔人を封じるための魔法と、その詠唱の詳細が書かれているようだ。\n"
            stop music
            play sound "audio/se/発見.mp3"
            voice "audio/voice/c/05/3_8_この本は、.mp3"
            extend "この本は、必要だ、持っていくことにしよう。"

            scene black
            with Dissolve(1.0)
            jump CH_C_06_dark_corridor

        "３．書庫を出て、別の場所を調べる。":
            stop voice
            scene black
            with fade
            play music "audio/bgm/strange_lullaby.mp3"
            voice "audio/voice/c/05/2_0_異様な気配.mp3"
            narrator_arrow "異様な気配を感じ取り、ふと書庫の壁に小さな亀裂があるのを見つけた。\n"
            voice "audio/voice/c/05/2_1_亀裂の隙間.mp3"
            extend "亀裂の隙間から光が漏れているのを見て、手を伸ばしてみた。\n"
            stop music
            play sound "audio/se/重力魔法2.mp3"
            scene expression Solid("#ffffff")
            voice "audio/voice/c/05/2_2_亀裂に手を.mp3"
            extend "亀裂に手を差し込むと、突然、壁に刻まれた魔法陣が鋭い光を放ち始めた！\n"
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            voice "audio/voice/c/05/2_3_罠の魔法で.mp3"
            extend "ワナの魔法で全身に強烈な光を浴びたあなたは、そのまま意識を失ってしまった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() 


    $ choice_comment = ""  