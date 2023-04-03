text = str(input("Enter text in Russian: ")).lower()
result = []
for element in text:
    if "а" in element:
        result.append(".-")
    if "б" in element:
        result.append("-...")
    if "в" in element:
        result.append(".--")
    if "г" in element:
        result.append("--.")
    if "д" in element:
        result.append("-..")
    if "е" in element:
        result.append(".")
    if "й" in element:
        result.append(".---")
    if "ж" in element:
        result.append("...-")
    if "з" in element:
        result.append("--..")
    if "и" in element:
        result.append("..")
    if "к" in element:
        result.append("-.-")
    if "л" in element:
        result.append(".-..")
    if "м" in element:
        result.append("--")
    if "н" in element:
        result.append("-.")
    if "о" in element:
        result.append("---")
    if "п" in element:
        result.append(".--.")
    if "р" in element:
        result.append(".-.")
    if "с" in element:
        result.append("...")
    if "т" in element:
        result.append("-")
    if "у" in element:
        result.append("..-")
    if "ф" in element:
        result.append("..-.")
    if " " in element:
        result.append(" ")
    if "х" in element:
        result.append("....")
    if "ц" in element:
        result.append("-.-.")
    if "ч" in element:
        result.append("---.")
    if "ш" in element:
        result.append("----")
    if "щ" in element:
        result.append("--.-")
    if "ъ" in element:
        result.append(".--.-.")
    if "ы" in element:
        result.append("-.--")
    if "ь" in element:
        result.append("-..-")
    if "э" in element:
        result.append("..-..")
    if "ю" in element:
        result.append("..--")
    if "я" in element:
        result.append(".-.-")
    if text == "выход":
        print("ЗАВЕРШЕНИЕ ПРОГРАММЫ")
        exit()


print("In Morse code")


print(*result,sep=' ')
for_exit = input("Press to exit...")
