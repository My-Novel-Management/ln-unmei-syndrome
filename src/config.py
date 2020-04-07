# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) AREAS
#       エリア設定
# 3) STAGES
#       舞台基本設定
# 4) DAYS
#       年月日設定
# 5) TIMES
#       時間帯基本設定
# 6) ITEMS
#       小道具設定
# 7) WORDS
#       辞書設定
# 8) RUBIS
#       ルビ設定
# 9) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("maho", "真穂", "皆本,真穂", 30,(1,1), "female", "無職", "me:私"),
        ("yoshi", "善人", "堺田,善人", 40,(1,1), "male", "医師", "me:僕"),
        ("nao", "奈央", "西野,奈央", 35,(1,1), "female", "移植コーディネーター", "me:私"),
        ("mitsu", "美津希", "西野,美津希", 40,(1,1), "female", "故人"),
        ## Family
        ("kosuke", "浩輔", "皆本,浩輔", 60,(1,1), "male", "父"),
        ("harue", "春枝", "皆本,春枝", 60,(1,1), "female", "母"),
        ## Doc
        ("taka", "高正", "高正,誠司", 45,(1,1), "male", "医師"),
        ("sanada", "真田", "", 40,(1,1), "male", "外科医"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        )

STAGES = (
        # Tag / 名前 / Area / 紹介
        ("sickroom", "病室"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("transplant", "移植手術日", 4,20,2018),
        ("current", "current", 1,1,2020),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Exclusion / Type
        )

LAYERS = (
        # Key / Title / Words
        )

