# -*- coding: utf-8 -*-
"""Chapter 5: 十月「窓際で人を待つと遅刻しない喫茶店」
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()

## scenes
def sc_tmp(w: World):
    return w.scene("Sc: xxx",
            camera=w.taro,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_tmp(w: World):
    return w.episode("Ep: xxx",
            sc_tmp(w),
            )

## chapter
def ch_waitingcafe(w: World):
    return w.chapter("５．十月「窓際で人を待つと遅刻しない喫茶店」",
            ep_tmp(w),
            note="知らない女性から「姉の美津希のことが好きだったの」と告白される")
