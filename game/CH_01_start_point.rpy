# CH_01_start_point.rpy

# デバックモード（公開版は False にしてください。）
default DEBUG_MODE = True

# screens.rpy の"メインメニュースクリーンとゲームメニュースクリーン"に
# "【デバッグ】クリア初期化"項目があるので、公開版は削除 or コメントアウト

# -------- Ren’Py 初期テンプレートからの変更点 -------------
# screens.rpy の　screen say(who, what):変更　window hide / show に連動させる分岐の追加
# screens.rpy オープニング画面の設定の変更。詳しくはdocsフォルダを参照
# text what:の変更（文字を大きく、文字の表示位置の変更、文字の縁取り）
# options.rpy の　default preferences.text_cps　を 0から30へ変更（タイピングエフェクト）
# CH_00_transforms.rpyの追加：背景をフルスクリーンにぴったり表示する transform を設置
# CH_00_menu_transformの追加：選択肢の時間差フェードイン、コメント表示など
# CH_00_majin_debug.rpy（デバックモード）の追加
# CH_E_99_end_credits.rpy エンドロール（スタッフロール、エンドクレジット）の作成

# CH_S_system_flags.rpy 作成 クリアフラグなど。
# gui.rpy の define gui.idle_color の色を変更。メニュー文字などUI系文字にアウトライン追加。
# ※ 詳しくはdocsフォルダ'オープニング画面変更点（魔人の棲む塔）.md'を参照
# "gui.rpy" の "フォントとフォントサイズ" 項目　フォントをすべて "fonts/NotoSansJP-Regular.ttf" に変更。

# CH_00_ui_transforms.rpyの作成。 CTC（文末アイコン）用の演出定義

# options.rpy ビルド設定 にてアセット関連のアーカイブ化 配布物から .rpy（ソース）を除外して、.rpyc のみ残す
# options.rpy アイコンの変更
# docsフォルダの追加

# (修正)ヒストリーの表示を修正 screens.rpy の screen history()　style history_name: style history_text:のあたり

# -----------------------------------------------
# v2 追加要素
# CH_00_effects.rpy の追加（山奥ペンションの殺意からそのまま流用）
# Bを押すことでシェード機能（CH_00_effects.rpy）screens.rpy のヘルプに項目追加
# CH_00_ui_transforms.rpy　の改良。ページ送り、ページめくりアイコンに対応（山奥ペンションの殺意からそのまま流用）
# -----------------------------------------------


label start:
    # デバック用分岐 （デバックモードが False なら無視）
    if DEBUG_MODE:
        call CH_00_majin_debug from _call_CH_00_majin_debug
    jump CH_01_start_point # 本編スタート

