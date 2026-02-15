# game/00_transforms.rpy

init -2:

    # --------------------------------------------------------
    # 背景をフルスクリーンで表示する transform
    # --------------------------------------------------------
    transform fullscreen_bg:
        xysize (config.screen_width, config.screen_height)