import csv

hold=[]
temp=""
with open('2008batsman.csv','r')as g:
	data = csv.reader(g)
	for row in data:
		hold.append(row[1].strip().lower().replace(" ",""))
g.close()

with open('2008_batsman_ranked.csv', mode='w') as file:
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	with open('basis.csv','r')as f:
		data = csv.reader(f)
		for row in data:
			with open('2008batsman.csv','r')as g:
				data1 = csv.reader(g)
				if(row[1].strip().lower().replace(" ","") in hold):
					for s in data1:
						if row[1].strip().lower().replace(" ","") == s[1].strip().lower().replace(" ",""):
							writer.writerow(s)
							break
				elif(row[1].strip().lower().replace(" ","") not in hold):
					writer.writerow(row)
