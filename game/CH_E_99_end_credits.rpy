# CH_99_end_credits.rpy
# エンドロール（スタッフロール）関連
# 変数、定数はバラバラのままにしています。
# ------------------------------------------------------------
# クレジット本文（ここを書き換えるだけでOK）
# ------------------------------------------------------------

define ENDING_CREDITS_TEXT = """
制作

プログラム・シナリオ： 
AglaoDev-jp／ChatGPT（AI）
画像作成：
ChatGPT 画像生成

使用素材（敬称略）

音楽：
フリーBGM DOVA-SYNDROME

【使用楽曲】

【基本BGM】「strange lullaby」 shimtone
【選択肢】「奇妙な話」 Heitaro Ashibe
【霊との遭遇】「透明な亡霊」 Heitaro Ashibe
【正解】「発見」 のる
【鏡の部屋】「静かな夜に」 のる
【不正解】「怖い系リプレイ音」 Causality Sound
【戦闘曲】「ENEMY_ENCOUNTER」 MagaMaga
【Ending】「プレリュード第2番『名前を入力してください』」 秦暁

効果音：
効果音ラボ

音声作成：
CoeFont（コエフォント）
Voiced by https://CoeFont.cloud
Standardプランを使用

【使用音声】
【語り、主人公（あなた）】：ひろゆき
【魔人】：Canel（CV: 森川智之）
【亡霊、怪鳥、勇者】：さのすけ（中低音ボイス）
【アリアーナ王女】：あかね大佐 \*

使用エンジン:
Ren’Py  
Copyright © 2004–2026 Tom Rothamel  
License: MIT License

フォント:
Noto Sans JP
© 2014-2021 Adobe
© 2014 Google LLC
SIL Open Font License 1.1

使用エディター：
Visual Studio Code（VSC）

"""

# ------------------------------------------------------------
# スタッフロール用 transform
# ------------------------------------------------------------

transform staff_roll_scroll(scroll_time=25.0):
    # 画面中央寄せ
    xalign 0.5

    # 「画面の下」から開始して「画面の上」へ流す
    # ypos: 0.0=上 / 1.0=下（画面外は 1.1 や -0.5 など）
    ypos 1.1
    linear scroll_time ypos -3.0 # エンドロールが途中で消える、逆になかなかEND表示が出ない場合はここを調整してください。

# ------------------------------------------------------------
# END表示用：フェードイン
# ------------------------------------------------------------
transform end_block_fade_in(t=0.8):
    alpha 0.0
    linear t alpha 1.0

# ------------------------------------------------------------
# 映画エンド型 スタッフロール screen
# - 背景は「今表示されている scene」をそのまま活かす
# - 必要なら薄い黒ベールだけかける（透過）
# - スクロール終了後に「〜 END 〜」で停止
# - クリックでフェードアウト → Return() で呼び出し元へ
# ------------------------------------------------------------

screen credits_scroll(scroll_time=25.0, fade_time=1.0, music_fade=2.0):

    # modal=True: クリック等をこの画面に集中させる（背後のUIに触れない）
    modal True

    # Solid("#000") をベタで敷くと背景が完全に消えます。
    # 今回は背景を残したいので「半透明の黒ベール」にします。
    add Solid("#0008")  # 8=透明度（薄い黒）。逆に、不要ならこの行ごと消す or コメントアウトでOK

    # スタッフロールが「流れ終わったか」を管理するフラグ
    default roll_done = False

    # 一定時間でロール完了扱いにする
    timer scroll_time action SetScreenVariable("roll_done", True) # この timer ってので時間が管理できるんですって。

    # 1) スクロール中の本文
    if not roll_done:
        text ENDING_CREDITS_TEXT:
            at staff_roll_scroll(scroll_time)
            xalign 0.5
            text_align 0.5
            size 36
            line_spacing 8

    # 2) ロール完了後は「〜 END 〜」で停止（ここで待機）
    else:
        # 表示を少しだけ遅らせる。
        timer 0.01 action NullAction()
        # END表示をフェードインさせるために vbox 全体に transform を適用
        vbox:
            xalign 0.5    # 中心基準
            yalign 0.57   # ← 0.55〜0.60で調整。まず0.57おすすめ
            spacing 12    # 行間

            # ★ここでフェードイン
            at end_block_fade_in(0.8)

            text "〜 END 〜":
                xalign 0.5
                size 54

            text "Presented by ChatGPT（AI）／AglaoDev-jp":
                xalign 0.5
                size 26

            text "Ren’Py Remake v1":
                xalign 0.5
                size 24

            text "© 2024-2026 AglaoDev-jp":
                xalign 0.5
                size 24


            null height 10

            text "（クリックで戻る）":
                xalign 0.5
                size 24

        # クリックされたら：
        # - 画面をフェードアウト
        # - 音楽も残っていればフェードアウト
        # - Return() で呼び出し側へ戻す
        key "mouseup_1" action [
            Stop("music", fadeout=music_fade),
            Hide("credits_scroll"),
            With(Fade(fade_time, 0.0, fade_time)),
            Return(True),
        ]
