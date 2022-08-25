#####################
#
#	Bill splitter
#	v2
#
#	Kalyan Pagadala
#	4 July 2022
#
#	Written using Python36
#
#####################

def csv_input(inp=""):
	# std_in = input(inp)
	return [i.strip() for i in inp.split(',')]

def read_ifile(fstr="template"):
	if not ".txt" in fstr:
		fstr += ".txt"
	
	with open(fstr, 'r') as f:
		cont = f.readlines()
	return cont

def main():
	for line in read_ifile("split"):
		if line.lower().startswith("enter people"):
			shares = {k: 0 for k in csv_input(line.split(":")[-1])}
			print(shares)
		elif line.lower().startswith("enter total"):
			total_bill = sum([float(i) for i in csv_input(line.split(":")[-1])])
		elif line.lower().startswith("enter discounted"):
			disco_bill = float(line.split(":")[-1])
			disco_percent = round(100 * (total_bill - disco_bill) / total_bill)
			print("Discount percent: {}%\n\n".format(disco_percent))
		elif line.lower().startswith("enter taxes"):
			taxes = sum([float(i) for i in csv_input(line.split(":")[-1])])
		elif line.split(",")[0].isnumeric():
			people = csv_input(line)[1:]
			cost   = float(csv_input(line)[0])
			while 'all' in people:
				people.pop(people.index('all'))
				people.extend(list(shares.keys()))
			for person in people:
				try:
					shares[person] = round(shares[person] + (cost/len(people)), 2)
				except KeyError as k:
					print(k)
					print("ERROR! Person entered for item not available. Check people involved")
			print('Current shares: ', shares, '. Current total: ', sum(shares.values()))

	total_before_tax = sum(shares.values())

	for person in shares:
		shares[person] = round(shares[person] + (taxes * (shares[person]/total_before_tax)), 2)

	print('Shares after tax, before discount: {}\n'.format(shares))

	for person in shares:
		shares[person] = round(shares[person] * ((100-disco_percent)/100), 2)

	print('Final Shares: {}\n\n'.format(shares))

	if 0.99*disco_bill < sum(shares.values()) < 1.01*disco_bill:
		print('Congrats. Total and sums match (within 1%)!!')
	else:
		print('Total Bill and sum of shares is different.')
		print('Disco Bill: ', disco_bill)
		print('Sum of shares: ', sum(shares.values()))
		# return

if __name__ == '__main__':
	main()
