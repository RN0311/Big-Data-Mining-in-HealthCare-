
# path = '/home/samiya/Desktop/mridul_weka/outputs/0.txt'
# f = open(path,'r+')
# g = f.readlines()[1036]
# f.close()

# x = g.split(": ")[1]
# x = x.strip().split(",")
# for i in range(len(x)):
# 	x[i] = int(x[i])

# setX = frozenset(x)

# for i in range(1, 100):
# 	path = '/home/samiya/Desktop/mridul_weka/outputs/'+str(i)+".txt"

# 	f = open(path,"r+")
# 	g = f.readlines()[1036]
# 	f.close()

# 	x = g.split(": ")[1]
# 	x = x.strip().split(",")[:120]
# 	for i in range(len(x)):
# 		x[i] = int(x[i])

# 	setY = frozenset(x)

# 	intersection = [x for x in setY if x in setX]

# 	setX = intersection

# 	# print(len(setX))




string = 'Selected attributes: 140,663,928,107,76,834,245,879,325,978,364,183,490,677,785,572,148,228,282,947 : 20'
setX = [int(x) for x in string.split(': ')[1].split(",")]



file = '/home/samiya/Desktop/mridul_weka/train.csv'

f = open(file,"r+")
g = f.readlines()[0].replace('"','').split(",")
# print g[1016]
f.close()


# print "TOP 50 FEATURES"
# for i in setX:
# 	# print i, g[i-1]
# 	print g[i-1]
if 'BMP5' in g:
	print "yeet"



	
