import numpy as np

class BagLearner(object):

    def __init__(self, learner,kwargs = {},bags=20, boost = False, verbose = False):
	self.numbags=bags
	self.learners=[]
	for i in xrange(bags):
		self.learners.append(learner(**kwargs))
	self.verbose = verbose
        pass # move along, these aren't the drones you're looking for

    def author(self):
        return 'bkumar37' # replace tb34 with your Georgia Tech username

    def addEvidence(self,dataX,dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
	numsam = dataY.shape[0]
	#data = np.append(dataX, dataY.reshape(numsam,1),axis=1)
	for l in self.learners:
		idx = np.random.randint(numsam,size=numsam)
		tempX = dataX[idx,:]
		tempY = dataY[idx]
		l.addEvidence(tempX,tempY)


    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
	y = np.zeros(points.shape[0])
	for l in self.learners:
		y = y + l.query(points)
	y = y/self.numbags
	return y


if __name__=="__main__":
    print "the secret clue is 'zzyzx'"
