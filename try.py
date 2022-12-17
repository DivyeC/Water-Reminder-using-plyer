import time

from datetime import datetime

from plyer import notification

from datetime import date

n = 1

if __name__ == "__main__":
    
    while True:
        
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        today = date.today()
        
        notification.notify(
            
        title = "PLEASE DRINK WATER NOW! ",
        
        message = """To prevent dehydration, You need to get plenty of water. Commonly recommend about 3 litres a day.""",
        
        app_icon =r'C:\Users\laksh\Desktop\water.ico',
        
        timeout=2,
        
        toast = True
        
        )

        if n==1:
            
            print("Program initiated on :",today, "  at :",current_time)
            
            n+=1
            
        else:
            
            print("Notification",n,"Displayed on :",today, "  at :",current_time)
            
            n+=1
        
        time.sleep(3600)
