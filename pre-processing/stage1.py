import csv
f = open('2019.rtf','r')
hold=[]
positive = list(f.readlines())
for word in positive:
	word=word.replace("\n","")
	word=word.replace("\\","")
	word=word.replace(" ","")
	word.rstrip()
	if(len(word) < 20):
		hold.append(word)
	
with open('2018clean.csv', mode='w') as file:
	writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	with open('IPL2018.csv','rt')as f:
		data = csv.reader(f)
		for row in data:
			for s in hold:
				if row[1].replace(" ","") in s:
					writer.writerow(row)
		
