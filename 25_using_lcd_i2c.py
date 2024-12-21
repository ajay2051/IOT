import LCD1602
import time

LCD1602.init(0*27, 1)
# lcd = LCD1602.lcd()
try:
    while True:
        LCD1602.write(0, 0, "Hello world") # column 0, row 0
        LCD1602.write(0, 1, "Welcome..")

except KeyboardInterrupt:
    time.sleep(0.5)
    LCD1602.clear()
    print("Closing LCD1602...")