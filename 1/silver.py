def main(filename):
	def calc(data):
		total = 0
		last = data[-1]
		for x in data:
			if last == x:
				total += last
			last = x	
		return total
	with open(filename, 'r') as f:
		for line in f:
			data = map(int, line.rstrip())
			print('{} {}'.format(calc(data), line))

if __name__ == "__main__":
	import sys
	if (len(sys.argv) < 2):
		print('missing input parameter')
		exit()
	for f in sys.argv[1:]:
		main(f)
