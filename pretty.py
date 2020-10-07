import tabulate

def pretty(arr):
	header = arr[0].keys()
	rows = [row.values() for row in arr]
	#print(header)
	#print(rows)
	print(tabulate.tabulate(rows, header))

def pretty1(row):
	header = row.keys()
	rows = [row.values()]
	print(tabulate.tabulate(rows,header))

def prettySkills(arr, comp):
	print(arr)
	print(comp)