label CH_01_start_point:

    # テキストウインドウを完全に非表示にする。（これがないとウインドウが出てしまうので毎回入れてください。）
    window hide

    play music "audio/bgm/strange_lullaby.mp3"
    scene black
    voice "audio/voice/s/01/0_0_あなたは、.mp3"
    # narrator_arrow（キャラクター）を先頭に置くことで設定した専用アイコンの点滅。
    narrator_arrow "あなたは、意識を取り戻した。\n" 
    voice "audio/voice/s/01/0_1_あなたは目.mp3"
    extend "あなたは目隠しをされ、堅い椅子にロープでしっかりと縛られている。\n"
    voice "audio/voice/s/01/0_2_あなたの村.mp3"
    extend "あなたの村は魔人に襲われ、どうやらここに幽閉されていたようだ。\n"
    voice "audio/voice/s/01/0_3_ロープは手.mp3"
    extend "ロープは手首と足首に巻かれているが、手首のロープが少し緩んでいることに気づいた。\n"
    voice "audio/voice/s/01//0_4_あなたは慎.mp3"
    extend "あなたは慎重に手首のロープを動かし、何度か試みた後、手首が自由になった。\n"
    voice "audio/voice/s/01/0_5_自由になっ.mp3"
    extend "自由になったあなたは、まず目隠しを外した。\n"
    voice "audio/voice/s/01/0_6_目の前には.mp3"
    # 面倒ですが最後の行に逐一これを置いてください
    # これを置くと矢印アイコンがページめくりのアイコンになります。
    # CH_00_ui_transforms.rpy
    $ ctc_mode = "page" 
    extend "目の前には薄暗い地下室が広がっていた。\n"

    scene solitary_cell at fullscreen_bg
    with fade

    voice "audio/voice/s/01/0_7_独房のよう.mp3"
    narrator_arrow "独房のようだ。\n"
    voice "audio/voice/s/01/0_8_壁には古び.mp3"
    extend "壁には古びたレンガが積み重なり、湿気が漂っている。\n"
    voice "audio/voice/s/01/0_9_あなたは周.mp3"
    $ ctc_mode = "page" 
    extend "あなたは周囲を見回し、脱出の手がかりを探し始めた。\n"

    show cell_door at fullscreen_bg
    with fade
    voice "audio/voice/s/01/0_10_あなたは重.mp3"    
    narrator_arrow "あなたは重い鉄の扉を見つけた。\n"
    voice "audio/voice/s/01/0_11_扉には鍵が.mp3"
    $ ctc_mode = "page" 
    extend "扉には鍵がかかっているが、鍵穴は古びており、簡単に壊せそうだった。\n"

    play music "audio/bgm/奇妙な話.mp3"
    voice "audio/voice/s/01/0_12_さて、どう.mp3"

    $ choice_comment = "さて、どうしようか？" # 選択肢コメント

    menu:

        "１．鍵を引っ張る。こんな古びた鍵ならすぐに取れてしまうだろう。":
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene black
            voice "audio/voice/s/01/1_0_鍵が取れた.mp3"
            narrator_arrow "鍵が取れた拍子に床に頭を強く打ってしまった。\n"
            voice "audio/voice/s/01/1_1_あなたは、.mp3"
            extend "あなたは、そのまま目覚めることはなかった。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page" 
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart() # renpy.full_restart() は ゲームを最初から再起動します。

        "２．穴に異物を突っ込む。鍵穴に何かを突っ込めば、簡単に壊せるだろう。":
            stop music
            play sound "audio/se/怖い系リプレイ音.mp3"
            scene black
            voice "audio/voice/s/01/2_0_異物を詰ま.mp3"
            narrator_arrow "異物を詰まらせて取れなくなってしまった！\n"
            voice "audio/voice/s/01/2_1_あなたは、.mp3"
            extend "あなたは、牢屋で息絶えた。\n"
            scene skeleton_bad at fullscreen_bg
            voice "audio/voice/ゲームオーバー.mp3"
            $ ctc_mode = "page" 
            extend "ゲームオーバー。\n"
            scene black
            with Dissolve(1.0)

            $ renpy.full_restart()

        "３．鍵を蹴る。簡単に壊せそうだ、蹴って鍵ごと壊してしまおう。":
            stop music
            play sound "audio/se/発見.mp3"
            scene cell_door_unlocked at fullscreen_bg
            voice "audio/voice/s/01/3_0_鍵は古びて.mp3"
            narrator_arrow "鍵は古びており、簡単に壊すことができた。\n"
            voice "audio/voice/s/01/3_1_あなたは、.mp3"
            extend "あなたは、重い扉を押し開けた。\n"
            voice "audio/voice/s/01/3_2_扉の向こう.mp3"
            $ ctc_mode = "page" 
            extend "扉の向こうには、階段が続いていた。\n"
            scene black
            with Dissolve(1.0)

            jump CH_02_cell_block

    $ choice_comment = ""  # コメント内を空にする。コメント使った場合、次に残らないように必ずこれを置いてください。

# renpy.full_restart() は ゲームを最初から再起動します。
# return だと「呼び出し元に戻る」なので、構造によってはタイトルに戻らないことがあります。
# 確実にタイトルへ戻すなら`renpy.full_restart() `が鉄板らしいです。

# ---------------------
# メモ
# Ren’Py は Case Sensitive（大小文字を区別） です。
# 画像名に大文字は使えないようです。
# label は、先頭に数字が使えないようです。
# ファイル名は構造的に無視されます。'jump' で、'game/'内の.rpyファイルすべての'label' を参照するそうです。すごいよね。
# ---------------------