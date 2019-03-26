"""Assess a betting strategy.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Bhuvesh Kumar  	  			    		  		  		    	 		 		   		 		  
GT User ID: bkumar37   	  			    		  		  		    	 		 		   		 		  
GT ID: 903338679	   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def author():  		   	  			    		  		  		    	 		 		   		 		  
        return 'bkumar37' # replace tb34 with your Georgia Tech username.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def gtid():  		   	  			    		  		  		    	 		 		   		 		  
	return 903338679 # replace with your GT ID number  		   	  			    		  		  		    	 		 		   		 		  


def get_spin_result(win_prob):
	result = False
	if np.random.random() <= win_prob:
		result = True
	return result

def myplot_data(df,filename="plot.png",title="Roullete Winnings", xlabel="Spin", ylabel="Winnings"):
    import matplotlib.pyplot as plt
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(linestyle='--')
    ax.set_ylim(-256,100)
    ax.set_xlim(0,300)
    ax.grid(linestyle='--')
    fig = ax.get_figure()
    fig.savefig(filename,dpi=1000)
    #plt.show()

def sim(money, win_prob):
	episode_winnings = 0
	spin_counter = 0
	winnings = np.full(1001,80.0)
	winnings[0]=0
	while episode_winnings < 80 and spin_counter < 1000:
		won = False
		bet_amount = 1
		while not won and spin_counter < 1000:
			won = get_spin_result(win_prob)
			spin_counter = spin_counter + 1
			if (won):
				episode_winnings = episode_winnings + bet_amount
			else:
				episode_winnings = episode_winnings - bet_amount
				if (money == -1):
					bet_amount = bet_amount*2
				else:
					bet_amount = min(money + episode_winnings, bet_amount*2)
			winnings[spin_counter] = episode_winnings
			if money != -1:
				if money + episode_winnings <= 0.001:
					winnings[spin_counter:] = episode_winnings
					spin_counter = 1000
			if episode_winnings >= 79.999:
				spin_counter = 1000
	return winnings

def multsim(num_sim, money= -1, win_prob = 18.0/38):
    sims = np.zeros((num_sim,1001))
    for i in range(num_sim):
        sims[i] = sim(money,win_prob)
    return sims 

def fig1(win_prob):
    sims = multsim(10)
    sims = pd.DataFrame(sims.T)
    myplot_data(sims,"figure1.png")

def fig23(sims):
    sims = sims.T
    #print sims.shape
    mea = sims.mean(axis=1)
    print "Expected value after 1000 spins: ",mea[1000]
    stds = np.std(sims, axis=1)
    #print mea.shape, stds.shape
    meap = mea + stds
    meam = mea - stds
    meandf = pd.DataFrame(data = {'mean': mea, 'mean + std': meap, 'mean - std': meam})
    myplot_data(meandf,"figure2.png")
    med = np.median(sims,axis=1)
    medp = med + stds
    medm = med - stds
    mediandf = pd.DataFrame(data = {'median': med, 'median + std': medp, 'median - std': medm})
    myplot_data(mediandf,"figure3.png")


def fig45(sims):
    sims = sims.T
    #print sims.shape
    mea = sims.mean(axis=1)
    print "Expected value after 1000 spins: ",mea[1000]
    stds = np.std(sims, axis=1)
    #print mea.shape, stds.shape
    meap = mea + stds
    meam = mea - stds
    meandf = pd.DataFrame(data = {'mean': mea, 'mean + std': meap, 'mean - std': meam})
    myplot_data(meandf,"figure4.png","Realistic Roullete Winnings")
    med = np.median(sims,axis=1)
    medp = med + stds
    medm = med - stds
    print stds[-1]
    mediandf = pd.DataFrame(data = {'median': med, 'median + std': medp, 'median - std': medm})
    myplot_data(mediandf,"figure5.png","Realistic Roullete Winnings")

def exp1(win_prob):
    print "Experiment 1"
    fig1(win_prob)
    sims = multsim(1000)
    t = sims[:,1000]>=80.0
    print "Number of 80 or more: ", np.count_nonzero(t)
    fig23(sims)      


def exp2(win_prob):
    print "Experiment 2"
    sims = multsim(1000,money=256)
    t = sims[:,1000]>=80.0
    print "Number of 80 or more: ", np.count_nonzero(t)
    fig45(sims)  
			

def test_code():  		   	  			    		  		  		    	 		 		   		 		  
	win_prob = 18.0/38 # set appropriately to the probability of a win  		   	  			    		  		  		    	 		 		   		 		  
	np.random.seed(gtid())
	exp1(win_prob)
	exp2(win_prob)	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
	# add your code here to implement the experiments  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":
    test_code()
