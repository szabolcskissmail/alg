# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:31:50 2020

@author: szabolcs
"""

import random

class Alg:
    def __init__(self, parentAlg, value):
        self._parentAlg = parentAlg
        self._value = value

    def calc(self) -> float:
        pass

    def format(self) -> str:
        pass

class AlgConst(Alg):
    def __init__(self, value):
        super().__init__(None, value)

    def calc(self) -> float:
        return self._value

    def format(self) -> str:
        return str(self._value)

class AlgAdd(Alg):
    def calc(self) -> float:
        return self._parentAlg.calc() + self._value

    def format(self) -> str:
        return "(" + self._parentAlg.format() + " + "+ str(self._value) + ")"

class AlgMinus(Alg):
    def calc(self) -> float:
        return self._parentAlg.calc() - self._value

    def format(self) -> str:
        return "(" + self._parentAlg.format() + " - "+ str(self._value) + ")"

class AlgMultiple(Alg):
    def calc(self) -> float:
        return self._parentAlg.calc() * self._value

    def format(self) -> str:
        return "(" + self._parentAlg.format() + " * "+ str(self._value) + ")"

class AlgDiv(Alg):
    def calc(self) -> float:
        return self._parentAlg.calc() / self._value

    def format(self) -> str:
        return "(" + self._parentAlg.format() + " / "+ str(self._value) + ")"


def generate(count, alg, deep = 0) -> Alg:
    if deep == count:
        return alg

    r = random.randint(0, 3)
    newdeep = deep + 1
    if r == 0:
        return generate(count, AlgAdd(alg, random.randint(1, 100)), newdeep)

    if r == 1:
        return generate(count, AlgMinus(alg, random.randint(1, 100)), newdeep)

    if r == 2:
        return generate(count, AlgMultiple(alg, random.randint(1, 100)), newdeep)

    if r == 3:
        return generate(count, AlgDiv(alg, random.randint(1, 100)), newdeep)

if __name__ == "__main__":
    A = generate(10, AlgConst(10))
    print(A.calc())
    print(A.format())
