# https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/python


def hello(name=None):
    return 'Hello, {name}!'.format(
        name=name.lower().capitalize() if name else 'World'
    )
