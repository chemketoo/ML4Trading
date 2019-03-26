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
from scipy.optimize import minimize


def compute_sr(allocs,prices,rfr=0.0, sf = 252.0):
	port_val = (prices*allocs).sum(axis=1)
	dr = (port_val.values[1:]/port_val.values[:-1])-1
	adr = dr.mean()
	sddr = np.std(dr,ddof=1)
	sr = np.sqrt(sf) * (adr - rfr) / sddr 
	return -1*sr


def compute_portfolio_stats(prices,allocs,rfr=0.0, sf = 252.0):
	port_val = (prices*allocs).sum(axis=1)
	dr = (port_val.values[1:]/port_val.values[:-1])-1
	adr = dr.mean()
	sddr = np.std(dr,ddof=1)
	cr = port_val[-1]/port_val[0] - 1
	sr = np.sqrt(sf) * (adr - rfr) / sddr 
	return cr,adr,sddr,sr


def myplot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
	import matplotlib.pyplot as plt
	"""Plot stock prices with a custom title and meaningful axis labels."""
	ax = df.plot(title=title, fontsize=12)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.grid(linestyle='--')
	fig = ax.get_figure()
	fig.savefig('./plot.png')
	plt.show()

												
# This is the function that will be tested by the autograder                                                
# The student must update this code to properly implement the functionality                                                
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
	syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):                                                
												
	# Read in adjusted closing prices for given symbols, date range                                                
	dates = pd.date_range(sd, ed)                                                
	prices_all = get_data(syms, dates)  # automatically adds SPY                                                
	prices = prices_all[syms]  # only portfolio symbols                                                
	prices_SPY = prices_all['SPY']  # only SPY, for comparison later                                                
												

	prices_SPY = prices_SPY/prices_SPY.ix[0]
	prices = prices/prices.ix[0]

	res = minimize(compute_sr, [1.0/len(syms)]*len(syms), bounds = ((0,1),)*len(syms), \
		constraints = ({ 'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs) }), args = ((prices)), \
		)
	allocs = res.x
	cr, adr, sddr, sr = compute_portfolio_stats(prices = prices,allocs=allocs,rfr = 0.0, sf = 252.0)           
												
	# Compare daily portfolio value with SPY using a normalized plot                                                
	if gen_plot:                                                
		port_val = (prices*allocs).sum(axis=1)                                                
		df_temp = pd.concat([port_val, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)
		myplot_data(df_temp, title="Daily portfolio value and SPY", xlabel="Date", ylabel="Normalized price")                                                
		pass                                                
												
	return allocs, cr, adr, sddr, sr                                                
												
def test_code():                                                
	# This function WILL NOT be called by the auto grader                                                
	# Do not assume that any variables defined here are available to your function/code                                                
	# It is only here to help you set up and test your code                                                
												
	# Define input parameters                                                
	# Note that ALL of these values will be set to different values by                                                
	# the autograder!                                                
												
	start_date = dt.datetime(2008,6,1)
	end_date = dt.datetime(2009,6,1)
	symbols = ['IBM', 'X', 'GLD','JPM']
                                            
												
	# Assess the portfolio                                                
	allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
		syms = symbols, \
		gen_plot = True)                                                
												
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
