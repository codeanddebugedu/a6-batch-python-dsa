"""
Logical Operators (to compare 2 or more comparisions)
AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T


OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT (reverse the result)
"""

physics = 33
chemistry = 99

# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)

# print(not (physics > 33 and chemistry > 33))
# print(not physics > 33 and chemistry > 33)
print(not (not physics > 33 and not chemistry > 33))
