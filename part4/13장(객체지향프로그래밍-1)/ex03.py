from Person import *

if __name__ == "__main__":
    # 기본 생성자 호출성
    # 기본 생성자는 호출되면 무조건 똑같은 초기값을 지니고 메모리에 생성된다.
    # 그리고 그 값을 변경하려면 직접 setter() 나 인스턴스명.필드 = 값 을 대입하여 변경하여야 하는 단점이 존재
    person1 = Person()
    person1.__str__()
    print("-------------------------")
    person2 = Person()
    person2.__str__()

    # 같은 필드의 값을 가지고 있지만 서로 다른 인스턴스이다.
    # print("person1의 주소 : ", id(person1))
    # print("person2의 주소 : ", id(person2))

    print("-------------------------")
    print("person1.name : ", person1.getName())
    person1.setName("김길동")
    print("person1.name : ", person1.getName())
    # age는 __ 가 붙지 않았기 때문에 public 성질을 지니고 있어서 변경이 가능
    person1.age = 50
    print("person1.age : ", person1.getAge())

