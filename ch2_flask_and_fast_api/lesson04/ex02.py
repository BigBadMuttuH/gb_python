import time


def slow_function():
    print('start function')
    time.sleep(5)
    print('end function')


print('start slow function')
slow_function()
print('end slow function')
