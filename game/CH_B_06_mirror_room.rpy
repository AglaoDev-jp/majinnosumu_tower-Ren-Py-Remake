# CH_B_06_mirror_room.rpy

label CH_B_06_mirror_room:

    window hide
    play music "audio/bgm/静かな夜に.mp3"

    scene mirror_room at fullscreen_bg
    with fade
    voice "audio/voice/b/06/0_2_部屋全体が.mp3"
    narrator_arrow "部屋全体が神秘的な光に包まれていることに気づく。\n"
    voice "audio/voice/b/06/0_3_部屋の中に.mp3"
    extend "部屋の中には巨大な鏡がいくつも設置され、それぞれが幻想的な風景を映し出している。\n"
    voice "audio/voice/b/06/0_4_部屋の中央.mp3"
    extend "部屋の中央には三つの特別大きな鏡が並んでおり、それぞれが異なる人物を映し出している。\n"

    scene mirror_three_figures at fullscreen_bg
    with fade
    voice "audio/voice/b/06/0_5_左の鏡には.mp3"
    narrator_arrow "左の鏡には優雅なドレスをまとった貴婦人、\n"
    voice "audio/voice/b/06/0_6_中央の鏡に.mp3"
    extend "中央の鏡には壮麗な甲冑を身に着けた騎士、\n"
    voice "audio/voice/b/06/0_7_右の鏡には.mp3"
    extend "右の鏡には怪しいローブを纏った魔法使いが映っている。\n"

    voice "audio/voice/b/06/0_0_出口のよう.mp3"
    narrator_arrow "出口のようなものは見当たらない。\n"
    voice "audio/voice/b/06/0_1_この3つの.mp3"
    extend "この3つの鏡になにか仕掛けがあるのだろうか。"

    voice "audio/voice/b/06/0_2_さて、どう.mp3"
    $ choice_comment = "さて、どうしようか？"
    menu:

        "１．左の鏡に触れる。美しい貴婦人だが、あなたをだますワナかもしれない。": # 標準フォントだと"罠"が文字化けする。
            stop music
            stop voice
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene false_paradise at fullscreen_bg
            voice "audio/voice/b/06/0_0_鏡に触れる.mp3"
            "鏡に触れると、鏡に吸い込まれ、帰れなくなった。\n"
            voice "audio/voice/b/06/0_1_あなたは、.mp3"
            extend "あなたは、偽りの楽園で永遠に過ごすことになるだろう。\n"

            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()
            
        "２．中央の鏡に触れる。勇敢そうな騎士だが、あなたを敵とみなすかもしれない。":
            scene black            
            stop music
            stop voice
            play sound "audio/se/発見.mp3"

            voice "audio/voice/b/06/0_0_鏡に手を伸.mp3"
            "鏡に手を伸ばしたその瞬間、映り込んでいた騎士の姿がまるで命を宿したかのように動き出した。\n"

            play music "audio/bgm/透明な亡霊.mp3"
            scene hero_face at fullscreen_bg
            with fade
            voice "audio/voice/b/06/0_1_彼は深い瞳.mp3"
            "彼は深い瞳であなたを見つめ、静かに語りかける。\n"
            voice "audio/voice/b/06/4_0_この剣を持.mp3"
            extend "「この剣を持って行け。"
            voice "audio/voice/b/06/4_1_魔人を倒す.mp3"
            extend "魔人を倒すには、この勇者の剣が必要だ。」\n"
            voice "audio/voice/b/06/0_4_騎士の声に.mp3"
            extend "騎士の声には、かつての戦いの傷跡が滲み出ているようだった。\n"
            voice "audio/voice/b/06/0_5_彼は言葉を.mp3"
            extend "彼は言葉を続ける。\n"
            voice "audio/voice/b/06/4_2_私には、も.mp3"
            extend "「私には、もう戦う力は残っていない。"
            voice "audio/voice/b/06/4_3_この剣を託.mp3"
            extend "この剣を託せる力のある者に…」\n"
            voice "audio/voice/b/06/0_8_騎士は最後.mp3"
            extend "騎士は最後の力を振り絞る。"
            stop music
            play sound "audio/se/ガラスが割れる1.mp3"
            scene mirror_breaks at fullscreen_bg
            voice "audio/voice/b/06/0_9_騎士は鏡を.mp3"
            "騎士は鏡を一撃で打ち砕いた。"
            voice "audio/voice/b/06/0_10_鏡は粉々に.mp3"
            "鏡は粉々に砕け散り、割れた鏡の裏から次のフロアへの階段が現れた。"
            scene sword_b at fullscreen_bg
            with fade
            voice "audio/voice/b/06/0_11_あなたは騎.mp3"
            "あなたは騎士から託された剣を手に取り、次のフロアへと向かう。"

            scene black
            with Dissolve(1.0)
            jump CH_B_07_treasure_room

        "３．右の鏡に触れる。いかにも怪しい魔法使いだが、逆に特別な何かがあるかもしれない。":
            stop voice
            stop music
            play sound "audio/se/雷魔法4.mp3"
            scene lightning_magic at fullscreen_bg
            voice "audio/voice/b/06/0_2_鏡に触れる.mp3"
            "鏡に触れると、激しい雷の魔法で倒されてしまった！\n"
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            voice "audio/voice/b/06/0_2_消し炭にな.mp3"
            extend "消し炭になったあなたを、だれも見分けることはできないだろう。\n"

            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            extend "ゲームオーバー。"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()

    $ choice_comment = ""  