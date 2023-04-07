import re

escape_symbol = '*'
flags = {'escape': 'e'}


def normalize(number, flag=''):
    s = re.sub('[^0-9]', '', number)[-10:]
    if flag == flags['escape']:
        s = '{0}{1}{0}'.format(escape_symbol, s)
    return s
