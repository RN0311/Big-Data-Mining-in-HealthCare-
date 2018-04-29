# Checks if output of all the feature selections are consistent

path = '/home/samiya/Desktop/mridul_weka/outputs/0.txt'
f = open(path,'r+')
g = f.readlines()
f.close()

length = len(g)
word = g[1036].split(" ")[0]

for i in range(1,100):
	path = '/home/samiya/Desktop/mridul_weka/outputs/'+str(i)+".txt"
	f = open(path,'r+')
	g = f.readlines()
	f.close()

	Nlength = len(g)
	Nword = g[1036].split(" ")[0]

	if Nlength != length or word != Nword:
		print("what")