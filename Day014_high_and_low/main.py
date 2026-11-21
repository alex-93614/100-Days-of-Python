from os import name

import art
import random
import game_data

# art_logoを表示
print(art.logo)

# type(game_data.data)

# AとBをディクショナリから持ってくる。
person_a = random.choice(game_data.data)
person_b = random.choice(game_data.data)

if person_a == person_b:
    person_b = random.choice(game_data.data)

loop = True
score = 0

# 問題を表示する　不正解になるまでループ
while loop == True:
    # Aを表示
    print(f"CompareA: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}.")
    # VSを表示
    print(art.vs)
    # Bを表示
    print(f"CompareB: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}.")

    # ユーザがどっちがfollower多いかこたえる
    player_choice = input("Who has more followers? Type 'A' or 'B': ")

    # どっちがおおいか

    if person_a["follower_count"] > person_b["follower_count"]:
        answer = "A"
    elif person_a["follower_count"] < person_b["follower_count"]:
        answer = "B"

    # 正解？不正解？
    # 正解なら、正解数を表示する。ＢをＡにして、新しいＢを選ぶ。次の問題へ
    if answer == player_choice:
        score += 1
        print(f"You're right! Current score: {score}")
        person_a = person_b
        person_b = random.choice(game_data.data)

        if person_a == person_b:
            person_b = random.choice(game_data.data)

    # 不正解なら、正解数を表示して終了
    else:
        print(f"Sorry, That's wrong! Final score: {score}")
        loop = False
