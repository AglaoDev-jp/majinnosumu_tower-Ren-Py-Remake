# CH_B_07_treasure_room.rpy

label CH_B_07_treasure_room:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"

    scene treasure_room at fullscreen_bg
    with fade

    voice "audio/voice/b/07/0_12_次のフロア.mp3"
    narrator_arrow "次のフロアは、宝物庫のようだ。\n"
    voice "audio/voice/b/07/0_13_部屋の中に.mp3"
    extend "部屋の中には金銀財宝が散らばり、まるで昔話に出てくるような財宝の山が広がっている。\n"
    voice "audio/voice/b/07/0_14_部屋の中央.mp3"
    extend "部屋の中央には大きな台座があり、そこには古代の工芸品が展示されている。\n"
    voice "audio/voice/b/07/0_15_目立つ宝箱.mp3"
    extend "目立つ宝箱が部屋の中央に置かれており、煌びやかな装飾が施されている。\n"
    voice "audio/voice/b/07/0_16_その隣には.mp3"
    $ ctc_mode = "page"
    extend "その隣には一見目立たない隅の小箱があり、他の財宝に埋もれるように置かれている。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/b/07/3_0_宝物庫を注.mp3"
    $ choice_comment = "宝物庫を注意深く見渡し、ワナを避けるのだ。"
    menu:

        "１．目立つ宝箱を開ける。豪華な装飾が施されているが、ワナかもしれない。":
            stop music
            play sound "audio/se/雷魔法4.mp3"
            scene treasure_chest_explosion at fullscreen_bg
            voice "audio/voice/b/07/0_0_宝箱が爆発.mp3"
            narrator_arrow "宝箱が爆発した！ワナだったようだ。\n"
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            voice "audio/voice/b/07/0_1_あなたは、.mp3"
            extend "あなたは、爆風で吹き飛ばされてしまった！\n"
            voice "audio/voice/ゲームオーバー.mp3"
            scene skeleton_bad at fullscreen_bg
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()            

        "２．隅の小箱を調べる。目立たないが、何かが隠されているかもしれない。":
            stop music
            play sound "audio/se/発見.mp3"
            scene hashigo at fullscreen_bg
            voice "audio/voice/b/07/0_0_隅の小箱を.mp3"
            narrator_arrow "隅の小箱を調べると、中に折りたたまれたはしごを見つけた。\n"
            voice "audio/voice/b/07/0_1_伸ばすこと.mp3"
            extend "伸ばすことで上側の通路に届くようだ。\n"
            voice "audio/voice/b/07/0_2_次のフロア.mp3"
            $ ctc_mode = "page"
            extend "次のフロアに進もう。\n"
            scene black
            with Dissolve(1.0)
            jump CH_B_08_Majin_room

        "３．中央の台座を探る。工芸品が展示されているが、ワナが仕掛けられている可能性がある。":

            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene pedestal_collapsing at fullscreen_bg
            voice "audio/voice/b/07/0_0_台座が崩れ.mp3"
            narrator_arrow "台座が崩れ、ワナが発動してしまった。\n"
            voice "audio/voice/b/07/1_1_あなたは、.mp3"
            extend "あなたは、奈落の底へと落ちていく。\n"
            scene black
            with fade
            scene solitary_cell at fullscreen_bg
            voice "audio/voice/b/07/0_2_気づくと、.mp3"
            extend "気づくと、そこはあの独房だった。\n"

            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()

    $ choice_comment = ""  