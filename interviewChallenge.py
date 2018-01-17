from operator import itemgetter

totalAmount = 25;

companies = [];

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

#find the price per one and add to  dictionary
# totalRequested = 0;
# for key in dataset:
# 	values = dataset[key];
# 	totalRequested +=values[0];
# 	pricePerOne = float(values[0]) / values[1];
# 	dataset[key]  = values + (pricePerOne,);

# #sort dictionary by the pricePerOne

itemsInside = dataset.items();
# itemsInside.sort(key=lambda x:x[1][2], reverse=True);
# print(totalRequested);

# if (totalRequested == total):
# 	print("Sell to all companies");
# else:
# 	recursive

dataSetLength = len(itemsInside);


def findTheCompanies(index,currentList, allLists, totalAmount):
	if totalAmount == sum(currentList):
		allLists.append(currentList);
	elif totalAmount < sum(currentList):
		return
	for i in range(index, dataSetLength):
		findTheCompanies(i,currentList + [itemsInside[i]],allLists,totalAmount);
	return allLists;

print(findTheCompanies(0,[],[],25));

