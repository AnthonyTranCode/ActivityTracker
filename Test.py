import time

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime

try:
    while True:
        input()
        totalTime = round(time.time() - startTime, 2)
        print('Activity 1 %s' % (totalTime), end='')
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')







