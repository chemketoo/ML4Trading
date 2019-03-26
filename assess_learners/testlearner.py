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
import LinRegLearner as lrl  		   	  			    		  		  		    	 		 		   		 		  
import sys
import DTLearner as dt
import RTLearner as rt
import BagLearner as bl
import InsaneLearner as il
import matplotlib.pyplot as plt
from time import time as t
import util  

def exp1(trainX, trainY, testX, testY):
    leaf_sizes = range(1,31)
    cotr = []
    cote = []
    rmtr = []
    rmte = []
    for leaf_size in leaf_sizes:
        learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
        learner.addEvidence(trainX, trainY) # train it
        #print learner.author()

        # evaluate in sample
        predY = learner.query(trainX) # get the predictions
        rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
        #print
        #print "In sample results"
        print "Leaf_size: ", leaf_size
        c = np.corrcoef(predY, y=trainY)
        print "Train RMSE: ", rmse, "corr: ", c[0,1]
        cotr = cotr + [c[0,1]]
        rmtr = rmtr + [rmse]
        # evaluate out of sample
        predY = learner.query(testX) # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
        c = np.corrcoef(predY, y=testY)
        print "Tes RMSE: ", rmse, "corr: ", c[0,1]
        cote = cote + [c[0,1]]
        rmte = rmte + [rmse]

    print leaf_sizes
    print rmtr
    print rmte
    plt.plot(leaf_sizes,rmtr,'g')
    plt.plot(leaf_sizes,rmte,'r')
    plt.xlabel('leaf size')
    plt.ylabel('RMSE')
    plt.title('RMSE vs Leaf size plot for DTLearner')
    plt.legend(['Train', 'Test'])
    plt.grid(linestyle='--')
    plt.savefig('RMSEdt.png')

    plt.clf()

    print leaf_sizes
    print cotr
    print cote
    plt.plot(leaf_sizes,cotr,'g')
    plt.plot(leaf_sizes,cote,'r')
    plt.xlabel('leaf size')
    plt.ylabel('Correlation')
    plt.title('Correlation vs Leaf size plot for DTLearner')
    plt.legend(['Train', 'Test'])
    plt.grid(linestyle='--')
    plt.savefig('cordt.png')
    plt.clf()

def exp2(trainX, trainY, testX, testY):
    leaf_sizes = range(1,31)
    cotr = []
    cote = []
    rmtr = []
    rmte = []
    num_iter = 10

    for leaf_size in leaf_sizes:
        Tcotr,Tcote,Trmtr,Trmte = .0,.0,.0,.0
        for i in range(num_iter):
            #learner = rt.RTLearner(leaf_size=leaf_size,verbose=False)
            learner = bl.BagLearner(learner = dt.DTLearner, kwargs = {"leaf_size":leaf_size}, bags = 20, boost = False, verbose = False)
            learner.addEvidence(trainX, trainY) # train it
            #print learner.author()

            # evaluate in sample
            predY = learner.query(trainX) # get the predictions
            rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
            #print
            #print "In sample results"
            print "Leaf_size: ", leaf_size
            c = np.corrcoef(predY, y=trainY)
            print "Train RMSE: ", rmse, "corr: ", c[0,1]
            Tcotr = Tcotr + c[0,1]
            Trmtr = Trmtr + rmse
            # evaluate out of sample
            predY = learner.query(testX) # get the predictions
            rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
            c = np.corrcoef(predY, y=testY)
            print "Tes RMSE: ", rmse, "corr: ", c[0,1]
            Tcote = Tcote + c[0,1]
            Trmte = Trmte + rmse
        Trmte = Trmte/num_iter
        Tcotr = Tcotr/num_iter
        Trmtr = Trmtr/num_iter
        Tcote = Tcote/num_iter
        cotr = cotr + [Tcotr]
        rmtr = rmtr + [Trmtr]
        cote = cote + [Tcote]
        rmte = rmte + [Trmte]


    print leaf_sizes
    print rmtr
    print rmte
    plt.plot(leaf_sizes,rmtr,'g')
    plt.plot(leaf_sizes,rmte,'r')
    plt.xlabel('leaf size')
    plt.ylabel('RMSE')
    plt.title('RMSE vs Leaf size plot for BagLearner 20 bags (10 iter avg)')
    plt.legend(['Train', 'Test'])
    plt.grid(linestyle='--')
    plt.savefig('RMSEbag20.png')

    plt.clf()

    print leaf_sizes
    print cotr
    print cote
    plt.plot(leaf_sizes,cotr,'g')
    plt.plot(leaf_sizes,cote,'r')
    plt.xlabel('leaf size')
    plt.ylabel('Correlation')
    plt.title('Correlation vs Leaf size plot for BagLearner 20 bags (10 iter avg)')
    plt.legend(['Train', 'Test'])
    plt.grid(linestyle='--')
    plt.savefig('corbag20.png')
    plt.clf()

