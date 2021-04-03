# 로그를 기록하는 기능을 데코레이터로 만들기

import datetime
import time

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs)
        )
        return original_function(*args, **kwargs)

    return wrapper

@my_logger
def display_infoInLogger(name, age):
    time.sleep(1)
    print('display_infoInLogger({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_infoInLogger('John', 251)