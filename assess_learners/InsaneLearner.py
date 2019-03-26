import numpy as np, LinRegLearner as lrl, BagLearner as bl
class InsaneLearner(object):
    def __init__(self,verbose = False): self.learner = bl.BagLearner(learner = bl.BagLearner, kwargs = { "learner" :lrl.LinRegLearner , "kwargs":{}, "bags":20, "boost":False, "verbose":False }, bags = 20, boost = False, verbose = False)
    def author(self): return 'bkumar37'
    def addEvidence(self,dataX,dataY): return self.learner.addEvidence(dataX,dataY)
    def query(self,points): return self.learner.query(points)
