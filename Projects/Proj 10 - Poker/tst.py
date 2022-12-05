import rx7 as rx
a = rx.random.shuffle(list("23456789TJQKA"))
print(a)
RANKS = "23456789TJQKA"
Ranks_set = sorted(list(set(a)), key=lambda x:RANKS.index(x))
print(Ranks_set)
print()
exit()



def get_straight(ranks_set):
    ranks_set.reverse()
    for i,nom in enumerate(ranks_set):
        new = [nom-n for n in range(5)]
        if new==ranks_set[i:i+5]:
            return True
    return False

print(get_straight(Ranks_set))