# CH_02_cell_block.rpy

label CH_02_cell_block:

    window hide
    play music "audio/bgm/strange_lullaby.mp3"
    scene black

    voice "audio/voice/s/02/0_0_塔の独房か.mp3"
    narrator_arrow "塔の独房から脱出したたあなたは、暗く湿った石の廊下を進み、ある部屋に辿り着いた。\n"
    voice "audio/voice/s/02/0_1_部屋の中に.mp3"
    $ ctc_mode = "page"
    extend "部屋の中に足を踏み入れると、薄暗い光がわずかに差し込む中で、家具や物品が見えてくる。\n"

    scene cell_block at fullscreen_bg
    with fade
    voice "audio/voice/s/02/0_2_まず目に入.mp3"
    narrator_arrow "まず目に入ったのは、部屋の中央に置かれた古い木製の机だった。\n"
    voice "audio/voice/s/02/0_3_机の表面は.mp3"
    extend "机の表面は傷だらけで、所々にインクの染みが見える。\n"
    voice "audio/voice/s/02/0_4_机の上には.mp3"
    extend "机の上には乱雑に置かれた書類の山と、所々錆びた鍵の束が無造作に置かれている。\n"
    voice "audio/voice/s/02/0_5_この部屋は.mp3"
    $ ctc_mode = "page"
    extend "この部屋は、独房の監視に使われていたのではないかと推測される。\n"

    voice "audio/voice/s/02/0_6_その隣には.mp3"
    narrator_arrow "その隣には、大きなチェストが鎮座している。\n"
    voice "audio/voice/s/02/0_7_厚い木材で.mp3"
    extend "厚い木材で作られたチェストは重厚で、表面には古い装飾が施されている。\n"
    voice "audio/voice/s/02/0_8_鍵穴の部分.mp3"
    extend "鍵穴の部分には小さな錠前が付いており、中に何かが隠されている可能性を示唆している。\n"
    voice "audio/voice/s/02/0_9_チェストの.mp3"
    extend "チェストの存在感から、単なる物置きではないことを感じさせる。\n"

    voice "audio/voice/s/02/0_10_部屋の奥に.mp3"    
    extend "部屋の奥には重厚な木製の扉がある。\n"
    voice "audio/voice/s/02/0_11_扉は古びた.mp3"
    extend "扉は古びた鉄の蝶番で支えられ、無数の傷跡がついている。\n"
    voice "audio/voice/s/02/0_12_誰かが強引.mp3"
    extend "誰かが強引にこじ開けようとした形跡がある。\n"
    voice "audio/voice/s/02/0_13_しかしそれ.mp3"
    $ ctc_mode = "page"
    extend "しかしそれでも扉は頑丈で、簡単に開きそうにない。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/s/02/0_14_さて、どう.mp3"
    $ choice_comment = "さて、どうやって脱出しようか？"
    menu:

        "１．チェストを調べてみる。何か役立つものや脱出の手がかりが見つかるかもしれない。":
            play music "audio/bgm/strange_lullaby.mp3"
            scene cell_block at fullscreen_bg
            voice "audio/voice/s/02/1_0_あなたは大.mp3"
            narrator_arrow "あなたは大きなチェストの前に立ち、その錠前に手をかける。\n"
            voice "audio/voice/s/02/1_1_錆びた鍵穴.mp3"
            $ ctc_mode = "page"
            extend "錆びた鍵穴に合う鍵を見つけ、ゆっくりと回して蓋を開ける。\n"

            stop music
            play sound "audio/se/ライオンの鳴き声1.mp3"
            scene cell_block_monster_1 at fullscreen_bg
            voice "audio/voice/s/02/1_2_すると突然.mp3"
            $ ctc_mode = "page"
            narrator_arrow "すると突然、中から怪物が飛び出してきた！\n"

            play sound "audio/se/怖い系リプレイ音.mp3"
            voice "audio/voice/s/02/1_3_驚きのあま.mp3"
            narrator_arrow "驚きのあまり後ずさる間もなく、怪物はあなたに襲いかかる。\n"
            voice "audio/voice/s/02/1_4_鋭い爪があ.mp3"
            extend "鋭い爪があなたの腕を掴み、力強い一撃があなたを地面に叩きつけた。\n"
            voice "audio/voice/s/02/1_5_あなたは抵.mp3"
            $ ctc_mode = "page"
            extend "あなたは抵抗する間もなく、怪物の牙が迫り、視界が暗転する。\n"

            scene black
            with fade
            voice "audio/voice/s/02/1_6_倒れたあな.mp3"
            narrator_arrow "倒れたあなたの目の端には、チェストの横に倒れ込んでいる看守が見える。\n"
            voice "audio/voice/s/02/1_7_どうやら看.mp3"
            extend "どうやら看守も、この怪物の犠牲となったようだ。\n"
            voice "audio/voice/s/02/1_8_あなたの視.mp3"
            extend "あなたの視界は次第に暗くなり、静寂が訪れる。\n"
            voice "audio/voice/s/02/1_9_どうやら脱.mp3"
            extend "どうやら脱出の望みは、ここで断たれるようだ。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()
            
        "２．鍵束の中から正しい鍵を探す。時間はかかるが、ひとつづつ試してみることにする。":
            play music "audio/bgm/strange_lullaby.mp3"
            scene lots_of_keys at fullscreen_bg
            voice "audio/voice/s/02/2_0_あなたは机.mp3"
            narrator_arrow "あなたは机の上の、錆びついた鍵束を手に取った。\n"
            voice "audio/voice/s/02/2_1_なんほんも.mp3"
            extend "何本も絡まった鍵を一つずつ試していくが、どれもドアの鍵には合わない。\n"
            voice "audio/voice/s/02/2_2_焦りが募る.mp3"
            $ ctc_mode = "page"
            extend "焦りが募る中、最後の鍵を試そうとしたその時、突然、机の下から低い唸り声が響いた。\n"

            stop music
            play sound "audio/se/ライオンの鳴き声1.mp3"
            scene cell_block_monster_2 at fullscreen_bg
            voice "audio/voice/s/02/2_3_次の瞬間、.mp3"
            narrator_arrow "次の瞬間、机の下から巨大な怪物が飛び出してきた。\n"
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            voice "audio/voice/s/02/2_4_暗闇の中で.mp3"
            extend "暗闇の中で見え隠れする鋭い牙と爪が、あなたに襲いかかる。\n"
            voice "audio/voice/s/02/2_5_恐怖に凍り.mp3"
            $ ctc_mode = "page"
            extend "恐怖に凍りついたあなたは身動きが取れず、怪物の凶暴な一撃を受けて倒れ込む。\n"

            scene black
            with fade
            voice "audio/voice/s/02/1_6_倒れたあな.mp3"
            narrator_arrow "倒れたあなたの目の端には、チェストの横に倒れ込んでいる看守が見える。\n"
            voice "audio/voice/s/02/1_7_どうやら看.mp3"
            extend "どうやら看守も、この怪物の犠牲となったようだ。\n"
            voice "audio/voice/s/02/1_8_あなたの視.mp3"
            extend "あなたの視界は次第に暗くなり、静寂が訪れる。\n"
            voice "audio/voice/s/02/1_9_どうやら脱.mp3"
            extend "どうやら脱出の望みは、ここで断たれるようだ。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page"
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)
            $ renpy.full_restart()

        "３．あたりをよく観察する。一度立ち止まり、見回してみることにする。":

            jump CH_03_path_branch

    $ choice_comment = "" 


