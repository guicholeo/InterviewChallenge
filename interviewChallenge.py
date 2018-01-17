from operator import itemgetter

dataset = {'A': (1,1),
			'B':(2,5),
			'C':(3,8),
			'D':(4,9),
			'E':(5,10),
			'F':(6,17),
			'G':(7,17),
			'H':(8,20),
			'I':(9,24),
			'J':(10,30)
			}

itemsInside = dataset.items();


dataSetLength = len(itemsInside);


def findTheCompanies(index,currentList, allLists, totalAmount):
	priceAndSum = findTheSum(currentList)
	#print(priceAndSum[1]);
	if totalAmount == priceAndSum[0]:
		
		currentList.append(("Total",priceAndSum[1]));
		allLists.append(currentList);
		#currentList.remove(len(currentList)-1);
	elif totalAmount < priceAndSum[0]:
		return
	for i in range(index, dataSetLength):
		#print(itemsInside[i]);
		findTheCompanies(i+1,currentList + [itemsInside[i]],allLists,totalAmount);
	return allLists;



def findTheSum(listWithInfo):
	
	if not listWithInfo:
		return (0,0);
	else:
		totalPrice = 0;
		totalSum = 0;

		for i in listWithInfo:
			if i[0] != "Total":
				totalSum +=i[1][0];
				totalPrice += i[1][1];
		return (totalSum,totalPrice);

allthe = findTheCompanies(0,[],[],25)

for j in allthe:
	print(j);