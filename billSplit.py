#####################
#
#	Bill splitter
#	v1
#
#	Kalyan Pagadala
#	13 April 2021
#
#####################

def csv_input(inp=""):
	std_in = input(inp)
	return [i.strip() for i in std_in.split(',')]

def main():
	num_ppl = int(input("Enter number of people involved: "))

	shares = dict()
	for i in range(num_ppl): shares[input('Enter name for person {}: '.format(i+1))] = 0
	print(shares)

	total_bill = sum([float(i) for i in csv_input("Enter total bill amount (inc tax, exc discount)(csv): ")])
	disco_bill = float(input("Enter discounted bill amount (finally paid): "))

	taxes = sum([float(i) for i in csv_input("Enter taxes (csv in case of sgst,cgst,sch):")])

	disco_percent = round(100 * (total_bill - disco_bill) / total_bill)
	print("Discount percent: {}%\n\n".format(disco_percent))

	print("Enter the amount of each item and then names of people who split it")
	print("If multiple shares, enter the name multiple times")
	print("If everyone has a share, enter 'all'")
	print("Enter wrong name to skip/redo the item")
	print("Enter 'q' as item amount to stop filling items")
	while True:
		redo = False
		inp = input('Item amount: ')
		if inp == 'q': break
		inp = float(inp)
		people = csv_input('People who split this item (csv): ')

		if 'all' in people:
			people.pop(people.index('all'))
			people.extend(list(shares.keys()))
		
		for person in people:
			if person not in shares.keys():
				print("Person not there in People to share with. Skipping current item")
				redo = True
				break

		if redo: continue
   
		for person in people:
			shares[person] += round(inp/len(people), 2)

		print('Current shares: ', shares, '. Current total: ', sum(shares.values()))

	total_before_tax = sum(shares.values())

	for person in shares:
		shares[person] += round(taxes * (shares[person]/total_before_tax), 2)

	print('Shares after tax, before discount: {}\n'.format(shares))

	for person in shares:
		shares[person] *= (100-disco_percent)/100

	print('Final Shares: {}\n\n'.format(shares))

	if sum(shares.values()) != disco_bill:
		print('Total Bill and sum of shares is different.')
		print('Disco Bill: ', disco_bill)
		print('Sum of shares: ', sum(shares.values()))
		# return
	else:
		print('Congrats. Total and sums match!!')

if __name__ == '__main__':
	main()
