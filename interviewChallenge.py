#recursion method idea obtained from here: 
#https://stackoverflow.com/questions/20193555/finding-combinations-to-the-provided-sum-value


#dataset given
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

#get items so its iterable
itemsInside = dataset.items();


dataSetLength = len(itemsInside);


#recursive function which checks which companies add up to the total items available
def findTheCompanies(index,currentList, allLists, totalAmount):
	priceAndSum = findTheSum(currentList)
	#print(priceAndSum[1]);
	#checks if the sum of the companies equals the total amount provided, if it matches it adds the list a another lis
	#where it has all the lists that have matched the total amount, else returns nothing
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


#adds up the items per company aswell as the total price 
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

allTheLists = findTheCompanies(0,[],[],25)

#sorts the list based on the total price
allTheLists.sort(key=lambda x:x[len(x)-1][1], reverse=True)
firstList = allTheLists[0];
length = len(firstList);

#output
print("The following companies following by the amount will give the most revenue");
for i in range(0,length-1):
	print("%s - %s" % (firstList[i][0],firstList[i][1][0]));
	#print(i[0] + " " + str(i[1][0]));
print("\n" + "To give a total profit of " + "$"+ str(firstList[length-1][1]));


