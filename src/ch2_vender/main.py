# -*- coding: utf-8 -*-
"""Chapter 2: 七月「時々二杯分入る自販機」
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
def ch_vender(w: World):
    return w.chapter("２．七月「時々二杯分入る自販機」",
            ep_tmp(w),
            note="先生にもう一度会いたいと言われた")
