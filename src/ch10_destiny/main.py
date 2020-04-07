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
def sc_herreport(w: World):
    maho, nao = W(w.maho), W(w.nao)
    return w.scene("$full_mahoについてのレポート",
            camera=w.nao,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

## episode
def ep_report(w: World):
    return w.episode("10-1．今回のレポートについて",
            sc_herreport(w),
            )

## chapter
def ch_destiny(w: World):
    return w.chapter("１０．三月「運命の人症候群」",
            ep_report(w),
            note="西野なおは全てのことの顛末をレポートにまとめていた。心臓移植をしたことで姉の記憶や嗜好を受け継いだ。姉の日記を読み返す")
