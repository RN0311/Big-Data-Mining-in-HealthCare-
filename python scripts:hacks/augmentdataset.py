# augementing the dataset given best features

f = open("bestfeatures.txt","r+")
g1 = f.readlines()
f.close()

file = '/home/samiya/Desktop/mridul_weka/train.csv'

f = open(file,"r+")
g2 = f.readlines()
firstrow = g2[0].replace('"','').split(",")
f.close()

indices = [0]
for i in g1[1:]:
	indices.append(int(i.split(" ")[0])-1)
indices.append(len(firstrow)-1)

# print(indices)

f = open("augmented.csv","w+")
for i in g2:
	x = i.strip().split(',')
	string = ''
	for j in indices:
		string+=x[j]+','

	string = string[:-1]+'\n'
	f.write(string)

f.close()