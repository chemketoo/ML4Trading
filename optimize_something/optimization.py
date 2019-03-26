"""MC1-P2: Optimize a portfolio.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		   	  			    		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		   	  			    		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import pandas as pd  		   	  			    		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import datetime as dt  		   	  			    		  		  		    	 		 		   		 		  
from util import get_data, plot_data  
		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		   	  			    		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality
#def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
#    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False): 
      		   	  			    		  		  		    	 		 		   		 		  
def optimize_portfolio(sd,ed,syms,gen_plot):  		   	  			    		  		  		    	 		 		   		 		  
    import scipy.optimize as sc	   	  			    		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		   	  			    		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		   	  			    		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		   	  			    		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		   	  			    		  		  		    	 		 		   		 		  
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later  
    prices_SPY_norm = prices_SPY/prices_SPY.iloc[0]
    prices_norm = prices/prices.iloc[0] 	   	  			    		  		  		    	 		 		   		 		  
    x0 =np.asarray([1/float(len(syms)) for i in syms])
    bnds =[(0,1) for i in syms]
    def fun(x):
        alloced = prices_norm * x
        port_val=alloced.sum(axis=1)
        daily_rt =np.zeros(shape=len(port_val))
        i=1
        while i< len(port_val):
            daily_rt[i]=(port_val[i]/port_val[i-1])-1
            i+=1
        obj_func = (-1)*np.sqrt(252)*daily_rt.mean()/daily_rt.std() 
        return obj_func
    cons = {'type':'eq','fun':lambda x: 1.0 - np.sum(x)}
    solution = sc.minimize(fun,x0, bounds = bnds,constraints= cons)
    allocs = solution.x
    alloced = prices_norm * allocs
    port_val=alloced.sum(axis=1)
    dr =np.zeros(shape=len(port_val))
    i=1
    while i< len(port_val):
        dr[i]=(port_val[i]/port_val[i-1])-1
        i+=1
    adr = pd.np.sum(dr.mean())
    sddr=pd.np.sum(dr.std()) 
    sr = np.sqrt(252)*adr/sddr   
    cr = (port_val[-1] / port_val[0]) - 1
       	   	  			    		  		  		    	 		 		   		 		  
    #### find the allocations for the optimal portfolio  		   	  			    		  		  		    	 		 		   		 		  
    # note that the values here ARE NOT meant to be correct for a test case  		   	  			    		  		  		    	 		 		   		 		  
    #allocs = np.asarray([0.2, 0.2, 0.3, 0.3]) # add code here to find the allocations  		   	  			    		  		  		    	 		 		   		 		  
    #cr, adr, sddr, sr = [0.25, 0.001, 0.0005, 2.1] # add code here to compute stats  		   	  			    		  		  		    	 		 		   		 		   		   	  			    		  		  		    	 		 		   		 		  
    # Get daily portfolio value  		   	  			    		  		  		    	 		 		   		 		  
    # add code here to compute daily portfolio values  		   	  			    		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		   	  			    		  		  		    	 		 		   		 		  
    if gen_plot:
        plt.figure()      
        plt.plot(prices_SPY_norm, label='SPY') 
        plt.plot(port_val, label='Portfolio')
        plt.ylabel('Normalized Prices')
        plt.xlabel('Date')
        plt.title('Daily Portfolio Value and SPY')
        plt.legend()	  
        #df_temp = pd.concat([port_val, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)   	  			    		  		  		    	 		 		   		 		  
        plt.savefig('portfolio.png')        		   	  			    		  		  		    	 		 		   		 		            	  			    		  		  		    	 		 		   		 		  
    return allocs, cr, adr, sddr, sr  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def test_code():  		   	  			    		  		  		    	 		 		   		 		  
    # This function WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that any variables defined here are available to your function/code  		   	  			    		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Define input parameters  		   	  			    		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		   	  			    		  		  		    	 		 		   		 		  
    # the autograder!  		   	  			    		  		  		    	 		 		   		 		    	  			    		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008,06,01)  		   	  			    		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2009,06,01)  		   	  			    		  		  		    	 		 		   		 		  
    symbols = ['IBM', 'X', 'GLD', 'JPM']  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Assess the portfolio  		   	  			    		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date, syms = symbols,gen_plot = True)  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Print statistics  		   	  			    		  		  		    	 		 		   		 		  
    print "Start Date:", start_date  		   	  			    		  		  		    	 		 		   		 		  
    print "End Date:", end_date  		   	  			    		  		  		    	 		 		   		 		  
    print "Symbols:", symbols  		   	  			    		  		  		    	 		 		   		 		  
    print "Allocations:", allocations  		   	  			    		  		  		    	 		 		   		 		  
    print "Sharpe Ratio:", sr  		   	  			    		  		  		    	 		 		   		 		  
    print "Volatility (stdev of daily returns):", sddr  		   	  			    		  		  		    	 		 		   		 		  
    print "Average Daily Return:", adr  		   	  			    		  		  		    	 		 		   		 		  
    print "Cumulative Return:", cr  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
