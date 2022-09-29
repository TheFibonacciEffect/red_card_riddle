# %%
from tqdm import tqdm
import random as r
import matplotlib.pyplot as plt
import numpy as np
# %%
def play_game(n,strategy,*args):
    drawn = []
    card_deck = [0]*(n//2) + [1]*(n//2)
    r.shuffle(card_deck)
    for i in range(n):
        card = card_deck.pop()
        drawn += [card]
        if not card_deck:
            return False #empty deck, you loose
        if strategy(drawn,n,*args):
            card = card_deck.pop()
            if card:
                return True
            else:
                return False

def simple(drawn,n):
    weighted_drawn = [1 if x == 0 else -1 for x in drawn]
    if sum(weighted_drawn)>=1:
        return True
    return False

def get_prop(drawn,n):
    n_remaining = n - len(drawn)
    number_red = n//2 - sum(drawn)
    number_black = n_remaining - number_red
    red_prop = number_red/n_remaining
    return red_prop

# props = []

n_end = 0
prop_prev = 0
def simple2(drawn,n, s): #TODO
    # global props
    global n_end
    global running_max
    prop = get_prop(drawn,n)
    # props += [prop]
    # running_max = prop if prop > prop_prev else prop_prev
    if prop > running_max:
        running_max = prop
    if len(drawn) >= s and prop>=0.55:
        return True
    elif len(drawn) == n-1:
        n_end += 1
        return True
    return False


N = 10000
# prop_array = [[],]*N
d = np.zeros([99,2])
for s in tqdm(range(99)):
    succ2 = 0
    succ1 = 0
    for i in range(N):
        # props = []
        running_max = 0
        # succ1 += play_game(100,simple)
        succ2 += play_game(10,simple2,s)
        # prop_array[i] = props
    d[s,:] = np.array([s,succ2/N])
plt.plot(*d.T)
# plt.plot()
# plt.show()
# %%
np.std(d,0)
p = d[:,1]
plt.hist(p)