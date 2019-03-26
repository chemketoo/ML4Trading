#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 00:54:11 2018

@author: seymagurkan
"""

import LinRegLearner as lrl
import BagLearner as bl
class InsaneLearner(object):
    def __init__(self,verbose = False):
        self.learner = bl.BagLearner(learner = bl.BagLearner, kwargs = { "learner" :lrl.LinRegLearner , "kwargs":{}, "bags":20, "boost":False, "verbose":False }, bags = 20, boost = False, verbose = False)
    def author(self):
        return 'sgurkan3'
    def addEvidence(self,dataX,dataY):
        return self.learner.addEvidence(dataX,dataY)
    def query(self,points):
        return self.learner.query(points)