import random

print("====================================")
print("標準出力ゲームへようこそ!")
print("最小値と最大値を入力してください。") 
print("最小値~最大値の範囲でランダムな数が選ばれます。")
print("その数を当ててください。")
print("チャンスは5回です。")
print("====================================")

print("====================================")
print(" ####   ######    ##    #####   ######  ")
print("#         #      #  #   #    #    #     ")
print(" ####     #     ######  #####     #     ")
print("     #    #     #    #  #  #      #     ")
print(" ####     #     #    #  #   ##    #     ")
print("====================================")

n = int(input("最小値: "))
m = int(input("最大値: "))

answer = random.randint(n, m)
chance = 5

while chance > 0:
    guess = int(input("予想: "))
    if guess == answer:
        print(" #####  #       ######    ##    #####   ")
        print("#       #       #        #  #   #    #  ")
        print("#       #       #####   ######  #####   ")
        print("#       #       #       #    #  #  #    ")
        print("#####  ######  ######  #    #  #   ##  ")
        print("回数: ", 5 - chance)
        break
    elif guess < answer:
        print("もっと大きい数です。")
    else:
        print("もっと小さい数です。")
    chance -= 1
    print("残りチャンス: ", chance)

print("正解は", answer, "でした。")

# python3 guess_the_number_game.py などで実行