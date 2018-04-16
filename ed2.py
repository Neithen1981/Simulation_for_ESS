import random
import numpy as np    
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt    

"""
children will not fully inherit their parents
their traits(strategy) will change at a rate of randomness
"""

class Female(object):
    """
    0 for coy, 1 for fast
    """
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
    """
    0 for faithful, 1 for philanderer
    """
    def __init__(self, strategy, payoff = 0, age = 0):
        Female.__init__(self, strategy, payoff, age)
        
    def reproduce(self, female, randomness):
        mS = self.strategy
        fS = female.getStrategy()
        if random.random() < randomness:
            mS = mS^1
        if random.random() < randomness:
            fS = fS^1
        return (Male(mS), Female(fS))

    def mate(self, female, raise_cost, reward, time_cost, randomness):
        if self.strategy == 0:
            if (female.getStrategy() == 0):
                payment = raise_cost/2 + reward + time_cost
                self.updatePayoff(payment)
                female.updatePayoff(payment)
                return self.reproduce(female, randomness)
            else:
                payment = raise_cost/2 + reward
                self.updatePayoff(payment)
                female.updatePayoff(payment)
                return self.reproduce(female, randomness)
        else:
            if (female.getStrategy() == 1):
                self.updatePayoff(reward)
                female.updatePayoff(raise_cost + reward)
                return self.reproduce(female, randomness)
            else:
                raise Exception()

    
def simulation(pop, faithful, coy, years, raise_cost, reward, time_cost, maxAge, maxPop, randomness):
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
        simulationInOneYear(males, females, raise_cost, reward, time_cost, maxAge, maxPop, randomness)
        visual(males, females)


def simulationInOneYear(males, females, raise_cost, reward, time_cost, maxAge, maxPop, randomness):
    children = []
    i = 0
    # reproduce randomly
    males[:] = np.random.permutation(males)
    for female in np.random.permutation(females):
        try:
            children.append(males[i].mate(female, raise_cost, reward, time_cost, randomness))
        except Exception:
            pass
        female.grow()
        i += 1
    # grow
    for male in males:
        male.grow()
    # natural death
    l = males[:]
    for one in l:
        if one.getAge() > maxAge:
            males.remove(one)
    l = females[:]
    for one in l:
        if one.getAge() > maxAge:
            females.remove(one)
    # eliminate by population pressure
    elimination = len(males) + len(females) + 2*len(children) - maxPop
    if elimination > 0:
        total = males[:] + females[:]
        total.sort(key = lambda x:x.getPayoff())
        total = total[elimination:]
        males[:] = []
        females[:] = []
        for one in total:
            if isinstance(one, Male):
                males.append(one)
            else:
                females.append(one)
    for child in children:
        males.append(child[0])
        females.append(child[1])

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
pop = 200
coy = 100
faithful = 100
years = 2
raise_cost = -20
reward = 0
time_cost = -2
maxAge = 10
maxPop = 1000
randomness = 0.05

simulation(pop, faithful, coy, years, raise_cost, reward, time_cost, maxAge, maxPop, randomness)