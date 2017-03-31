# for weekly Q: prisoner delima

from random import randint
from statistics import mean

def prison_delima(n, strategy1, strategy2):
    suspect1=0
    suspect2=0
    while n > 0:
        if strategy1=="nice" and strategy2=='nice':
            suspect1 += 1
            suspect2 += 1
            n -= 1
        elif strategy1=='nice' and strategy2=='rat':
            suspect1 += 5
            suspect2 += 0
            n -= 1
        elif strategy1=='nice' and strategy2=='rat-nice':
            suspect1 += 5
            suspect2 += 0
            strategy2 = 'nice'
            n -= 1
        elif strategy1=='rat' and strategy2=='nice':
            suspect1 += 0
            suspect2 += 5
            n -= 1
        elif strategy1=='rat' and strategy2=='rat':
            suspect1 += 2
            suspect2 += 2
            n -= 1
        elif strategy1=='rat' and strategy2=='rat-nice':
            suspect1 += 2
            suspect2 += 2
            strategy2 = 'rat'
            n -= 1
        elif strategy1=='rat-nice' and strategy2=='nice':
            suspect1 += 0
            suspect2 += 5
            strategy1 = 'nice'
            n -= 1
        elif strategy1=='rat-nice' and strategy2=='rat':
            suspect1 += 2
            suspect2 += 2
            strategy1 = 'rat'
            n -=1
        elif strategy1=='rat-nice' and strategy2=='rat-nice':
            suspect1 += 2
            suspect2 += 2
            strategy1 = 'rat'
            strategy2 = 'rat'
            n -= 1

    return (suspect1, suspect2)

def expectation_of_certen_type(certen_type, n, times=300):
    types = ['nice', 'rat', 'rat-nice']
    years_for_certen=[]
    years_for_random=[]
    years=[]
    for t in range (0,times):
        strategy1 = certen_type
        strategy2 = types[randint(0,2)]
        years=prison_delima(n, strategy1, strategy2)
        years_for_certen.append(years[0])
        years_for_random.append(years[1])
    expectation_for_certen = mean(years_for_certen)
    expectation_for_random = mean(years_for_random)
    max_year_for_certen = max(years_for_certen)
    max_year_for_random = max(years_for_random)
    sum_of_both = mean(years_for_certen) + mean(years_for_random)

    return(expectation_for_certen, expectation_for_random,
           max_year_for_certen, max_year_for_random, sum_of_both)
        


