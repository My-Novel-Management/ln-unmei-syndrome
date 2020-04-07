# -*- coding: utf-8 -*-
"""Chapter 10: 三月「運命の人症候群」
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
def ch_destiny(w: World):
    return w.chapter("１０．三月「運命の人症候群」",
            ep_tmp(w),
            note="西野なおは全てのことの顛末をレポートにまとめていた。心臓移植をしたことで姉の記憶や嗜好を受け継いだ。姉の日記を読み返す")
