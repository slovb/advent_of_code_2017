def main(filename):
	def calc(data):
		total = 0
		l = len(data)
		for i,x in enumerate(data):
			j = (i + l/2) % l
			y = data[j]
			if y == x:
				total += y
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
