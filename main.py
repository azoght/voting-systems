
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

    def plurality(self):
        pass

    def instantrunoff(self):
        pass

    def bordacount(self):
        pass

    def condorcet(self):
        pass