import itertools as it

#Accumulate : [ p0, p0+p1, p0+p1+p2, … ]
p = [5, 6, 4, 8, 3, 9]
print(list(it.accumulate(p)))


#Compress
data = ["Bruce", "Wayne", "05/04/1931", "Gotham", "Thomas"]
new_data = list(it.compress(data, [1, 0, 0, 1, 1]))
print(new_data)

#groupby()
str = 'qwerdsasdewsddddwwqqarr'
temp = sorted(str)
new_str = [list(g) for k, g in it.groupby(temp)]
print(new_str)