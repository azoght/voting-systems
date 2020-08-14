#Voting Systems
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


Simulates ~~four~~ 4 vote count systems that can used with ranked ballots:
1. Plurality/Majority
2. Instant Runoff (IRV/RCV)
3. Borda Count
4. Condorcet

You can learn more about these four voting systems here: [**PBS Infinite Series: Voting Systems and the Condorect Paradox**](https://www.youtube.com/watch?v=HoAnYQZrNrQ)
![](https://image.pbs.org/video-assets/7GRiDXk-asset-mezzanine-16x9-Ju2FaRu.jpg.focalcrop.1200x630.50.10.jpg)

---

# Getting Started

> See travis.yml for how to get started

## Setup
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)

Requires Python 3 or higher
###To install:
```
pip install -r requirements.txt
```
###To clone:
```
git clone https://github.com/azoght/voting-systems
```

__Don't forget to fork and edit the code anyway you wish!__

## How to
###Make a ballot
#####Example:
```python
candidates = ['A','B','C']
votes = [1,2,3]
b = Ballot(candidates,votes)
```
###Make a ballot registry
#####Example (Non-randomized):
```python
r = BallotRegistry()
b = Ballot(['A','B','C'],[1,2,3])
for i in range(5):
    r.addBallot(b)
b = Ballot(['A','B','C'],[2,3,1])
for i in range(5):
    r.addBallot(b)
```
#####Example (Randomized):
```python
def randomBallotVoteConfiguration(c: []) -> []:
    con = c
    random.shuffle(con)
    return con
options = ['A','B','C']

configs = []
r = BallotRegistry()
for i in range(100):
    configs.append(randomBallotVoteConfiguration([1, 2, 3]))

for c in configs:
    r.addBallot(Ballot(options, c))
```

###Make vote count
```python
v = VoteCount(r)
# Voting Methods (return no value, but print winner)
v.plurality()
v.instantRunoff()
v.bordaCount()
v.condorcet()
```
