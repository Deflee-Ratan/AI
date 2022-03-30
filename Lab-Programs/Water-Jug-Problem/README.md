## WATER JUG PROBLEM
A Water Jug Problem: You are given two jugs, a 4-gallon one and a 3-gallon one, a
pump which has unlimited water which you can use to fill the jug, and the ground on
which water may be poured. Neither jug has any measuring markings on it. How can you
get exactly 2 gallons of water in the 4-gallon jug?
Here the initial state is (0, 0). The goal state is (2, n) for any value of n.
State Space Representation: we will represent a state of the problem as a tuple (x,
y) where x represents the amount of water in the 4-gallon jug and y represents the amount
of water in the 3-gallon jug. Note that 0 ≤ x ≤ 4, and 0 ≤ y ≤ 3.
To solve this we have to make some assumptions not mentioned in the problem.
They are:
  - We can fill a jug from the pump.
  - We can pour water out of a jug to the ground.
  - We can pour water from one jug to another.
  - There is no measuring device available.

Operators — we must define a set of operators that will take us from one state to
another.

| Sr. | Current State | Next State | Descriptions |
| --- | ------------- | ---------- | ------------ |
| 1 | (x,y) if x < 4 | (4,y) | Fill the 4 gallon jug |
| 2 | (x,y) if y < 3 | (x,3) | Fill the 3 gallon jug |
| 3 | (x,y) if x > 0 | (x-d,y) | Pour some water out of the 4 gallon jug |
| 4 | (x,y) if y > 0 | (x,y-d) | Pour some water out of the 3 gallon jug |
| 5 | (x,y) if y > 0 | (0,y) | Empty the 4 gallon jug |
| 6 | (x,y) if y > 0 | (x,0) | Empty the 3 gallon jug |
| 7 | (x,y) if x + y >= 4 and y > 0 | (4,y-(4-x)) | Pour water from the 3 gallon jug into the 4 gallon jug until the 4 gallon jug is full |
| 8 | (x,y) if x + y >= 3 and x > 0 | (x-(3-y),3) | Pour water from the 4 gallon jug into the 3 gallon jug until the 3 gallon jug is full |
| 9 | (x,y) if x + y <= 4 and y > 0 | (x+y,0) | Pour all the water from the 3 gallon jug into the 4 gallon jug |
| 10 | (x,y) if x + y <= 3 and x > 0 | (0,x+y) | Pour all the water from the 3 gallon jug into the 4 gallon jug |
| 11 | (0,2) | (2,0) | Pour 2 gallons from the 3 gallon jug into the 4 gallon jug |
| 12 | (2,y) | (0,y) | Empty the 2 gallons in the 4 gallon jug |
