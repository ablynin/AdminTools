# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, Tag
import string
from pass_gen import cyrillic_letters
import re

flags_def = {
    'empty': 'e',
    'latin': 'l',
    'cyrillic': 'c',
    'numbers': 'n',
    'spaces': 's',
    'punctuation': 'p',
    'emails': 'm',
    'replace': 'r',
    'no_emails': 'd',
    'default': 'f',
    'password': 'w'
}

colors_def = {
    flags_def['latin']: 'green',
    flags_def['cyrillic']: 'red',
    flags_def['numbers']: 'blue',
    flags_def['spaces']: 'yellow',
    flags_def['punctuation']: 'orange',
    flags_def['emails']: 'lime',
    flags_def['replace']: 'yellow',
    flags_def['default']: 'black',
    flags_def['password']: 'black'
}

highlight_styles = {}

replace_dict = {
    'А': 'A',
    'В': 'B',
    'Е': 'E',
    'З': '3',
    'К': 'K',
    'М': 'M',
    'Н': 'H',
    'О': 'O',
    'Р': 'P',
    'С': 'C',
    'Т': 'T',
    'У': 'Y',
    'Х': 'X',
    'Ь': 'b',
    'а': 'a',
    'б': '6',
    'е': 'e',
    'о': 'o',
    'р': 'p',
    'с': 'c',
    'у': 'y',
    'х': 'x'
}

mail_regex_string = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
mail_regex = re.compile(mail_regex_string)

font_family = 'MS Shell Dlg 2'
font_size = 8.25
bold = False
font_weight = {True: 700, False: 400}

emptyTextEditContext = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; '''
'''-qt-block-indent:0; text-indent:0px;"><br /></p></body></html>'''

testTextEditContext = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; '''
'''-qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; '''
'''text-indent:0px;">T<span class="cyrillic">ES</span>T</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; '''
'''text-indent:0px;">Y<span class="latin">YYY</span>Y</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; '''
'''-qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; '''
'''-qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; '''
'''text-indent:0px;">testТЕUСТ123gest</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; '''
'''-qt-block-indent:0; text-indent:0px;"><br /></p></body></html>'''


def new_line(soup):
    return soup.new_tag(
        'p',
        style=" margin-top:0px; margin-bottom:0px; margin-left:0px; "
              "margin-right:0px; -qt-block-indent:0; text-indent:0px;"
    )


def highlight_styles_init():
    global highlight_styles
    highlight_styles = {
        flags_def['latin']: '.latin {color: %s;}\n' % colors_def[flags_def['latin']],
        flags_def['cyrillic']: '.cyrillic {color: %s;}\n' % colors_def[flags_def['cyrillic']],
        flags_def['numbers']: '.numbers {color: %s;}\n' % colors_def[flags_def['numbers']],
        flags_def['spaces']: '.spaces {background-color: %s;}\n' % colors_def[flags_def['spaces']],
        flags_def['punctuation']: '.punctuation {color: %s;}\n' % colors_def[flags_def['punctuation']],
        flags_def['emails']: '.emails {background-color: %s}\n' % colors_def[flags_def['emails']],
        flags_def['replace']: '.replace {color: %s;}\n' % colors_def[flags_def['replace']]
    }


def new_empty_line(soup):
    nt = soup.new_tag(
        'p',
        style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
              "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
    )
    nt.append(soup.new_tag('br'))
    return nt


def highlight_emails(line, soup, flags=''):
    spl = []
    if flags_def['emails'] in flags:
        tag_span_emails = soup.new_tag('span')
        tag_span_emails.attrs = {'class': 'emails'}

        mails = mail_regex.findall(line)
        n_text = line
        sp = []
        for m in mails:
            sp = n_text.split(m)
            n_text = n_text.replace(m, '')
            n_text = n_text.replace(sp[0], '')
            if sp:
                spl.append(sp[0])
                tag_span_emails.append(m)
                spl.append(tag_span_emails.__copy__())
                tag_span_emails.string = ''

        if len(sp) > 1:
            spl.append(sp[1])
    return spl or [line]


