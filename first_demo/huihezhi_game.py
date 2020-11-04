#回合制游戏，电脑在200内随机减少血量，人则自己输入每轮减少血量。初始值均为1000
import random

def game():
    my_hp = 1000
    computer_hp = 1000
    while True:
        my_power = int(input("请输入你的攻击值（1~200）："))
        computer_power = random.randint(1,200)
        my_hp = my_hp - computer_power
        computer_hp = computer_hp - my_power
        if my_hp <= 0:
            print("你输了")
            break
        elif computer_hp <= 0:
            print("你赢了")
            break
        print("你的血量剩余为：", my_hp, "电脑的血量剩余为：", computer_hp)
game()




