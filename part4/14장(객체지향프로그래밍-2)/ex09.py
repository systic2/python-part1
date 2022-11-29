# 메서드 오버라이딩 : 상속관계에서 조상클래스의 멤버메서드를 자손클래스에서 상속받아서
# 자신의 기능에 맞게끔 수정을 한다.(modify, change) 또는 재정의라고도 한다.
# 단, 메서드의 선언부는 반드시 동일하고 구현부만 다르게 하는 것이다.

# 조상클래스의 정의
class Car:
    speed = 0

    def upSpeed(self, speed):
        self.speed += speed
        print(f'현재속도(조상클래스) : {self.speed}')

    # __ 는 private 성질을 지니기 때문에 자신의 클래스에서만 작성하여 사용한다.
    # 상속도 안되고 마지막 메서드이다.
    # 이것의 용도는 자신의 클래스에서 호출하고 실행하고자 할 때 사용한다.
    def __downSpeed(self, speed):
        self.speed -= speed
        print(f'현재속도(조상클래스) : {self.speed}')

    def call(self):
        self.__downSpeed(100)


# 자손클래스 Sedan의 정의
class Sedan(Car):
    # 메서드 오버라이딩
    def upSpeed(self, speed):
        self.speed += speed
        # 150Km 속도를 넘지 못하게 한다.
        if self.speed > 150:
            self.speed = 150
            print(f'150Km를 넘을 수 없습니다.')
        print(f'현재속도(자손클래스) : {self.speed}')

    def downSpeed(self, speed):
        self.speed -= speed
        # super().__downSpeed(100)
        print(f'현재속도(자손클래스) : {self.speed}')


# 자손클래스 Truck의 정의
class Truck(Car):
    # 구현부에 pass 를 적으면, 조상클래스의 멤버만 상속받고 자신의 멤버는 추가하지 않겠다.
    pass


if __name__ == "__main__":
    sedan1 = None
    truck1 = None

    sedan1 = Sedan()
    truck1 = Truck()
    # 메서드 오버라이딩이 되어진 자손클래스의 upSpeed() 메서드가 호출됨
    sedan1.upSpeed(200)
    print(f'승용차의 속도 : {sedan1.speed}')
    truck1.upSpeed(200)
    print(f'트럭의 속도 : {truck1.speed}')
    # __메서드명() 형태는 외부에서도 호출할 수가 없다.
    # sedan1.__downSpeed(100)
    # sedan1.downSpeed(120)
    # truck 인스턴스는 __downSpeed를 호출할 수가 없다.
    car = Car()
    car.call()