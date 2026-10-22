#This is an example of a retry loop

from time import sleep

TIMES = 5
BACKOFF = 5

print("Starting the retry loop...")
for attempt in range(TIMES):
    print(f"Attempt {attempt + 1} of {TIMES}")
    delay = BACKOFF*(attempt)
    print(f"sleeping for {delay} seconds before retrying...")
    #sleep(delay)
    for i in range(delay):
        if i%2 == 0:
            print("x", end="", flush = True)
        else:
            print("o", end="", flush = True)
        sleep(1)
        print("\b", end="", flush = True)
    print("Retrying now...")