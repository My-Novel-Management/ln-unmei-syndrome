# -*- coding: utf-8 -*-
"""Chapter 9: 二月「赤い糸」
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
def ch_redthread(w: World):
    return w.chapter("９．二月「赤い糸」",
            ep_tmp(w),
            note="完全に姉にのっとられ、彼との同棲生活が始まる。でも鏡の中で、別の自分が笑っていた。一つの体と、二つの意識。それが互いを奪い合う。そしてナイフを取り出した")
