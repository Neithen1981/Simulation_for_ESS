import random
import numpy as np    
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt    


class Female(object):
    def __init__(self, strategy, payoff = 0, age = 0):
        self.strategy = strategy
        self.payoff = payoff
        self.age = age

    def getStrategy(self):
        return self.strategy

    def getPayoff(self):
        return self.payoff

    def updatePayoff(self, payment):
        self.payoff += payment

    def getAge(self):
        return self.age

    def grow(self):
        self.age += 1
    
    def __str__(self):
        return self.strategy


class Male(Female):
    def __init__(self, strategy, payoff = 0, age = 0):
        Female.__init__(self, strategy, payoff, age)

    def mate(self, female, raise_cost, reward, time_cost):
        if self.strategy == 0:
            if (female.getStrategy() == 0):
                payment = raise_cost/2 + reward + time_cost
                self.updatePayoff(payment)
                female.updatePayoff(payment)
            else:
                payment = raise_cost/2 + reward
                self.updatePayoff(payment)
                female.updatePayoff(payment)
        else:
            if (female.getStrategy() == 1):
                self.updatePayoff(reward)
                female.updatePayoff(raise_cost + reward)
            else:
                payment = reward + time_cost
                self.updatePayoff(payment)
                female.updatePayoff(raise_cost + reward + time_cost)


def simulation(pop, faithful, coy, years, raise_cost, reward, time_cost, maxAge, refresh_rate):
    males = []
    females = []
    for i in range(faithful):
        males.append(Male(0))
    for i in range(coy):
        females.append(Female(0))
    for i in range(pop-faithful):
        males.append(Male(1))
    for i in range(pop-coy):
        females.append(Female(1))
    for year in range(years):
        simulationInOneYear(males, females, raise_cost, reward, time_cost, maxAge, pop, refresh_rate)
        visual(males, females)


def simulationInOneYear(males, females, raise_cost, reward, time_cost, maxAge, pop, refresh_rate):
    i = 0
    # reproduce
    males[:] = np.random.permutation(males)
    for female in np.random.permutation(females):
        males[i].mate(female, raise_cost, reward, time_cost)
    # refresh
    elimination = int(pop * refresh_rate)
    males.sort(key = lambda x:x.getPayoff())
    males[:] = males[elimination:]
    winner = males[-1]
    for i in range (elimination):
        males.append(winner)
    females.sort(key = lambda x:x.getPayoff())
    females[:] = females[elimination:]
    winner = females[-1]
    for i in range (elimination):
        females.append(winner)

def visual(males, females):
    f = 0
    p = 0
    co = 0
    fa = 0
    for male in males:
        if male.getStrategy() == 0:
            f += 1
        else:
            p += 1
    for female in females:
        if female.getStrategy() == 0:
            co += 1
        else:
            fa += 1
    labels = ["faithful", "philanderer", "coy", "fast"]
    quants = [f, p, co, fa]
    print(quants)
#    width = 0.4 
#    ind = np.linspace(0.5,9.5,4)  
#    # make a square figure  
#    fig = plt.figure(1)  
#    ax  = fig.add_subplot(111)  
#    # Bar Plot  
#    ax.bar(ind-width/2,quants,width,color='green')  
#    # Set the ticks on x-axis  
#    ax.set_xticks(ind)  
#    ax.set_xticklabels(labels)  
#    # labels  
#    ax.set_xlabel('strategy')  
#    ax.set_ylabel('number')  
#    # title  
#    ax.set_title('Different strategy numbers', bbox={'facecolor':'0.8', 'pad':5})  
#    plt.grid(True)  
#    plt.show()  
#    plt.close()  
pop = 500
coy = 250
faithful = 250
years = 100
raise_cost = -20
reward = 12
time_cost = -2
maxAge = 10
refresh_rate = 0.1

simulation(pop, faithful, coy, years, raise_cost, reward, time_cost, maxAge, refresh_rate)