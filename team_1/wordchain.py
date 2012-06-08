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
    if destination == current:
        return [current]
    for next_current in neighbours(candidates, current):
        match = dfs(next_current, destination, candidates-set([next_current]))
        if match is not None:
            return match + [current]
    return None

def bfs(current, destination, candidates):
    current_neighbours = neighbours(candidates, current)
    for c in current_neighbours:
        if c == destination:
            return [current]

    for c in current_neighbours:
        match = bfs(c, destination, candidates)
        if match:
           return match
    return None

candidates = {x for x in dictionary if len(x) == len(first_word)}

def dist(current, destination, candidates):
    canddict = {x: None for x in candidates}
    canddict[current] = 0
    steps = 1
    while True:
        for word in canddict:
            if canddict[word] is None:
                for n in neighbours(candidates, word):
                    if n == destination:
                        return steps
                    if canddict[n] is None:
                        canddict[n] = steps
        steps += 1


def _test_2():
    assert list(neighbours(['bat', 'bog', 'bot'], 'bit')) == ['bat', 'bot']

def test_3():
    current = "dog"
    destination = "bat"
    path = dfs(current, destination, candidates)
    print path

def test_4():
    current = "dog"
    dest = "bat"
    path = dist(current, dest, candidates)
    #print path

def test_5():
    current = "dog"
    dest = "bat"
    path = bfs(current, dest, candidates)
    print path

