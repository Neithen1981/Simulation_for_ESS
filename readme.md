# Simulation for ESS

#### The three versions of simulation are for "battle of sexes", a well-studied scene in evolutionary biology. It can be generalized to any long-term simulation of two gender strategies.

`ed2.py`: no fixed sex ratio

`ed3.py`: fixed sex ratio

`ed6.py`: "cunning" philanderer

All three models are sensible to the parameters, I recommand following the setting in the program.

### Simulation Logic:

We assume that, the sex ratio at the start of simulation is 1:1. Every year, each female can only mate once with a random male, and reproduce one pair of offsprings (one male and one female). If the mating is successful, the daughter will inherit her mother’s strategy and the son his father's.
Also, during the reproduction, because of different strategies adopted, besides offsprings, the parents will receive some payoffs as well. Details are listed below.

If one faithful male meets one coy female, they will spend some time to test each other and eventually bring up their children together. Hence each one receive half of the raise-cost and time-cost.

If one faithful male and one fast female, they will skip the test process and only receive half of the raise-cost each.

If the male is philanderer and the female is coy, they will not mate because the male would not spend time to assure the female. Thus each of them get 0 and no offspring is reproduced.

If the male is philanderer while the female is fast, philanderer father will leave the mother and let her bring up the children by herself. As a result, the female receive the raise-cost alone.

We also introduced a factor of mutation, by setting a threshold of randomness. Consequences are that some offsprings will adopt the opposite strategy of their parents at a certain level of probability.

Under the pressure of natural selection, the population cannot grow unlimitedly. We set an upper bound of the population. Once exceeded, those with the lowest accumulated payoffs will be eliminated. Also those elders will die naturally when they grew to a certain age.

Furthermore, as the mother will look after her children anyway, their payoffs are generally lower than males, causing females to be less in the whole population. To fit into the reality that the sex ratio is roughly 1:1, the elimination process can be conducted separately for the two genders. 

#### "Cunning" Philanderer

Adopting the new philanderer strategy, each year, the number of offsprings will be exactly the same as the environmental capacity. Therefore, all the parents will be eliminated. To solve this problem, we propose a new model by setting a refresh rate. Each year, a certain proportion of the population with the lowest payoff will be eliminated. And they were replaced by the strategy with the highest payoff.

### Explanation and Discussion

#### Impacts of mutation

When there is no mutation, i.e. offsprings will fully inherit their parents, coy females will be less or even be eliminated. We think that this is because without mutation, the population tends to play a better but less stable strategy. Just like in the Prisoner's Dilemma, if they both choose not to betray, they can actually do better, but it is not a Nash equilibrium. In our case, mutation is kind of a betrayal to the whole population. 

From the perspective of ESS, we can also explain this phenomenon. ESS requires that in the population, any small proportion of different strategies would not do better, thus is stable. But without mutation, there will not be this small proportion, hence the result may not be an ESS.

#### Fix sex ratio

One of the direct influences of not fixing sex ratio is that, females will be less than males. This is because mothers will look after their children anyway even if her husband left her alone, making them inferior when competing with the male gender.

Another influence is that, fixing sex ratio protects those fast females. If not fixing, coy is obviously a secure strategy. 

#### "Cunning" Philanderer

If the philanderer male spend time to cheat the coy female in order to have offsprings every year, their proportion in the population will dominate.  Also, due to the fact that coy no longer has the ability to recognize those irresponsible fathers, their numbers will decrease.


Thanks and have fun!