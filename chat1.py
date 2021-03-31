import os # operating system

# 讀取檔案

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # 前面有怪符號
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	prerson = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new
				
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f: # 寫入模式, 沒有這個檔案就會產生這個檔案
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'input.txt'
	lines = read_file(filename)
	lines = convert(lines)
	write_file('output.txt', lines)

main()