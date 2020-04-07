# -*- coding: utf-8 -*-
"""Chapter 4: 九月「お弁当を持って行かないと雨が降る公園」
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
def ch_rainpark(w: World):
    return w.chapter("４．九月「お弁当を持って行かないと雨が降る公園」",
            ep_tmp(w),
            note="先生から「好きだよ」と告白された")
