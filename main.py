import random
import interface

attempts = 12
solution = [random.randrange(1, 7, 1) for i in range(1, 5)]

print(solution)

allUserGuesses = []

while attempts > 0:
    userInput = input("Twoja odpowiedź ")

    userGuess = [int(num) for num in userInput]
    print("Obecne: ", userGuess)
    print("Poprzednie: ")
    for guess in allUserGuesses:
        print(guess)
    allUserGuesses.append(userGuess)

    rightSpot = 0
    rightNum = 0
    allIndexes = []
    checkedNum = []

    for i in range(0, len(userGuess)):
        if userGuess[i] not in checkedNum:
            checkedNum.append(userGuess[i])
            if userGuess[i] in solution:
                numOfSameElementsUser = userGuess.count(
                    userGuess[i]
                )  # ile takich samych liczb w zgadywanym
                numOfSameElements = solution.count(
                    userGuess[i]
                )  # ile takich samych liczb w rozwiazaniu
                checkSameElements = numOfSameElements - numOfSameElementsUser
                if checkSameElements == 0:
                    rightNum += numOfSameElements  # jesli liczba zgadnietych liczb jest rowna liczb w rozwiazaniu
                elif checkSameElements > 0:
                    rightNum += numOfSameElementsUser  # jesli wiecej liczb jest w rozwiazaniu dodajemy tylko liczbe w zgadnietym
                else:
                    rightNum += numOfSameElements  # jesli wiecej liczb jest w zgadnietym dodajemy tylko liczbe w rozwiazaniu
        if userGuess[i] == solution[i]:
            rightSpot += 1  # jesli liczba jest na swoim miejscu
            rightNum -= 1  # odjęcie od na niewłaściwym miejscu

    attempts -= 1
    print("Na dobrym miejscu: ", rightSpot)
    print("Na niewłaściwym miejscu", rightNum)
    print("Pozostałe próby ", attempts)
