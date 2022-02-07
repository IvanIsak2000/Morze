line=str(input("введите строчку "))
l=list()
for element in line:
	if "а" in element:

		 l.append(".-")
	if "б" in element:
		 l.append("-...")
	if "в" in element:
		 l.append(".--")
	if  "г" in element:
		 l.append("--.")
	if  "д" in element:
		 l.append("-..")
	if  "е"in element:
		 l.append(".")
	if "й" in element:
		l.append(".---")
	if  "ж" in element:
		 l.append("...-")
	if  "з" in element:
		 l.append("--..")
	if  "и" in element:
		 l.append("..")
	if  "к" in element:
		 l.append("-.-")
	if  "л" in element:
		 l.append(".-..")
	if  "м" in element:
		 l.append("--")
	if  "н" in element:
		 l.append("-.")
	if  "о" in element:
		 l.append("---")
	if  "п" in element:
		 l.append(".--.")
	if  "р" in element:
		 l.append(".-.")
	if  "с" in element:
		 l.append("...")
	if  "т" in element:
		 l.append("-")
	if  "у" in element:
		 l.append("..-")
	if "ф" in element:
		 l.append("..-.")
	if " " in element:
		l.append(" ")
	if "х" in element:
		l.append("....")
	if "ц" in element:
		l.append("-.-.")
	if "ч" in element:
		l.append("---.")
	if "ш" in element :
		l.append("----")
	if "щ" in element:
		l.append("--.-")
	if "ъ" in element:
		l.append(".--.-.")
	if "ы" in element:
		l.append("-.--")
	if "ь" in element:
		l.append("-..-")
	if "э" in element:
		l.append("..-..")
	if "ю" in element:
		l.append("..--")
	if "я" in element:
		l.append(".-.-")
	if line=="выход":
		print("ЗАВЕРШЕНИЕ ПРОГРАММЫ")
		exit()



print("на азбуке Морзе: ")


for i in l:
	print(i)
print("ALL DONE")
