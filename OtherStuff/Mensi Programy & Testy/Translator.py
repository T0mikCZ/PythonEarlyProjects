def translate(stringToTranslate):
    stringToTranslate = str(stringToTranslate)

    translation = ""

    for letter in stringToTranslate:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "T"
            else:
                translation += "t"
        else:
            translation += letter
    
    return translation


print(translate("Za Warudo"))

