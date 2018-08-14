from vm import run, init


# 최초의 잔액 테스트
def test_initial_change_sholud_be_zero():
    init()
    assert "잔액은 0원입니다" == run("잔액")

# 동전을 넣으면 잔액이 올라가는가?
def test_insert_coin_and_check():
    init()
    assert "100원을 넣었습니다" == run("동전 100")
    assert "잔액은 100원입니다" == run("잔액")

# 동전을 두 번 넣으면 잔액이 그만큼 올라가는가?
def test_accumulation_of_change():
    init()
    run("동전 100")
    run("동전 100")
    assert "잔액은 200원입니다" == run("잔액")

# 잔액/동전 외의 명령어를 넣으면 "알 수 없는 명령입니다."가 나오는가?
def test_unknown():
    init()
    assert "알 수 없는 명령입니다." == run("달러")
    assert "알 수 없는 명령입니다." == run("돈내놔")
