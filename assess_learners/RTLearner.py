#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 01:37:28 2018

@author: seymagurkan
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:11:47 2018

@author: seymagurkan
"""

"""  		   	  			    		  		  		    	 		 		   		 		  
A simple wrapper for linear regression.  (c) 2015 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			    		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			    		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			    		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			    		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			    		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			    		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			    		  		  		    	 		 		   		 		  
or edited.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		   	  			    		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			    		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			    		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np 
import collections as cl 		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
class RTLearner(object):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    def __init__(self, leaf_size=1, verbose = False): 
        self.verbose=verbose
        self.leaf_size=leaf_size 		   	  			    		  		  		    	 		 		   		 		  
        pass # move along, these aren't the drones you're looking for  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    def author(self):  		   	  			    		  		  		    	 		 		   		 		  
        return 'sgurkan3' # replace tb34 with your Georgia Tech username  		   	  			    		  		  		    	 		 		   		 		  
	   	  			    		  		  		    	 		 		   		 		  
    def addEvidence(self,dataX,dataY):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Add training data to learner  		   	  			    		  		  		    	 		 		   		 		  
        @param dataX: X values of data to add  		   	  			    		  		  		    	 		 		   		 		  
        @param dataY: the Y training values
        @data x ve data ylar her seferinde update ediliyor!!!!!  		   	  			    		  		  		    	 		 		   		 		  
        """
        dataY=dataY.flatten()  		   	  			
        if dataX.shape[0] <= self.leaf_size:
            return [[-1, dataY[0], 0, 0]] 
        if len(cl.Counter(dataY)) == 1: 
            return [[-1, dataY[0], 0, 0]] 
        else:
            i =np.random.random_integers(0,dataX.shape[1]-1)
            dataY=dataY[dataX[:,i].argsort()]
            dataX=dataX[dataX[:,i].argsort()]
            SplitVal = np.median(dataX[:,i])
            if dataX[dataX[:,i]<=SplitVal].shape[0] ==dataX.shape[0] or dataX[dataX[:,i]>SplitVal].shape[0] ==dataX.shape[0]:
                return [[-1, np.mean(dataY), 0, 0]]
            else: 
                lefttree = np.array(self.addEvidence(dataX[dataX[:,i]<=SplitVal],dataY[dataX[:,i]<=SplitVal]))       
                righttree =np.array(self.addEvidence(dataX[dataX[:,i]>SplitVal],dataY[dataX[:,i]>SplitVal]))
            lefttree =np.asarray(lefttree)
            root = np.array([i,SplitVal,1,lefttree.shape[0] + 1]).reshape(1,4)
            root = np.append(root,lefttree,axis=0)
            root = np.append(root,righttree,axis=0)
            self.tree = root
        return root
    
    
    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        y=[]
        mytree = self.tree
        for point in points:
            j =0
            while(mytree[j,0] != -1):
                if point[int(float(mytree[j,0]))] <=float(mytree[j,1]):
                    j+=1
                else:
                    j+=int(float(mytree[j,3]))
            y= y + [mytree[j,1]]       
        return np.array(y)
	   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "the secret clue is 'zzyzx'"  	

	   	  			    		  		  		    	 		 		   		 		  
