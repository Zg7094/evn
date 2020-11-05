"""定义一个天山童姥类，类名为tonglao，属性有血量，武力值（通过传入的参数得到，类里有两个方法。
1. see_people方法，需要传入一个name参数，如果传入 wuyazi ，则打印 师弟 如果传入 李秋水 打印 呸 贱人
如果传入 丁春秋 打印  叛徒我杀了你
2. fight_zms方法--天山折梅手，调用该方法会将自己的武力值提升10倍，血量缩减2倍，需要传入敌人的hp,power ，
进行一回合制对打，打完后比较双发血量，血多的一方获胜
定义一个xuzhu类，继承于童姥，虚竹宅心仁厚不想打架，所以虚竹只有一个read的方法，每次调用都会打印 罪过罪过  加入模块化改造"""
class tonglao():
    def __init__(self):
        self.tonglao_hp = 1000
        self.tonglao_power = int(input("请输入你的武力值："))

    def see_people(self,name):
        if name == "wuyazi" :
            print("师弟！！！！")
        elif name == "liqiushui" :
            print("呸，贱人")
        elif name == "dingchunqiu" :
            print("叛徒，我要杀了你")


    def fight_zms(self,hp,power):
        self.tonglao_hp = self.tonglao_hp / 2
        self.tonglao_power = self.tonglao_power * 10
        final_tonglao_hp = self.tonglao_hp - power
        final_hp = hp - self.tonglao_power
        if final_hp > final_tonglao_hp :
            print("童姥输了")
        elif final_hp < final_tonglao_hp :
            print("童姥赢了")

class xuzhu(tonglao):
    def read(self):
        print("罪过罪过")

huminzhi = xuzhu()
huminzhi.see_people("wuyazi")
huminzhi.read()
huminzhi.fight_zms(1000,100)