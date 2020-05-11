import time
from time import time as my_timer, perf_counter as my_perf_timer, monotonic as my_mono_timer
import random

# epoch: start time, tuple
print(time.gmtime(0))
# now: local time, tuple
print(time.localtime())
# now: epoch in ms
# OR
#  my_timer()
print(time.time())
print()

#
wait_time = random.randint(1, 6)
# wait between 1 to 6 ms
time.sleep(wait_time)
# current ms
# perf_counter most accurate
# monotonic for day light saving
start_time = my_timer()  # my_mono_timer()  # my_perf_timer()
input("Press enter to stop")
end_time = my_timer()  # my_mono_timer()  # my_perf_timer()

print("Started at "+time.strftime("%X", time.localtime(start_time)))
print("Ended at "+time.strftime("%X", time.localtime(end_time)))

print("Lapsed time was between your reaction was {}".format(end_time-start_time))
