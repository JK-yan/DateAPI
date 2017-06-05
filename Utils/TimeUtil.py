import time


def timestamp(format_time='%Y-%m-%d %H:%M:%S'):

    """
    获取当前时间
    :return:
    """
    return time.strftime(format_time, time.localtime(time.time()))

if __name__ == '__main__':
    aa = '%Y-%m-%d %H:%M:%S'
    print('%s' % timestamp(aa))

    print(timestamp())