def exp3noisy(trainX, trainY, testX, testY):
  leaf_sizes = range(1,31)
  DTcotr = []
  DTcote = []
  DTrmtr = []
  DTrmte = []
  DTtimetr = []

  RTcotr = []
  RTcote = []
  RTrmtr = []
  RTrmte = []
  RTtimetr = []
  corrupt_rows = int(0.2*train_rows)
  corrupt_ind = np.random.randint(train_rows,size = corrupt_rows)
  trainX[[corrupt_ind],:] = 5*np.random.rand(corrupt_rows, trainX.shape[1])

  cotr,cote,rmtr,rmte, timetr, timete = [],[],[],[],[],[]
  

  num_iter = 20

  for leaf_size in leaf_sizes:
    Tcotr,Tcote,Trmtr,Trmte, Ttr, Tte = .0,.0,.0,.0,.0,.0
    for i in range(num_iter):
 
      learner = rt.RTLearner(leaf_size=leaf_size,verbose=False)
      
      

      #learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
      ti = t()
      learner.addEvidence(trainX, trainY) # train it
      tf = t()
      Ttr = Ttr + tf - ti
      #print learner.author()

      # evaluate in sample
      predY = learner.query(trainX) # get the predictions
      rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
      #print
      #print "In sample results"
      print "Leaf_size: ", leaf_size
      c = np.corrcoef(predY, y=trainY)
      print "Train RMSE: ", rmse, "corr: ", c[0,1]
      Tcotr = Tcotr + c[0,1]
      Trmtr = Trmtr + rmse
      
      # evaluate out of sample
      ti = t()
      predY = learner.query(testX) # get the predictions
      tf = t()
      Tte = Tte + tf - ti
      rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
      c = np.corrcoef(predY, y=testY)
      print "Tes RMSE: ", rmse, "corr: ", c[0,1]
      Tcote = Tcote + c[0,1]
      Trmte = Trmte + rmse
    Trmte = Trmte/num_iter
    Tcotr = Tcotr/num_iter
    Trmtr = Trmtr/num_iter
    Tcote = Tcote/num_iter
    Ttr = Ttr / num_iter
    Tte = Tte / num_iter
    cotr = cotr + [Tcotr]
    rmtr = rmtr + [Trmtr]
    cote = cote + [Tcote]
    rmte = rmte + [Trmte]
    timetr = timetr + [Ttr]
    timete = timete + [Tte]

  RTcotr = cotr
  RTcote = cote
  RTrmtr = rmtr
  RTrmte = rmte
  RTtimetr = timetr
  RTtimete = timete

  cotr,cote,rmtr,rmte, timetr, timete = [],[],[],[],[],[]
  num_iter = 1
  for leaf_size in leaf_sizes:
    Tcotr,Tcote,Trmtr,Trmte, Ttr, Tte = .0,.0,.0,.0,.0,.0
    for i in range(num_iter):
      
      
      learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
      

      ti = t()
      learner.addEvidence(trainX, trainY) # train it
      tf = t()

      Ttr = Ttr + tf - ti
      #print learner.author()

      # evaluate in sample
      predY = learner.query(trainX) # get the predictions
      rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
      #print
      #print "In sample results"
      print "Leaf_size: ", leaf_size
      c = np.corrcoef(predY, y=trainY)
      print "Train RMSE: ", rmse, "corr: ", c[0,1]
      Tcotr = Tcotr + c[0,1]
      Trmtr = Trmtr + rmse
      
      # evaluate out of sample
      ti = t()
      predY = learner.query(testX) # get the predictions
      tf = t()
      Tte = Tte + tf - ti
      rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
      c = np.corrcoef(predY, y=testY)
      print "Tes RMSE: ", rmse, "corr: ", c[0,1]
      Tcote = Tcote + c[0,1]
      Trmte = Trmte + rmse
    Trmte = Trmte/num_iter
    Tcotr = Tcotr/num_iter
    Trmtr = Trmtr/num_iter
    Tcote = Tcote/num_iter
    Ttr = Ttr / num_iter
    Tte = Tte / num_iter
    cotr = cotr + [Tcotr]
    rmtr = rmtr + [Trmtr]
    cote = cote + [Tcote]
    rmte = rmte + [Trmte]
    timetr = timetr + [Ttr]
    timete = timete + [Tte]


  DTcotr = cotr
  DTcote = cote
  DTrmtr = rmtr
  DTrmte = rmte
  DTtimetr = timetr
  DTtimete = timete

  #print leaf_sizes
  #print rmtr
  #print rmte

  plt.plot(leaf_sizes,DTrmtr,'g')
  plt.plot(leaf_sizes,DTrmte,'r')
  plt.plot(leaf_sizes,RTrmtr,'g--')
  plt.plot(leaf_sizes,RTrmte,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('RMSE')
  plt.title('RMSE vs Leaf size plot for DTLearner and RTlearner Noisy (20 iter avg)')
  plt.legend(['DT-Train', 'DT-Test','RT-Train', 'RT-Test'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-RMSE_noise.png')

  plt.clf()


  plt.plot(leaf_sizes,DTcotr,'g')
  plt.plot(leaf_sizes,DTcote,'r')
  plt.plot(leaf_sizes,RTcotr,'g--')
  plt.plot(leaf_sizes,RTcote,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('corellation')
  plt.title('corellation vs Leaf size plot for DTLearner and RTlearner Noisy (20 iter avg)')
  plt.legend(['DT-Train', 'DT-Test','RT-Train', 'RT-Test'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-cor_noise.png')
  
  plt.clf()

  plt.plot(leaf_sizes,DTtimetr,'g')
  #plt.plot(leaf_sizes,DTrmte,'r')
  plt.plot(leaf_sizes,RTtimetr,'g--')
  #plt.plot(leaf_sizes,RTrmte,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('Time (seconds)')
  plt.title('Train time vs Leaf size plot for DTLearner and RTlearner Noisy (20 iter avg)')
  plt.legend(['DT', 'RT'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-traintime_noise.png')


  plt.clf()


  plt.plot(leaf_sizes,DTtimete,'r')
  #plt.plot(leaf_sizes,DTrmte,'r')
  plt.plot(leaf_sizes,RTtimete,'r--')
  #plt.plot(leaf_sizes,RTrmte,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('Time (seconds)')
  plt.title('Test time vs Leaf size plot for DTLearner and RTlearner Noisy (20 iter avg)')
  plt.legend(['DT', 'RT'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-testtime_noise.png')

  plt.clf()


def exp3(trainX, trainY, testX, testY):
  leaf_sizes = range(1,31)
  DTcotr = []
  DTcote = []
  DTrmtr = []
  DTrmte = []
  DTtimetr = []

  RTcotr = []
  RTcofte = []
  RTrmtr = []
  RTrmte = []
  RTtimetr = []

  cotr,cote,rmtr,rmte, timetr, timete = [],[],[],[],[],[]
  

  num_iter = 20

  for leaf_size in leaf_sizes:
    Tcotr,Tcote,Trmtr,Trmte, Ttr, Tte = .0,.0,.0,.0,.0,.0
    for i in range(num_iter):
 
      learner = rt.RTLearner(leaf_size=leaf_size,verbose=False)
      
      

      #learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
      ti = t()
      learner.addEvidence(trainX, trainY) # train it
      tf = t()
      Ttr = Ttr + tf - ti
      #print learner.author()

      # evaluate in sample
      predY = learner.query(trainX) # get the predictions
      rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
      #print
      #print "In sample results"
      print "Leaf_size: ", leaf_size
      c = np.corrcoef(predY, y=trainY)
      print "Train RMSE: ", rmse, "corr: ", c[0,1]
      Tcotr = Tcotr + c[0,1]
      Trmtr = Trmtr + rmse
      
      # evaluate out of sample
      ti = t()
      predY = learner.query(testX) # get the predictions
      tf = t()
      Tte = Tte + tf - ti
      rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
      c = np.corrcoef(predY, y=testY)
      print "Tes RMSE: ", rmse, "corr: ", c[0,1]
      Tcote = Tcote + c[0,1]
      Trmte = Trmte + rmse
    Trmte = Trmte/num_iter
    Tcotr = Tcotr/num_iter
    Trmtr = Trmtr/num_iter
    Tcote = Tcote/num_iter
    Ttr = Ttr / num_iter
    Tte = Tte / num_iter
    cotr = cotr + [Tcotr]
    rmtr = rmtr + [Trmtr]
    cote = cote + [Tcote]
    rmte = rmte + [Trmte]
    timetr = timetr + [Ttr]
    timete = timete + [Tte]

  RTcotr = cotr
  RTcote = cote
  RTrmtr = rmtr
  RTrmte = rmte
  RTtimetr = timetr
  RTtimete = timete

  cotr,cote,rmtr,rmte, timetr, timete = [],[],[],[],[],[]
  num_iter = 1
  for leaf_size in leaf_sizes:
    Tcotr,Tcote,Trmtr,Trmte, Ttr, Tte = .0,.0,.0,.0,.0,.0
    for i in range(num_iter):
      
      
      learner = dt.DTLearner(leaf_size=leaf_size,verbose=False)
      

      ti = t()
      learner.addEvidence(trainX, trainY) # train it
      tf = t()

      Ttr = Ttr + tf - ti
      #print learner.author()

      # evaluate in sample
      predY = learner.query(trainX) # get the predictions
      rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
      #print
      #print "In sample results"
      print "Leaf_size: ", leaf_size
      c = np.corrcoef(predY, y=trainY)
      print "Train RMSE: ", rmse, "corr: ", c[0,1]
      Tcotr = Tcotr + c[0,1]
      Trmtr = Trmtr + rmse
      
      # evaluate out of sample
      ti = t()
      predY = learner.query(testX) # get the predictions
      tf = t()
      Tte = Tte + tf - ti
      rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])
      c = np.corrcoef(predY, y=testY)
      print "Tes RMSE: ", rmse, "corr: ", c[0,1]
      Tcote = Tcote + c[0,1]
      Trmte = Trmte + rmse
    Trmte = Trmte/num_iter
    Tcotr = Tcotr/num_iter
    Trmtr = Trmtr/num_iter
    Tcote = Tcote/num_iter
    Ttr = Ttr / num_iter
    Tte = Tte / num_iter
    cotr = cotr + [Tcotr]
    rmtr = rmtr + [Trmtr]
    cote = cote + [Tcote]
    rmte = rmte + [Trmte]
    timetr = timetr + [Ttr]
    timete = timete + [Tte]


  DTcotr = cotr
  DTcote = cote
  DTrmtr = rmtr
  DTrmte = rmte
  DTtimetr = timetr
  DTtimete = timete

  #print leaf_sizes
  #print rmtr
  #print rmte

  plt.plot(leaf_sizes,DTrmtr,'g')
  plt.plot(leaf_sizes,DTrmte,'r')
  plt.plot(leaf_sizes,RTrmtr,'g--')
  plt.plot(leaf_sizes,RTrmte,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('RMSE')
  plt.title('RMSE vs Leaf size plot for DTLearner and RTlearner (20 iter avg)')
  plt.legend(['DT-Train', 'DT-Test','RT-Train', 'RT-Test'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-RMSE.png')

  plt.clf()


  plt.plot(leaf_sizes,DTcotr,'g')
  plt.plot(leaf_sizes,DTcote,'r')
  plt.plot(leaf_sizes,RTcotr,'g--')
  plt.plot(leaf_sizes,RTcote,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('corellation')
  plt.title('corellation vs Leaf size plot for DTLearner and RTlearner (20 iter avg)')
  plt.legend(['DT-Train', 'DT-Test','RT-Train', 'RT-Test'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-cor.png')
  
  plt.clf()

  plt.plot(leaf_sizes,DTtimetr,'g')
  #plt.plot(leaf_sizes,DTrmte,'r')
  plt.plot(leaf_sizes,RTtimetr,'g--')
  #plt.plot(leaf_sizes,RTrmte,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('Time (seconds)')
  plt.title('Train time vs Leaf size plot for DTLearner and RTlearner (20 iter avg)')
  plt.legend(['DT', 'RT'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-traintime.png')


  plt.clf()


  plt.plot(leaf_sizes,DTtimete,'r')
  #plt.plot(leaf_sizes,DTrmte,'r')
  plt.plot(leaf_sizes,RTtimete,'r--')
  #plt.plot(leaf_sizes,RTrmte,'r--')
  plt.xlabel('leaf size')
  plt.ylabel('Time (seconds)')
  plt.title('Test time vs Leaf size plot for DTLearner and RTlearner (20 iter avg)')
  plt.legend(['DT', 'RT'])
  plt.grid(linestyle='--')
  plt.savefig('RT-DT-testtime.png')

  plt.clf()


  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    if len(sys.argv) != 2:  		   	  			    		  		  		    	 		 		   		 		  
        print "Usage: python testlearner.py <filename>"  		   	  			    		  		  		    	 		 		   		 		  
        sys.exit(1)  		   	  			    		  		  		    	 		 		   		 		  
    #inf = open(sys.argv[1])  		   	  			    		  		  		    	 		 		   		 		  
    #data = np.array([map(float,s.strip().split(',')) for s in inf.readlines()])
    datafile = sys.argv[1]
    with util.get_learner_data_file(datafile) as f:                                                               
        data = np.genfromtxt(f,delimiter=',')                                                                
        # Skip the date column and header row if we're working on Istanbul data                                                               
        if datafile == 'Istanbul.csv':                                                                
            data = data[1:,1:]  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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

    exp1(trainX, trainY, testX, testY)
    exp2(trainX, trainY, testX, testY)
    exp3(trainX, trainY, testX, testY)
    exp3noisy(trainX, trainY, testX, testY)       		   	  			    		  		  		    	 		 		   		 		  
