# 생성자에 대한 실습
# 개념 : 인스턴스를 생성하기 위해서 꼭 필요한 존재
# 아울러 필드의 초기화 메서드 역할을 한다.
# __init__() 작성해줌으로써 생성자가 호출이 된다.
# 만약에 클래스에 생성자가 존재하지 않으면 인터프리터가 알아서 하나의 기본생성자를 추가해준다.

class Person:
    name = ""
    age = 0
    height = 0
    weight: int = 0
    address: str = ''

    # 기본 생성자를 작성
    def __init__(self):
        self.__name = "홍길동"  # __를 붙이면 private 성질을 가진다.(클래스 내부에서만 접근이 가능)
        # __가 붙지 아니하면 public 성질을 지닌다 클래스 내부든 외부든 접근이 가능
        self.age = 35
        self.height = 175
        self.weight = 70
        self.address = "경북"
        print("Person의 기본 생성자 호출")

    # getter()는 리턴값만 존재하고 매개변수는 존재하지 않는다.
    def getName(self):
        return self.__name

    def getAge(self):
        return self.age

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getAddress(self):
        return self.address

    # setter() 메서드
    def setName(self, name):
        self.__name = name

    # __str__() 멤버변수의 값을 간단하게 확인하고자 할 때 사용하면 편리하다. 자바의 toString()와 유사하다.
    def __str__(self):
        print(self.__name, self.age, self.height, self.weight, self.address)
