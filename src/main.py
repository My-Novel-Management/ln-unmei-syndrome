# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## assets
from storybuilder.assets import basic, accessory
## local files
from src.chapter.main import ch_tmp

## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   ４月　『神様の悪戯という名の雨　changed Heart』
#   ７月　『時々２杯分入る自販機　warm Liver』
#   ８月　『好きから始めると必ず好きになる花　Stomachache』
#   ９月　『お弁当を持っていかないと雨が降る公園　pang Duodenum』
#   １０月『窓際で人を待つと遅刻しない喫茶店　fried Kidney』
#   １１月『手を繋いで入ると嬉しいことがある水族館　tangle Intestine』
#   １２月『遅刻したら別れる遊園地　abnormal Marrow』
#   １月　『真夜中に見てはいけない鏡　squeezed Lunges』
#   ２月　『赤い糸　gazing at Eyes』
#   ３月　『運命の人症候群　illusion of Brain』
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("運命の人症候群")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2020)
    w.setBaseArea("Tokyo")
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("心臓移植を受けた真穂は移植後、運命を感じる男性と出会った。その医者の彼と、新しい恋が始まる。けれどその恋は運命の悪戯を彼女に仕掛けるのだった")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_tmp(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

