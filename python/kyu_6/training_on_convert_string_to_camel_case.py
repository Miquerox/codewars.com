# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python


def to_camel_case(text):
    if not text:
        return ''
    result = []
    for word in text.replace('-', '_').split('_'):
        result.append(word.capitalize())
    return text[0] + ''.join(result)[1:]
