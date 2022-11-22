# 클래스 안의 상수를 많이 사용한다.
# 상수는 보통 클래스 변수 형태로 지정하여 사용한다.

class Character:
    # 상수값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self):
        self.__hp = Character.NORMAL

    def levelup(self):
        self.__hp = Character.STRONG

    def damage(self):
        self.__hp = Character.WEAK

    # __str__() print() 주 목적으로 하는 것이 아니고 문자열을 리턴하게끔 해주는 것이 주 목적이다.
    def __str__(self):
        return f'HP : {self.__hp}'


if __name__ == "__main__":
    character = Character()
    print(character)
    character.levelup()
    print(character)
    character.damage()
    print(character)