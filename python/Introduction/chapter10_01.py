# Chapter10-1
# Hangman(행맨) 미니게임 제작(1)
# 기본 프로그램 제작 및 테스트

# process time
import time

# Hello
name = input("What is your name? ")
print("Hi!, " + name, "Time to play hangman game!")
print()

#1 sec sleep
time.sleep(1)

print("Start loading...")
print()
time.sleep(0.5)

# answer
word = "secret"

# guess
guesses = ''

# chance count
turns = 10

# key : While Loop
# if chance count has remained
while turns > 0:
    # fail count
    failed = 0

    # iterate answer
    for char in word:
        # If guesses contains answer,
        if char in guesses:
            # print guessed charector
            print (char, end=' ')
        else:
            # print dash(_)
            print ("_", end=' ')
            # fail count up
            failed += 1

    # if succeed to guess word
    if failed == 0:
        print()
        print()
        print("Congratulations! The Guesses is correct.")
        # stop while statement
        break

    print()

    # input guessed word
    print()
    guess = input("guess a character:")

    # add word
    guesses += guess

    # If guessed word is not contained in answer word
    if guess not in word:
        # chance count down
        turns -= 1
        # print wrong message
        print("Oops! Wrong")
        # print remained change count
        print("You have", + turns, 'more guesses!')

        # if fail
        if turns == 0:
            # fail message
            print("You hangman game failed. Bye!")
