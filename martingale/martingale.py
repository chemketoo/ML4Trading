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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Seyma Gurkan (replace with your name)  		   	  			    		  		  		    	 		 		   		 		  
GT User ID: sgurkan3 (replace with your User ID)  		   	  			    		  		  		    	 		 		   		 		  
GT ID: 903087381 (replace with your GT ID)  		   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np
import matplotlib.pyplot as plt
  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def author():  		   	  			    		  		  		    	 		 		   		 		  
        return 'sgurkan3' # replace tb34 with your Georgia Tech username.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def gtid():  		   	  			    		  		  		    	 		 		   		 		  
	return 903087381 # replace with your GT ID number  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		   	  			    		  		  		    	 		 		   		 		  
	result = False  		   	  			    		  		  		    	 		 		   		 		  
	if np.random.random() <= win_prob:  		   	  			    		  		  		    	 		 		   		 		  
		result = True  		   	  			    		  		  		    	 		 		   		 		  
	return result  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def test_code():  		   	  			    		  		  		    	 		 		   		 		  
    win_prob = 0.4737 # set appropriately to the probability of a win  		   	  			    		  		  		    	 		 		   		 		  
    np.random.seed(gtid()) # do this only once
    simulation1(win_prob)  	
    simulation2(win_prob)	   	  			    		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob)) # test the roulette spin
 
def simulation1(win_prob): 
    sim=1
    while sim<11:
        winnings = np.zeros(1001)
        n=0   
        episode_winnings =0
        while n<1001:
            while episode_winnings < 80:
                won = False
                bet_amount = 1    
                while not won:
                    won = get_spin_result(win_prob)
                    n+=1
                    if won == True:
                        episode_winnings = episode_winnings + bet_amount
                        winnings[n]= episode_winnings
                    else:
                        episode_winnings = episode_winnings - bet_amount
                        winnings[n]= episode_winnings
                        bet_amount = bet_amount * 2 
            winnings[n]=80	
            n+=1
        sim+=1
        plt.xlim(0,300)
        plt.ylim(-256,100)      
        plt.plot(winnings)        	  			    		  		  		    	 		 		   		 		  
    plt.savefig('plot.png')
    sim=1
    winnings = np.zeros((1001,1001))
    while sim<1001:
        n=0   
        episode_winnings =0
        while n<1001:
            while episode_winnings < 80:
                won = False
                bet_amount = 1    
                while not won:
                    won = get_spin_result(win_prob)
                    n+=1
                    if won == True:
                        episode_winnings = episode_winnings + bet_amount
                        winnings[n][sim]= episode_winnings
                    else:
                        episode_winnings = episode_winnings - bet_amount
                        winnings[n][sim]= episode_winnings
                        bet_amount = bet_amount * 2 
            winnings[n][sim]=80	
            n+=1
        sim+=1         	  			    		  		  		    	 		 		   		 		  
    x=np.mean(winnings, axis=1)
    y=np.std(winnings, axis=1)
    z=np.median(winnings, axis=1)
    plt.figure()
    plt.xlim(0,300)
    plt.ylim(-256,100)      
    plt.plot(x) 
    plt.plot(x-y)
    plt.plot(x+y)         	  			    		  		  		    	 		 		   		 		  
    plt.savefig('plot2.png')
    plt.figure()
    plt.xlim(0,300)
    plt.ylim(-256,100)      
    plt.plot(z)
    plt.plot(z-y)
    plt.plot(z+y)        	  			    		  		  		    	 		 		   		 		  
    plt.savefig('plot3.png')	
    
def simulation2(win_prob): 
    sim=1
    winnings = np.zeros((1001,1001))
    while sim<1001:
            n=0   
            episode_winnings =0
            while n<1001:
                while episode_winnings < 80:
                    if episode_winnings==-256:
                        break
                    if n==1001:
                        break
                    won = False
                    bet_amount = 1    
                    while not won:
                        won = get_spin_result(win_prob)
                        n+=1
                        if won == True:
                            episode_winnings = episode_winnings + bet_amount
                            winnings[n][sim]= episode_winnings
                        else:
                            episode_winnings = episode_winnings - bet_amount
                            winnings[n][sim]= episode_winnings
                            bet_amount = bet_amount * 2 
                            if bet_amount>abs(-256-episode_winnings):
                                bet_amount=abs(-256-episode_winnings)
                if episode_winnings==-256:
                    winnings[n][sim]=-256	
                else:
                    winnings[n][sim]=80	
                n+=1
            sim+=1         	  			    		  		  		    	 		 		   		 		  
    x=np.mean(winnings, axis=1)
    y=np.std(winnings, axis=1)
    z=np.median(winnings, axis=1)
#    k=1
#    sim=1
#    while k<1002:
#        if winnings[k][sim]
    plt.figure()
    plt.xlim(0,300)
    plt.ylim(-256,100)      
    plt.plot(x) 
    plt.plot(x-y)
    plt.plot(x+y)         	  			    		  		  		    	 		 		   		 		  
    plt.savefig('plot4.png')
    plt.figure()
    plt.xlim(0,300)
    plt.ylim(-256,100)      
    plt.plot(z)
    plt.plot(z-y)
    plt.plot(z+y)        	  			    		  		  		    	 		 		   		 		  
    plt.savefig('plot5.png')		   	      
		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
