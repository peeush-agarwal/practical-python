# bounce.py
#
# Exercise 1.5

height = 100 # 100 meters

for i in range(1, 11):
    height *= float(3/5)
    print(i, round(height, 4))