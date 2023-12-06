if ID == 0:
		nombre = np.sum(nombres)
	
	elif ID == 1:		
		nombre = np.prod(nombres)
		
	elif ID == 2:
		nombre = np.amin(nombres)
		
	elif ID == 3:
		nombre = np.amax(nombres)
	
	elif ID == 5:
		nombre = int(nombres[0] > nombres[1])
		
	elif ID == 6:
		nombre = int(nombres[0] < nombres[1])
		
	elif ID == 7:
		nombre = int(nombres[0] == nombres[1])
