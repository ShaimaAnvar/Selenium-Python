import pytest


def test_firstProgram():
    print('hello')

def test_secondProgram():
    print('hi')


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])