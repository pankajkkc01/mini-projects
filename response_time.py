import time
import random
def measure_response_time():
    print("Get ready....")
    time.sleep(random.randint(2,5))
    start_time=time.time()
    input("press enter as soon as you see this message....")
    end_time=time.time()
    response_time=end_time-start_time
    print(f"your response time is {response_time:3f} seconds")
    
if __name__=="__main__":
    measure_response_time()