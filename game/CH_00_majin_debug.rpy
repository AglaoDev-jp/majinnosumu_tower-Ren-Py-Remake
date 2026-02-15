# CH_00_majin_debug.rpy

# デバックモードのオンオフは、"CH_01_start_point.rpy"にあります。

label CH_00_majin_debug:
    $ choice_comment = "よく来たな。ここはデバックモードモードだ。さあ、好きなところへ飛ばしてやろう……。"
    menu:
        "CH_01_オープニング（最初から）":
            return
        "CH_02_監視所":
            jump CH_02_cell_block
        "CH_03_分かれ道":
            jump CH_03_path_branch
        "CH_A_04_ホール":
            jump CH_A_04_hall
        "シナリオA　魔人の門シナリオ":
            jump CH_00_a
        "シナリオB　王女アリアーナシナリオ":
            jump CH_00_b
        "シナリオC　怪鳥シナリオ":
            jump CH_00_c
        "タイトルへ":
            $ renpy.full_restart()

    $ choice_comment = ""  

label CH_00_a:
    $ choice_comment = "魔人の門シナリオ"
    menu:
        "CH_A_05 武器庫":
            jump CH_A_05_armory
        "CH_A_06_戦士の霊たち":
            jump CH_A_06_Tomb_of_the_Warriors
        "CH_A_06_bad_戦士の霊たち_1":
            jump CH_A_06_bad_Tomb_of_the_Warriors_1
        "CH_A_06_bad_戦士の霊たち_2":
            jump CH_A_06_bad_Tomb_of_the_Warriors_2
        "CH_A_06_good_戦士の霊たち":
            jump CH_A_06_good_Tomb_of_the_Warriors
        "CH_A_07_魔人の門":
            jump CH_A_07_Majin_Gate
        "CH_A_07_魔人の門END":
            jump CH_A_07_Majin_Gate_end
        "ひとつ前にもどる":
            jump CH_00_majin_debug

    $ choice_comment = ""  

label CH_00_b:
    $ choice_comment = "王女アリアーナシナリオ"
    menu:
        "CH_B_04 薬の部屋":
            jump CH_B_04_potion_room
        "CH_B_05_室内庭園":
            jump CH_B_05_garden
        "CH_B_06 鏡の部屋":
            jump CH_B_06_mirror_room
        "CH_B_07_宝の部屋":
            jump CH_B_07_treasure_room
        "CH_B_08_魔人の部屋":
            jump CH_B_08_Majin_room
        "CH_B_09 魔人と対面":
            jump CH_B_09_Confronting_the_devil
        "CH_B_Good_END1":
            jump CH_B_09_Confronting_the_devil_GOOD_1
        "CH_B_Good_END2":
            jump CH_B_09_Confronting_the_devil_GOOD_2
        "CH_B_エンディング":
            jump CH_B_09_GOOD_END
        "ひとつ前にもどる":
            jump CH_00_majin_debug

    $ choice_comment = ""  

label CH_00_c:
    $ choice_comment = "怪鳥シナリオ"
    menu:
        "CH_C_05_隠し図書館":
            jump CH_C_05_hidden_library
        "CH_C_06_暗闇回廊":
            jump CH_C_06_dark_corridor
        "CH_C_07_勇者の石像":
            jump CH_C_07_Heros_Statue
        "CH_C_07_怪鳥":
            jump CH_C_08_monster_bird
        "CH_C_07_怪鳥bad_end":
            jump CH_C_08_monster_bird_bad_end
        "CH_C_07_怪鳥_good_end":
            jump CH_C_08_monster_bird_good_end
        "ひとつ前にもどる":
            jump CH_00_majin_debug

    $ choice_comment = ""  