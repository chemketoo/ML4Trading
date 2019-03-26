"""  		   	  			    		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
import math  
import pandas as pd		   	  			    		  		  		    	 		 		   		 		  
import LinRegLearner as lrl
import DTLearner as dt
import RTLearner as rtl
import BagLearner as bl 
import matplotlib.pyplot as plt 		   	  			    		  		  		    	 		 		   		 		  
import sys

def question1(trainX,trainY,testX,testY):
    leaf_sizes = range(1,26)
    corrin = []
    corrout = []
    rmsein = []
    rmseout = []
    for leaf_size in leaf_sizes:
        learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
        learner.addEvidence(trainX, trainY) # train it

        # evaluate in sample
        predY = learner.query(trainX)
        predY = predY.astype(float)# get the predictions		   	  			    		  		  		    	 		 		   		 		  
        rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])  		   	  			    		  		  		    	 		 		   		 		    		   	  			    		  		  		    	 		 		   		 		  
        print "Leaf_size: ", leaf_size
        c = np.corrcoef(predY, y=trainY)
        print "Train RMSE: ", rmse, "corr: ", c[0,1]
        corrin = corrin + [c[0,1]]
        rmsein = rmsein + [rmse]
        
        # evaluate out of sample
        predY = learner.query(testX) 
        predY = predY.astype(float) # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
        print "Leaf_size: ", leaf_size
        c = np.corrcoef(predY, y=testY)
        print "Test RMSE: ", rmse, "corr: ", c[0,1]
        corrout = corrout + [c[0,1]]
        rmseout = rmseout + [rmse]
           
    plt.plot(leaf_sizes,rmsein,'g')
    plt.plot(leaf_sizes,rmseout,'r')
    plt.xlabel('leaf size')
    plt.ylabel('RMSE')
    plt.title('RMSE vs Leaf size plot for BagLearner')
    plt.legend(['Train', 'Test'])
    plt.grid(linestyle='--')
    plt.savefig('dtRMSE.png')
    plt.clf()
#    plt.plot(leaf_sizes,corrin,'g')
#    plt.plot(leaf_sizes,corrout,'r')
#    plt.xlabel('leaf size')
#    plt.ylabel('Correlation')
#    plt.title('Correlation vs Leaf size plot for DTLearner')
#    plt.legend(['Train', 'Test'])
#    plt.grid(linestyle='--')
#    plt.savefig('dtlcorr.png')
#    plt.clf()
 
def question2(trainX,trainY,testX,testY):
    leaf_sizes = range(1,26)
    corrin = []
    corrout = []
    rmsein = []
    rmseout = []
    for leaf_size in leaf_sizes:
        learner = learner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":leaf_size}, bags = 20, boost = False, verbose = False)
        learner.addEvidence(trainX, trainY) # train it

        # evaluate in sample
        predY = learner.query(trainX)
        predY = predY.astype(float)# get the predictions		   	  			    		  		  		    	 		 		   		 		  
        rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])  		   	  			    		  		  		    	 		 		   		 		    		   	  			    		  		  		    	 		 		   		 		  
        print "Leaf_size: ", leaf_size
        c = np.corrcoef(predY, y=trainY)
        print "Train RMSE: ", rmse, "corr: ", c[0,1]
        corrin = corrin + [c[0,1]]
        rmsein = rmsein + [rmse]
        
        # evaluate out of sample
        predY = learner.query(testX) 
        predY = predY.astype(float) # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
        print "Leaf_size: ", leaf_size
        c = np.corrcoef(predY, y=testY)
        print "Test RMSE: ", rmse, "corr: ", c[0,1]
        corrout = corrout + [c[0,1]]
        rmseout = rmseout + [rmse]       
   
    plt.plot(leaf_sizes,rmsein,'g')
    plt.plot(leaf_sizes,rmseout,'r')
    plt.xlabel('leaf size')
    plt.ylabel('RMSE')
    plt.title('RMSE vs Leaf size plot for BagLearner with 20 bags')
    plt.legend(['Train', 'Test'])
    plt.grid(linestyle='--')
    plt.savefig('blRMSE.png')
    plt.clf()
    
def question3(trainX,trainY,testX,testY):
 
    corrdt = []
    rmsedt = []
    corrrt = []
    rmsert = []
    
    dtlearner = dt.DTLearner()
    dtlearner.addEvidence(trainX, trainY) # train it
    # evaluate out of sample
    predY = dtlearner.query(testX) 
    predY = predY.astype(float) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    c = np.corrcoef(predY, y=testY)
    print "Test RMSE: ", rmse, "corr: ", c[0,1]
    corrdt = corrdt + [c[0,1]]
    rmsedt = rmsedt + [rmse]
    
    rtlearner = rtl.DTLearner()
    rtlearner.addEvidence(trainX, trainY) # train it
    # evaluate out of sample
    predY = rtlearner.query(testX) 
    predY = predY.astype(float) # get the predictions
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
    c = np.corrcoef(predY, y=testY)
    print "Test RMSE: ", rmse, "corr: ", c[0,1]
    corrrt = corrrt + [c[0,1]]
    rmsert = rmsert + [rmse]
    
       
#    plt.plot(l,rmsedt,'g')
#    plt.plot(leaf_sizes,rmsert,'r')
#    plt.xlabel('leaf size')
#    plt.ylabel('RMSE')
#    plt.title('DT vs. RT for RMSE')
#    plt.legend(['Train', 'Test'])
#    plt.grid(linestyle='--')
#    plt.savefig('Q3 - RMSE.png')
#    plt.clf()
 		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		    		   	  			    		  		  		    	 		 		   		 		  
    data = pd.read_csv('Data/Istanbul.csv')
    data=data.values	
    data = data[:,1:]
    data = data.astype(float)   	  			    		  		  		    	 		 		   		 		  
    # compute how much of the data is training and testing  		   	  			    		  		  		    	 		 		   		 		  
    train_rows = int(0.6* data.shape[0])  		   	  			    		  		  		    	 		 		   		 		  
    test_rows = data.shape[0] - train_rows  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # separate out training and testing data  		   	  			    		  		  		    	 		 		   		 		  
    trainX = data[:train_rows,0:-1]  		   	  			    		  		  		    	 		 		   		 		  
    trainY = data[:train_rows,-1] 		   	  			    		  		  		    	 		 		   		 		  
    testX = data[train_rows:,0:-1]  		   	  			    		  		  		    	 		 		   		 		  
    testY = data[train_rows:,-1]  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    print testX.shape  		   	  			    		  		  		    	 		 		   		 		  
    print testY.shape  		   	  			    		  		  		    	 		 		   		 		  
  
	
    
    # create a learner and train it  		   	  			    		  		  		    	 		 		   		 		  
    learner = dt.DTLearner(verbose = True) # create a LinRegLearner  		   	  			    		  		  		    	 		 		   		 		  
    l=learner.addEvidence(trainX, trainY) # train it  		   	  			    		  		  		    	 		 		   		 		  
    print learner.author()
	   	  			    		  		  		    	 		 		   		 		   		   	  			    		  		  		    	 		 		   		 		  
#  		   	  			    		  		  		    	 		 		   		 		  
    # evaluate in sample  		   	  			    		  		  		    	 		 		   		 		  
    predY = learner.query(trainX)
    predY = predY.astype(float)# get the predictions		   	  			    		  		  		    	 		 		   		 		  
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])  		   	  			    		  		  		    	 		 		   		 		    		   	  			    		  		  		    	 		 		   		 		  
    print "In sample results"  		   	  			    		  		  		    	 		 		   		 		  
    print "RMSE: ", rmse  		   	  			    		  		  		    	 		 		   		 		  
    c = np.corrcoef(predY, trainY)  		   	  			    		  		  		    	 		 		   		 		  
    print "corr: ", c[0,1]  		   	  			    		  		  		    	 		 		   		 		  
#  		   	  			    		  		  		    	 		 		   		 		  
    # evaluate out of sample  		   	  			    		  		  		    	 		 		   		 		  
    predY = learner.query(testX) # get the predictions
    predY = predY.astype(float)  		   	  			    		  		  		    	 		 		   		 		  
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Out of sample results"  		   	  			    		  		  		    	 		 		   		 		  
    print "RMSE: ", rmse  		   	  			    		  		  		    	 		 		   		 		  
    c = np.corrcoef(predY, testY)  		   	  			    		  		  		    	 		 		   		 		  
    print "corr: ", c[0,1]  

  ` question1(trainX,trainY,testX,testY)	
    question2(trainX,trainY,testX,testY)		   	  			    		  		  		    	 		 		   		 		  
