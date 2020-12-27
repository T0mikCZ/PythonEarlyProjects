import string

def alphabet_position(text):
    text = text.lower()
    alphabetDic = dict(zip(string.ascii_lowercase, range(1,27)))
    textConvert = ""
    for i in range(len(text)):
        if text[i] in alphabetDic:
            if i == 0:
                textConvert += f"{str(alphabetDic[text[i]])}"
            else:
                textConvert += f" {str(alphabetDic[text[i]])}"
    return textConvert

print(alphabet_position("The sunset sets at twelve o' clock."))