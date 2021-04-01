def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # 前面有怪符號
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	for line in lines:
		s = line.split(' ')
		time = s[0][:5] # 字串可以當做清單使用
		name = s[0][5:]
		print(name)

def main():
	filename = '3.txt'
	lines = read_file(filename)
	lines = convert(lines)

main()