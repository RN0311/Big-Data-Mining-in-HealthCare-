
file = "train.csv"

f = open(file,"r+")
g = f.readlines()[0].replace('"','')
f.close()

x = g.strip().split(',')

i = int(input())
print(x[i])