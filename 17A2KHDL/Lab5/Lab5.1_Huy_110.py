import time

class SimpleTask:
    def execute_task(self):
        for i in range(1, 11):
            print('Đã in lần thứ:', i)
            time.sleep(2)  
            
def main():
    task = SimpleTask()
    task.execute_task()

if __name__ == "__main__":
    main()