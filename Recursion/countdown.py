import time
def count(seg):
    print(seg)

    time.sleep(3)


    if seg == 3:
        return 0
    else:
        return count(seg-1)