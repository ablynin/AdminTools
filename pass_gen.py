import string
import secrets

cyrillic_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cyrillic_upper = ''.join([c.capitalize() for c in cyrillic_lower])
cyrillic_letters = cyrillic_lower + cyrillic_upper
cyrillic_symbol = '№'

str_list = [string.digits, string.punctuation, string.ascii_uppercase, string.ascii_lowercase,
            cyrillic_lower, cyrillic_upper, cyrillic_symbol, ' ']

def create_pass(length=8, flags='ae'):
    alphabet = ''
    necessarily = 0
    if flags == 'e':
        flags = 'ae'

    if 'd' in flags:
        alphabet += string.digits
        necessarily += 1
    if 's' in flags:
        alphabet += string.punctuation
        necessarily += 1
    if 'u' in flags:
        alphabet += string.ascii_uppercase
        necessarily += 1
    if 'l' in flags:
        alphabet += string.ascii_lowercase
        necessarily += 1
    if 'o' in flags:
        alphabet += cyrillic_lower
        necessarily += 1
    if 'p' in flags:
        alphabet += cyrillic_upper
        necessarily += 1
    if 'q' in flags:
        alphabet += cyrillic_symbol
        necessarily += 1
    if 'r' in flags:
        alphabet += ' '
        necessarily += 1
    if 'a' in flags:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        necessarily = 1
    if 'c' in flags:
        bad_symbols = "'`|Il\"\\"
        alphabet = alphabet.translate({ord(c): None for c in bad_symbols})

    if necessarily == 0:
        necessarily = 1

    if length < necessarily:
        print('Password length is not enough: %s' % length)
        return None, necessarily

    temp_pass = ''
    while not temp_pass:
        temp_pass = "".join([alphabet[secrets.randbelow(len(alphabet))] for i in range(length)])
        if 'a' in flags:
            break
        if 'd' in flags:
            if not  set(string.digits) & set(temp_pass):
                temp_pass = ''
        if 's' in flags:
            if not  set(string.punctuation) & set(temp_pass):
                temp_pass = ''
        if 'u' in flags:
            if not  set(string.ascii_uppercase) & set(temp_pass):
                temp_pass = ''
        if 'l' in flags:
            if not  set(string.ascii_lowercase) & set(temp_pass):
                temp_pass = ''
        if 'o' in flags:
            if not set(cyrillic_lower) & set(temp_pass):
                temp_pass = ''
        if 'p' in flags:
            if not set(cyrillic_upper) & set(temp_pass):
                temp_pass = ''
        if 'q' in flags:
            if not set(cyrillic_symbol) & set(temp_pass):
                temp_pass = ''
        if 'r' in flags:
            if not ' ' in temp_pass:
                temp_pass = ''
        if 't' in flags:
            if len(set(temp_pass)) != len(temp_pass):
                temp_pass = ''

    if 'e' in flags:
        temp_pass = temp_pass.translate({ord(c): '\\' + c for c in string.punctuation})

    return temp_pass, necessarily

if __name__ == '__main__':
    # s1 = 'abcdeab'
    # s2 = set(s1)
    # print(len(s2), len(s1))
    print(create_pass(3, 'lopqt'))