import random
import re
from exceptions import IncorrectInput

from abc import ABC, abstractmethod


class RegulyGry(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def guess(self, userGuess):
        pass

    @abstractmethod
    def userInputGuess(self, entry):
        pass

    @abstractmethod
    def returnUserGuesses(self):
        pass


class mastermind(RegulyGry):
    def __init__(self):
        self.__attempts = 12
        self.__solution = [random.randrange(1, 7, 1) for i in range(1, 5)]
        self.__allUserGuesses = []
        self.__listInfo = []

    def guess(self, userGuess):
        if self.__attempts > 0:
            self.__listInfo = []
            rightSpot = 0
            rightNum = 0
            checkedNum = []

            if userGuess == self.__solution:
                return "wygrana"

            for i in range(0, len(userGuess)):
                if userGuess[i] not in checkedNum:
                    checkedNum.append(userGuess[i])
                    if userGuess[i] in self.__solution:
                        numOfSameElementsUser = userGuess.count(
                            userGuess[i]
                        )  # ile takich samych liczb w zgadywanym
                        numOfSameElements = self.__solution.count(
                            userGuess[i]
                        )  # ile takich samych liczb w rozwiazaniu
                        checkSameElements = numOfSameElements - numOfSameElementsUser
                        if checkSameElements == 0:
                            rightNum += numOfSameElements  # jesli liczba zgadnietych liczb jest rowna liczb w rozwiazaniu
                        elif checkSameElements > 0:
                            rightNum += numOfSameElementsUser  # jesli wiecej liczb jest w rozwiazaniu dodajemy tylko liczbe w zgadnietym
                        else:
                            rightNum += numOfSameElements  # jesli wiecej liczb jest w zgadnietym dodajemy tylko liczbe w rozwiazaniu
                if userGuess[i] == self.__solution[i]:
                    rightSpot += 1  # jesli liczba jest na swoim miejscu
                    rightNum -= 1  # odjęcie od na niewłaściwym miejscu

            self.__attempts -= 1
            self.__listInfo.append(rightSpot)
            self.__listInfo.append(rightNum)
            self.__listInfo.append(self.__attempts)

            return self.__listInfo.copy()

    def userInputGuess(self, entry):
        try:
            num_format = re.compile(r"^([1-6][1-6][1-6][1-6])$")
            if not re.match(num_format, entry):
                raise IncorrectInput("Niepoprawny kod")
        except IncorrectInput:
            return -1

        userGuess = [int(num) for num in entry]
        self.__allUserGuesses.append(userGuess)

        return self.guess(userGuess)

    def returnUserGuesses(self):
        return self.__allUserGuesses.copy()


# w wersji oszusta nawet nie generujemy popranwej odpowiedzi jako ze ta odpowiedz nie bedzie brana pod uwage
class oszustMastermind(RegulyGry):
    def __init__(self):
        self.__attempts = 12
        self.__listInfo = []
        self.__allUserGuesses = []

    def guess(self, userGuess):
        if self.__attempts > 0:
            self.__listInfo = []

            rightSpot = 0
            rightNum = 0

            rightSpot = random.randrange(
                0, 5, 1
            )  # przy oszuscie wybieramy loswą liczbe na wlasciwym miejscu
            rightNum = random.randrange(
                0, 5 - rightSpot, 1
            )  # wybieramy losową liczbe ale taka zeby suma rightSpot i rightNum nie była większa od 4

            self.__attempts -= 1
            self.__listInfo.append(rightSpot)
            self.__listInfo.append(rightNum)
            self.__listInfo.append(self.__attempts)

            return self.__listInfo.copy()

    def userInputGuess(self, entry):
        try:
            num_format = re.compile(r"^([1-6][1-6][1-6][1-6])$")
            if not re.match(num_format, entry):
                raise IncorrectInput("Niepoprawny kod")
        except IncorrectInput:
            return -1

        userGuess = [int(num) for num in entry]
        self.__allUserGuesses.append(userGuess)

        return self.guess(userGuess)

    def returnUserGuesses(self):
        return self.__allUserGuesses.copy()


def gameMastermind():
    randomgame = random.randrange(
        2
    )  # losujemy czy zagramy normalnego masterminda czy oszukiwanego
    if randomgame == 0:
        return mastermind()
    else:
        return oszustMastermind()
