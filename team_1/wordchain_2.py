import re
import sys

dictionary = [word.lower().strip() for word in
    open('/usr/share/dict/words').readlines() if re.match(r'\w+', word)]

first_word = 'dog' # raw_input("First word: ").lower()
second_word = 'bat' # raw_input("Second word: ").lower()

if len(first_word) != len(second_word):
    print "Fail"
    sys.exit()

def neighbours(cands, w1):
    for cand in cands:
        if sum(l1!=l2 for l1, l2 in zip(cand, w1)) == 1:
            yield cand

def dfs(current, destination, candidates):
    print current, destination, len(candidates)
    # for neighbour in path[-1].neigh
    # if neighbour == destination: reutrn
    # remove(neighbour from candidates)
    # dfs(neighbour)
    print current
#    candidates -= set([current])
    if destination == current:
        return [current]
    for next_current in sorted(neighbours(candidates, current), key=lambda w, d=destination: sum(l1==l2 for l1, l2 in zip(w, destination)), reverse=1):
        match = dfs(next_current, destination, candidates-set([next_current]))
        if match is not None:
            return match + [current]
    return None

def path(candidates, w1, w2):
    print len(candidates)
    #print candidates

candidates = {x for x in dictionary if len(x) == len(first_word)}

def test_1():
    print path(candidates, 'dog', 'bat')

def test_2():
    assert list(neighbours(['bat', 'bog', 'bot'], 'bit')) == ['bat', 'bot']

def test_3():
    current = "dog"
    destination = "bat"
    path = dfs(current, destination, candidates)
    print path
    assert(False)
