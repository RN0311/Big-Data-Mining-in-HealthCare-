f1 = open("/home/samiya/Desktop/mridul_weka/pos_train_normal.txt","r+")
g = f1.readlines()
header = g[0]

g1 = g[1:]

f2 = open("/home/samiya/Desktop/mridul_weka/pos_test_normal.txt","r+")
g2 = f2.readlines()[1:]

f3 = open("/home/samiya/Desktop/mridul_weka/neg_train_normal.txt","r+")
g3 = f3.readlines()[1:]

f4 = open("/home/samiya/Desktop/mridul_weka/neg_test_normal.txt","r+")
g4 = f4.readlines()[1:]

header = header.strip() + ",LABEL\n"

final = [header]

for i in g1:
	final.append(i.strip()+",1\n")
print "pos_train_normal copied"

for i in g2:
	final.append(i.strip()+",1\n")
print "pos_test_normal copied"

for i in g3:
	final.append(i.strip()+",0\n")
print "neg_train_normal copied"

for i in g4:
	final.append(i.strip()+",0\n")
print "neg_test_normal copied"


f = open("final.csv","w+")

for i in final:
	f.write(i)

f.close()