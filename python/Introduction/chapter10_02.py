# Chapter10-2
# Hangman mini game implementation 2
# completion of program and final test

# process time
import time
# random
import random
# process csv
import csv
# process sound
import winsound
# file io
import os

# Hello
name = input("What is your name? ")
print("Hi!, " + name, "Time to play hangman game!")
print()

#1 sec sleep
time.sleep(1)

print("Start loading...")
print()

# 0.5 sec sleep
time.sleep(0.5)

# CSV words list
words = []

# 문제 CSV 파일 로드
scriptPath = os.path.dirname(__file__)
filePath = os.path.join(scriptPath, './resource/word_list.csv')
with open(filePath, 'r') as f:
	reader = csv.reader(f)
	# Header Skip
	next(reader)
	for c in reader:
		words.append(c)

# shuffle
random.shuffle(words)
# choose a word
q = random.choice(words)

# answer
word = q[0].strip()

#guess
guesses = ''

#chance
turns = 10

# key : While Loop
# if chance count has remained (true)
while turns > 0:
    # failed character count
    failed = 0

    # iterate answer word
    for char in word:
        # 정답 단어 내에 추측 단어가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print (char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print ("_", end=' ')
            # 실패 횟수 증가
            failed += 1

    # if guess equal to answer
    if failed == 0:
        print()
        print()
		# succeed sound
        soundPath = os.path.join(scriptPath, './sound/good.wav')
        winsound.PlaySound(soundPath, winsound.SND_FILENAME)
		# succeed message
        print("Congratulations! The Guesses is correct.")
        # stop while statement
        break

    print()
    # i
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character:")

    # add inputted character
    guesses += guess

    # If current guess characters is not contained answer
    if guess not in word:
        # chance count down
        turns -= 1
        # fail message
        print("Oops! Wrong")
        # print remained chance count
        print("You have", + turns, 'more guesses!')

        # if turns is zero
        if turns == 0:
			# fail sound
            winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)
            # fail message
            print("You hangman game failed. Bye!")
