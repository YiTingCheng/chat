import os # operating system

# 讀取檔案

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # 前面有怪符號
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	prerson = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_img_count = 0
	viki_img_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_img_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == "Viki":
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_img_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('allen說了', allen_word_count, '個字', '傳了', allen_sticker_count,'個貼圖', '傳了', allen_img_count,'張圖片')
	print('viki說了', viki_word_count, '個字', '傳了', viki_sticker_count,'個貼圖', '傳了', viki_img_count,'張圖片')	

				
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f: # 寫入模式, 沒有這個檔案就會產生這個檔案
		for line in lines:
			f.write(line + '\n')


def main():
	filename = 'LINE-Viki.txt'
	lines = read_file(filename)
	lines = convert(lines)
	# write_file('output.txt', lines)


main()

# 清單的切割寫法:
# n[開始值:結束值] (開始有包含, 結束不包含)
# n[:3] 可以拿到前3個 (開始值是0可以不寫)
# n[2:4] 可以拿到一個清單裝著n[2]跟n[3]
# n[-2:] 可以拿到最後2個 (結尾值不寫表示到最後)