# game/ui_transforms.rpy
# CTC（文末アイコン）用の演出定義
# transform と「ctcに渡すdisplayable」をここにまとめる

init -1:

    # 点滅（透明度を往復）
    transform blink:
        alpha 1.0
        linear 0.6 alpha 0.15
        linear 0.6 alpha 1.0
        repeat

# ここは「init python」で “表示物” を組み立てるのが安全
init -1 python:
    # Transformでサイズ調整 → Atで点滅transformを適用
    # ※ zoom はまず 0.18〜0.35 あたりがサウンドノベルの文末に収まりやすいです
    ctc_arrow_blink = At(Transform("ui/arrow.png", zoom=0.1), blink)
    ctc_page_blink  = At(Transform("ui/page_turn.png", zoom=0.1), blink)

