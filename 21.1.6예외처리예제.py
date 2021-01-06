# 예외처리 예제
# 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# 출력메세지: "잘못된 값을 입력하였습니다."
# 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
# 치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
# 출력메세지: "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception):                  #사용자 정의에러 클래스 통하여 지정
    pass

chicken = 10
wait = 1
while(True):
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("몇 마리 주문하시겠습니까?:"))   #int로 감싸주어 입력값은 정수값만 받음 / 그 외의값은 자동 ValueError 발생
        if chicken < order:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError                    #1보다 작은값이 입력으로 들어올경우 ValueError 발생
        else:
            print("[대기번호 {0}] {1}마리 치킨이 주문되었습니다.".format(wait, order))
            wait += 1
            chicken -= order

        if chicken == 0:                            #치킨재고가 0일때의 사용자 정의에러 발생
            raise SoldOutError

    except ValueError:                      #ValueError 일때의 에러출력문
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:                    #SoldOutError 일때의 에러출력문
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break                       #프로그램 종료