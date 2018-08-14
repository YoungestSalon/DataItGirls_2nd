# VendingMachine이라는 새로운 개념이 생김
class VendingMachine:

    # VendingMachine의 초기값을 설정해줌.
    # test_vm.py에서 'm = VendingMachine()'을 실행하는 순간 실체(인스턴스)가 생김
    # self : 새로 생긴 실체(인스턴스) 그 자체를 가리키며, 자아(=초기값)를 부여해줌
    # _change : change 앞의 under-bar(_) = '클래스 정의 부분 밖에서 임의로 change 호출/변경 금지'를 의미
    # __init__ : under-bar가 2개(__) = 'Python 내장 문법이기 때문에 절대 임의로 변경하지 말 것'을 의미
    def __init__(self):
        self._change = 0

    # 메소드(= 특정 클래스에서만 사용 가능한 함수)를 정의해줌.
    # 모든 메소드의 첫번째 호출 인자는 self(인스턴스 그 자체)여야 함.
    def run(self, raw):
        tokens = raw.split(" ")
        cmd, params = tokens[0], tokens[1:]

        # if cmd not in ["잔액", "동전"]:
        #     return "알 수 없는 명령입니다"
        if cmd == "잔액":
            return "잔액은 " + str(self._change) + "원입니다"
        elif cmd == "동전":
            coin = params[0]
            self._change += int(coin)
            return coin + "원을 넣었습니다"
        else:
            return "알 수 없는 명령입니다."
            pass


# change = 0
#
# # Test Isolation을 위한 함수
# def init():
#     global change
#     change = 0
#
# # Main Code
# def run(raw):
#     global change
#
#     tokens = raw.split(" ")
#     cmd, params = tokens[0], tokens[1:]
#
#     # if cmd not in ["잔액", "동전"]:
#     #     return "알 수 없는 명령입니다"
#     if cmd == "잔액":
#         return "잔액은 " + str(change) + "원입니다"
#     elif cmd == "동전":
#         coin = params[0]
#         change += int(coin)
#         return coin + "원을 넣었습니다"
#     else:
#         return "알 수 없는 명령입니다."
