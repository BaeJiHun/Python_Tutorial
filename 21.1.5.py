# 클래스 init, 멤버변수, 메소드, 상속

class unit:
    def __init__(self,name,hp,damage):        #init: 초기변수 #name, hp, damage : 멤버변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다. 체력: {1} 공격력: {2}".format(self.name, self.hp, self.damage))

unit1 = unit("마린", 50, 5)
unit2 = unit("탱크", 150, 35)
unit3 = unit("레이스", 80, 10)

class attackunit:
    def __init__(self,name,hp,damage):        #init: 초기변수 #name, hp, damage : 멤버변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다. 체력: {1} 공격력: {2}".format(self.name, self.hp, self.damage))

    def attack(self,name):                      #메소드: attack
        print("{0}이 {1}에게 {2}의 데미지를 주었습니다.".format(self.name, name, self.damage))
        print("{0}이 {1}에게 {2}의 데미지를 주었습니다.".format(self.name, name, self.damage))
        print("{0}이 {1}에게 {2}의 데미지를 주었습니다.".format(self.name, name, self.damage))
        print("{0}이 {1}에게 {2}의 데미지를 주었습니다.".format(self.name, name, self.damage))
        print("{0}은 파괴되었습니다.".format(name))

    def damaged(self,name,damage):              #메소드: damaged
        self.hp -= damage
        print("{0}이 {1}에게 {2}의 데미지를 입었습니다.".format(self.name,name,damage))
        print("{0}의 현재 남은 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛은 파괴되었습니다.".format(self.name))


unit4 = attackunit("파이어뱃", 50, 16)
unit4.attack("마린")
unit4.damaged("레이스", 25)
unit4.damaged("질럿", 25)

# 상속
class BuildingUnit(unit):
    def __init__(self,name, hp, location):
        #부모 클래스 unit 초기화
        unit.__init__(self, name, hp, damage=0)
        self.location = location


# pass : 넘어간다 / 껍데기만 남겨둠
# super 초기화: 다중상속 시 후자의 부모클래스는 호출 X



