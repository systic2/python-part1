# Monitor 클래스를 이용한 실습
from Monitor import *

if __name__ == "__main__":
    # 매개변수가 있는 생성자를 호출하는 방법
    # company, inch, price, color
    monitor1 = Monitor("LG", 32, 300000, "흰색")
    monitor1.__str__()
    print("------------------------------")
    monitor1.setCompany("삼성")
    monitor1.setInch(27)
    monitor1.setPrice(150000)
    monitor1.setColor("검정색")
    monitor1.__str__()
