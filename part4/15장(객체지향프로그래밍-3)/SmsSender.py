from ContentSender import *


# ContentSender 추상클래스를 상속받음
class SmsSender(ContentSender):
    content = ""

    def __init__(self, title, name, content):
        # 조상클래스 생성자 호출
        super().__init__(title, name)
        self.content = content

    # 조상클래스의 멤버인 추상메서드를 오버라이딩을 한 것이다.
    # SmsSender 클래스는 인스턴스를 생성할 수가 있다.
    def sendMsg(self, recipient):
        print(f"제목 = {self.title}")
        print(f"이름 = {self.name}")
        print(f"내용 = {self.content}")
        print(f"받는사람 = {recipient}")
