# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 stop -> 다른 작업으로 위임 -> stop 지점부터 재실행 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO
# 순차 실행

import timeit
from urllib.request import urlopen

urls = ['http://daum.net','https://google.com','https://apple.com','https://tistory.com','https://github.com','https://gmarket.co.kr']

start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print('Start',url)
    # 실제 요청
    text = urlopen(url)
    # print('Contents',text.read())
    print('Done',url)

# 완료시간 - 시작시간
duration = timeit.default_timer() - start
print(f'Total time: {duration}')