def highlight_text(line, soup, flags=''):
    alphabet = []
    tag_span_latin = None
    tag_span_cyrillic = None
    tag_span_numbers = None
    tag_span_spaces = None
    tag_span_punctuation = None
    tag_span_replace = None

    if flags_def['latin'] in flags:
        tag_span_latin = soup.new_tag('span')
        tag_span_latin.attrs = {'class': 'latin'}
        alphabet += string.ascii_letters

    if flags_def['cyrillic'] in flags:
        tag_span_cyrillic = soup.new_tag('span')
        tag_span_cyrillic.attrs = {'class': 'cyrillic'}
        alphabet += cyrillic_letters

    if flags_def['numbers'] in flags:
        tag_span_numbers = soup.new_tag('span')
        tag_span_numbers.attrs = {'class': 'numbers'}
        alphabet += string.digits

    if flags_def['spaces'] in flags:
        tag_span_spaces = soup.new_tag('span')
        tag_span_spaces.attrs = {'class': 'spaces'}
        alphabet.append(' ')

    if flags_def['punctuation'] in flags:
        tag_span_punctuation = soup.new_tag('span')
        tag_span_punctuation.attrs = {'class': 'punctuation'}
        alphabet += string.punctuation

    if flags_def['replace'] in flags:
        tag_span_replace = soup.new_tag('span')
        tag_span_replace.attrs = {'class': 'replace'}
        alphabet += replace_dict.keys()

    tag = []
    non_cat = []
    for i, letter in enumerate(line):
        if flags_def['latin'] in flags and letter in string.ascii_letters:
            tag_span_latin.append(letter)
            if i == len(line) - 1 or line[i + 1] not in string.ascii_letters:
                tag.append(tag_span_latin.__copy__())
                tag_span_latin.string = ''
        elif flags_def['cyrillic'] in flags and letter in cyrillic_letters and (flags_def['replace'] not in flags or
                                                                                letter not in replace_dict.keys()):
            tag_span_cyrillic.append(letter)
            if i == len(line) - 1 or line[i + 1] not in cyrillic_letters:
                tag.append(tag_span_cyrillic.__copy__())
                tag_span_cyrillic.string = ''
        elif flags_def['numbers'] in flags and letter in string.digits:
            tag_span_numbers.append(letter)
            if i == len(line) - 1 or line[i + 1] not in string.digits:
                tag.append(tag_span_numbers.__copy__())
                tag_span_numbers.string = ''
        elif flags_def['spaces'] in flags and letter == ' ':
            tag_span_spaces.append(letter)
            if i == len(line) - 1 or line[i + 1] != ' ':
                tag.append(tag_span_spaces.__copy__())
                tag_span_spaces.string = ''
        elif flags_def['punctuation'] in flags and letter in string.punctuation:
            tag_span_punctuation.append(letter)
            if i == len(line) - 1 or line[i + 1] not in string.punctuation:
                tag.append(tag_span_punctuation.__copy__())
                tag_span_punctuation.string = ''
        elif flags_def['replace'] in flags and letter in replace_dict.keys():
            tag_span_replace.append(replace_dict[letter])
            if i == len(line) - 1 or line[i + 1] not in replace_dict.keys():
                if tag_span_cyrillic:
                    tag.append(tag_span_cyrillic.__copy__())
                    tag_span_cyrillic.string = ''
                tag.append(tag_span_replace.__copy__())
                tag_span_replace.string = ''
        else:
            non_cat.append(letter)
            if i == len(line) - 1 or line[i + 1] in alphabet:
                tag += non_cat
                non_cat = []
    # print(tag)
    return tag


def highlight_context(line, soup, flags=''):
    if not line:
        soup.body.append(new_empty_line(soup))
        return

    he = highlight_emails(line, soup, flags)
    ntg = []
    for h in he:
        if type(h) == Tag:
            tag_span_emails = soup.new_tag('span')
            tag_span_emails.attrs = {'class': 'emails'}
            ht = highlight_text(h.text, soup, flags)
            for t in ht:
                tag_span_emails.append(t)
            ntg.append(tag_span_emails.__copy__())
        else:
            ntg += highlight_text(h, soup, flags)
    tag = new_line(soup)
    for t in ntg:
        tag.append(t)
    soup.body.append(tag)


def transform_context(text, flags=''):
    context = (
        '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body '''
        f'''style=" font-family:{font_family}'; font-size:{font_size}pt; font-weight:{font_weight[bold]}; '''
        f'''font-style:normal; color:{colors_def[flags_def['default']]}"></body></html>'''
    )
    soup = BeautifulSoup(context, 'html.parser')
    highlight_styles_init()
    if flags_def['latin'] in flags:
        soup.style.append(highlight_styles[flags_def['latin']])
    if flags_def['cyrillic'] in flags:
        soup.style.append(highlight_styles[flags_def['cyrillic']])
    if flags_def['numbers'] in flags:
        soup.style.append(highlight_styles[flags_def['numbers']])
    if flags_def['spaces'] in flags:
        soup.style.append(highlight_styles[flags_def['spaces']])
    if flags_def['punctuation'] in flags:
        soup.style.append(highlight_styles[flags_def['punctuation']])
    if flags_def['emails'] in flags:
        soup.style.append(highlight_styles[flags_def['emails']])
    if flags_def['replace'] in flags:
        soup.style.append(highlight_styles[flags_def['replace']])

    tl = text.split('\n')

    if flags_def['no_emails'] in flags:
        n = []
        if tl[-1] == '':
            n = ['']
        tl = mail_regex.findall(text) + n

    if flags_def['empty'] in flags:
        for line in tl[:-1]:
            if not line or re.match('^ *$', line):
                tl.remove(line)

    for s in tl:
        highlight_context(s, soup, flags)
    res_context = str(soup)
    return res_context
