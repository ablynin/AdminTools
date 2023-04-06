"""Module for transliteration for passport"""
TRANSLIT_DICTIONARY = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'ZH',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'KH',
        'Ц': 'TS',
        'Ч': 'CH',
        'Ш': 'SH',
        'Щ': 'SHCH',
        'Ъ': 'IE',
        'Ы': 'Y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'IU',
        'Я': 'IA'
}


def translit(src_str):
    """Returns transliterated string"""
    res = ''
    for letter in src_str:
        if letter.upper() in TRANSLIT_DICTIONARY:
            if letter.isupper():
                res += TRANSLIT_DICTIONARY[letter.upper()].capitalize()
            else:
                res += TRANSLIT_DICTIONARY[letter.upper()].lower()
        else:
            res += letter
    return res
