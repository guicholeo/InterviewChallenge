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
for key in dataset:
	values = dataset[key];
	pricePerOne = float(values[0]) / values[1];
	dataset[key]  = values + (pricePerOne,);
