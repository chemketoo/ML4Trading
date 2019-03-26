import numpy as np

class DTLearner(object):

    def __init__(self, leaf_size=1,verbose = False):
	self.leaf_size = leaf_size
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
	numfeat = dataX.shape[1]
	numsam = dataY.shape[0]
	data = np.append(dataX, dataY.reshape(numsam,1),axis=1)
	if self.verbose: print data	
	self.tree = self.build_tree(data)
        if self.verbose: print self.tree 

        
    def build_tree(self,data):
	if data.shape[0] <= self.leaf_size or np.std(data[:,-1])==0:
		return np.array([-1, np.mean(data[:,-1]),0,0]).reshape(1,4)
   	maxfeat = 0
	maxcor = np.abs(np.corrcoef(data[:,0],data[:,-1])[0,1])
	for i in xrange(1,data.shape[1]-1):
		np.seterr(divide='ignore', invalid='ignore')
		cor = np.abs(np.corrcoef(data[:,i],data[:,-1])[0,1])
		if cor>maxcor:
			maxcor=cor
			maxfeat=i
	SplitVal = np.median(data[:,maxfeat])
	left_data = data[data[:,maxfeat]<=SplitVal]
	right_data = data[data[:,maxfeat]>SplitVal]
	if self.verbose:
		print left_data.shape
		print right_data.shape
	if left_data.shape[0]==data.shape[0] or right_data.shape[0]==data.shape[0]:
		return np.array([-1, np.mean(data[:,-1]),0,0]).reshape(1,4)
	
	left_tree = self.build_tree(left_data)
	right_tree = self.build_tree(right_data)
	root = np.array([maxfeat,SplitVal,1,left_tree.shape[0] + 1]).reshape(1,4)
	root = np.append(root,left_tree,axis=0)
	root = np.append(root,right_tree,axis=0)
	return root




    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
	y = []
	for point in points:
		yi = self.pointquery(point)
		y = y + [yi]	
        return  np.array(y)
    


    def pointquery(self,point):
	idx = 0
	while(self.tree[idx,0] != -1):
		if point[self.tree[idx,0].astype(int)]<=self.tree[idx,1]:
			idx = idx+1
		else:
			idx = idx+self.tree[idx,3].astype(int)
		if self.verbose: print idx
	return self.tree[idx,1]







if __name__=="__main__":
    print "the secret clue is 'zzyzx'"
