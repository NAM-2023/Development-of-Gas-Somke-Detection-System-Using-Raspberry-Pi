from gpiozero import DigitalInputDevice   # 가스 센서를 입력 장치로 사용하기 위한 클래스 import
from gpiozero import OutputDevice         # 부저를 출력 장치로 사용하기 위한 클래스 import
import time                               # 시간 지연을 위한 time 라이브러리 import

bz = OutputDevice(18)                     # GPIO 18번 핀을 부저 제어용 출력으로 설정
gas = DigitalInputDevice(17)              # GPIO 17번 핀을 MQ-2 가스 센서 입력으로 설정

try:
    while True:                           # 무한 반복 루프 시작 (지속적으로 센서 상태 확인)
        if gas.value == 0:                # 센서 출력이 LOW(0)이면 가스가 감지된 상태
            print("가스감지됨")           # 터미널에 가스 감지 메시지 출력
            bz.on()                       # 부저 ON (경고음 발생)
        else:                             # 센서 출력이 HIGH(1)이면 정상 상태
            print("정상")                 # 터미널에 정상 상태 메시지 출력
            bz.off()                      # 부저 OFF (소리 중지)

        time.sleep(0.2)                   # 0.2초 간격으로 센서 값을 반복 확인

except KeyboardInterrupt:                 # Ctrl+C 입력 시 프로그램 종료 처리
    pass                                  # 별도 동작 없이 종료

bz.off()                                  # 프로그램 종료 시 부저를 OFF 상태로 설정



