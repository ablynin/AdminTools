import re

escaper = '*'
flags = {'escape': 'e'}

def normalize(number, flag=''):
    s = re.sub('[^0-9]', '', number)[-10:]
    # print(number, s, 'flag=', flag)
    if flag == flags['escape']:
        s = '{0}{1}{0}'.format(escaper, s)
    return s


if __name__ == '__main__':
    print(normalize('79104512008', 'e'))
