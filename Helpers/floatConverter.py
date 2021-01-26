# Converts a list of numbers represented as: 0,245231 to Python recognizable floats
def floatConverter(listConvert):
    convertedList = []
    for items in listConvert:
        convertedString = ''
        for chars in items:
            if chars != ',':
                convertedString = convertedString + chars
            else:
                convertedString = convertedString + '.'
        convertedList.append(convertedString)
    return convertedList