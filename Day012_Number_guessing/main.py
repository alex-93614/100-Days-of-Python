#数当てゲーム
# 1～100の数字を推測する
#回数　easyモード：10回、hardモード5回
import random
import art

#Todo 0.art表示
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: easy, medium, hard: ")


#Todo １．１～100の数字から1つランダムに選ぶ

correct_number = random.randint(1, 100)

#Todo 2.ユーザに難易度入力させる　⇒ loop回数を変数に代入
loop = 0
if difficulty == "easy":
    loop = 10
else:
    loop = 5

#Todo 3.loop回数が0になるまでwhile
while loop > 0:
     print(f"You have {loop} attempts remaining to guess the number.")
     # Todo 4.ユーザに数字入力させる
     guess = int(input("Guess a number: "))

     if guess == correct_number:
         # Todo 　丁度なら正解を表示して終了
        print(f"You got it! The answer was {correct_number}")
        break
     elif guess > correct_number:
            # Todo 　大きかったらToo highを表示してloop -1
        print("Too high.")
        loop = loop - 1
     else:
            # Todo 　小さかったらToo lowを表示してloop -1
        print("Too low.")
        loop = loop - 1

#Todo 5.loopが0になったらゲームオーバー
if loop == 0:
    print("You've run out of guesses. Goodbye!")