# 문제
# 은행 계좌에 돈을 저금할 수 있고 인출을 할 수 도 있다.
# 은행 계좌를 간단하게 클래스로 정의해보자.
# 은행계좌(Account) 는 현재 잔액(balance) 을 필드로 선언하고 기본 생성자를 작성하고
# 입금(deposit) 메서드와 출금(Withdraw) 메서드를 작성해보자.
# 출력결과
# 통장에 1,000,000원이 입금됨
# 현재 잔액 : 1,000,000원
# 통장에 200,000원이 출금됨
# 현재 잔액 : 800,000원

# 클래스 정의
class Account:
    __balance = 0

    # 기본 생성자
    def __init__(self, balance):
        self.__balance = balance

    # getter() 작성
    def getBalance(self):
        return self.__balance

    # setter() 작성
    def setBalance(self, balance):
        self.__balance = balance

    # 입금 메서드 작성
    def moneyDeposit(self, money):
        self.__balance += money
        print(f'통장에 {format(money, ",")}원이 입금됨')
        print(f'현재 잔액 : {format(self.getBalance(), ",")}원')

    # 출금 메서드 작성
    def moneyWithdraw(self, money):
        self.__balance -= money
        print(f'통장에 {format(money, ",")}원이 출금됨')
        print(f'현재 잔액 : {format(self.getBalance(), ",")}원')


if __name__ == "__main__":
    act1 = Account(0)
    act1.moneyDeposit(1000000)
    act1.moneyWithdraw(200000)
