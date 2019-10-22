# -*- coding: utf-8 -*-

"""Main module."""


import json

def lang_generator():
    """
    """
    with open('programming_languages.txt', 'r') as file:
        langs = file.readlines()
    for lang in langs:
        yield lang.strip()

def feelings_generator():
    with open('feelings.txt', 'r') as file:
        feelings = file.readlines()
    for feeling in feelings:
        yield feeling.strip()


def verbs_generator():
    with open('link_verbs.txt', 'r') as file:
        verbs = file.readlines()
    for verb in verbs:
        yield verb.strip()


def create_for_zip_1():
    list_ = []
    for language in lang_generator():
        for verb in verbs_generator():
            for feeling in feelings_generator():
                item = f'{language.capitalize()}{verb.capitalize()}{feeling.capitalize()}\n'
                list_.append(item)
    with open('password_1.txt', 'w') as file:
        file.writelines(list_)

def create_for_zip_2():
    list_ = []
    for language in lang_generator():
        for feeling in feelings_generator():
            item = f'{language.capitalize()}{feeling.lower()}\n'
            list_.append(item)
    with open('password_2.txt', 'w') as file:
        file.writelines(list_)


if __name__ == '__main__':
    create_for_zip_1()
    create_for_zip_2()
    