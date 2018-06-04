import numpy as np
i=0
for i in range(0, 20):
	a = np.random.choice(9, 16)
	s=""
	
	for letter in a:
		s +=str(letter)
	print("locations["+str(i)+"] = Location("+str(i)+", "+s+" )")
	i+=1