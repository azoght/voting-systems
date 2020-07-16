import random

class Ballot:

    def __init__(self,c: [str],v: [int]):
        if len(c) == len(v):
            self.candidates = c
            self.votes = v
        else:
            self.candidates = None
            self.votes = None
            print("Invalid Ballot!")

def isEqualToAll(l1: [],l2: []) -> bool:
    if len(l1) == len(l2):
        count = 0
        for i in l1:
            if l1(i) == l2(i):
                count += 1
        if count == len(l1):
            return True
    return False

def hasMajority(b: Ballot) -> bool:
    majThreshold = 0
    for v in b.votes:
        if b.votes[v] != -1:
            majThreshold +=1
    majThreshold = majThreshold // 2
    biggest = 0
    for v in b.votes:
        if b.votes[v] > b.votes[biggest]:
            biggest = v
    if b.votes[biggest] >= majThreshold:
        return True
    return False

def containsBoth(l: [],a1,a2) -> bool:
    count1 = 0
    count2 = 0
    for i in l:
        if l[i] == a1:
            count1 += 1
        if l[i] == a2:
            count2 += 1
    if count1 > 0 and count2 > 0:
        return True
    return False

def isHigherThan(b: Ballot, b1: int, b2: int) -> bool:
    return b.votes[b1] < b.votes[b2]


class BallotRegistry:

    def __init__(self):
        self.br = []

    def addBallot(self, b: Ballot):
        if len(self.br) == 0:
            self.br.append(b)
        if len(self.br) >= 0:
            zeropos = self.br[0]
            if isEqualToAll(b.candidates,zeropos.candidates):
                self.br.append(b)
            else:
                print("Invalid ballot for registry")

class VoteCount:

    def __init__(self,br: BallotRegistry):
        self.registry = br

    def __makecountregister__(self) -> Ballot:
        vee = []
        for c in range(len(self.registry.br[0].candidates)):
            vee.append(0)
        count_register = Ballot(c=self.registry.br[0].candidates, v=vee)
        return count_register

    def plurality(self):
        count_register = self.__makecountregister__()
        for b in self.registry.br:
            for r in b:
                if b.votes[r] == 1:
                    count_register.votes[r] += 1

        winner = 0

        for c in count_register.votes:
            if count_register.votes[c] > count_register.votes[winner]:
                winner = c

        print("Winner is",count_register.candidates[winner])

    def instantrunoff(self):
        count_register = self.__makecountregister__()
        for o in range(1, len(count_register.candidates) - 1):
            for b in self.registry.br:
                for r in b:
                    if b.votes[r] == o and count_register.candidates[r] != -1:
                        count_register.votes[r] += 1
            least = 0
            for c in count_register.votes:
                if count_register.votes[c] < count_register.votes[least] and count_register.votes[c] != -1:
                    least = c

            if o > 1 and hasMajority(count_register):
                break
        winner = 0
        for c in count_register.votes:
            if count_register.votes[c] > count_register.votes[winner]:
                winner = c

        print("Winner is",count_register.candidates[winner])

    def bordacount(self):
        count_register = self.__makecountregister__()
        bordalist = []
        for i in reversed(range(len(count_register.votes) - 1)):
            bordalist.append(i)

        for o in range(1,len(count_register.candidates)):
            for b in self.registry.br:
                for r in b:
                    if b[r] == o:
                        count_register.votes[r] += bordalist[o - 1]

        winner = 0
        for c in count_register.votes:
            if count_register.votes[c] > count_register.votes[winner]:
                winner = count_register.candidates[winner]

        print("Winner is", winner)

    def condorcet(self):
        count_register = self.__makecountregister__()
        roundList = []
        r = []
        fillingList = True
        co = False
        lengthofRoundList = 0.5 * (len(count_register.candidates) ** 2) - 0.5 * len(count_register.candidates)
        while fillingList:
            r1 = random.uniform(0,len(count_register.candidates) - 1)
            r2 = random.uniform(0,len(count_register.candidates) - 1)
            if r1 != r2:
                for ro in roundList:
                    if containsBoth(ro, r1, r2):
                        co = True
                        break
                if co == True:
                    continue
                r.append(r1)
                r.append(r2)
                roundList.append(r)
            if len(roundList) == lengthofRoundList:
                fillingList = False

            for ro in roundList:
                c1 = 0
                c2 = 0
                for b in self.registry.br:
                    if isHigherThan(b, ro[0], ro[1]):
                        c1 += 1
                    else:
                        c2 += 1
                if c1 > c2:
                    count_register.votes[ro[0]] += 1
                if c2 > c1:
                    count_register.votes[ro[1]] += 1

            biggest_num = 0
            for v in count_register.votes:
                if count_register.votes[v] > biggest_num:
                    biggest_num = count_register.votes[v]

            count = 0
            for v in count_register.votes:
                if count_register.votes[v] == biggest_num:
                    count += 1

            if count > 1:
                print("It's a tie!")
            else:
                winner = ""
                for c in count_register.candidates:
                    if count_register.votes[c] == biggest_num:
                        winner = count_register.candidates[c]

                print("Winner is",winner)

