# 클래스 Tv를 설계하는 코드
class Tv:
    # 필드를 선언
    color = ''      # 색상
    power = False   # 전원
    channel = 0     # 채널
    volume = 0      # 볼륨

    # Tv를 전원을 켜거나 끄는 멤버 메서드
    def powerTv(self, power, tv):
        self.power = power
        if self.power == True:
            print("%s의 전원이 켜졌습니다." % tv)
        else:
            print("%s의 전원이 꺼졌습니다." % tv)

    # Tv 의 채널을 올리는 기능을 하는 멤버 메서드
    def channelUp(self, channel, tv):
        if channel < 0:
            print("채널은 음수일 수 없습니다.")
            return
        if not self.power:
            print("%s의 전원을 켜주세요." % tv)
            return
        self.channel += channel

    # Tv 의 채널을 올리는 기능을 하는 멤버 메서드
    def channelDown(self, channel, tv):
        if channel < 0:
            print("채널은 음수일 수 없습니다.")
            return
        if not self.power:
            print("%s의 전원을 켜주세요." % tv)
            return
        self.channel -= channel

    # Tv 의 볼륨을 올리는 기능을 하는 멤버 메서드
    def volumeUp(self, volume, tv):
        if volume < 0:
            print("볼륨은 음수일 수 없습니다.")
            return
        if not self.power:
            print("%s의 전원을 켜주세요." % tv)
            return
        self.volume += volume

    # Tv 의 볼륨을 올리는 기능을 하는 멤버 메서드
    def volumeDown(self, volume, tv):
        if volume < 0:
            print("볼륨은 음수일 수 없습니다.")
            return
        if not self.power:
            print("%s의 전원을 켜주세요." % tv)
            return
        self.volume -= volume

    # Tv의 현재 상태를 출력하는 메서드
    def printTv(self, tv):
        print("%s의 색상 : %s" % (tv, self.color))
        print("%s의 채널 : %s" % (tv, self.channel))
        print("%s의 볼륨 : %s" % (tv, self.volume))
