import time, sys
indent=0
increasing = True
try:
    while True:
        print(' '*indent, end='')
        print('*********************************')
        time.sleep(0.01)
        if increasing:
            indent+=1
            if indent==50:
                increasing=False
        else:
            indent-=1
            if indent==25:
                increasing=True

except KeyboardInterrupt:
    sys.exit()