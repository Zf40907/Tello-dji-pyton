from djitellopy import Tello
import time

#from djitellopy import Tello
#import time เอาการจัดการเวลาเข้ามาช่วย
#djitellopy = ไลบรารี Python ที่เป็น wrapper สำหรับ Tello SDK (จัดการ UDP ให้เรา)
#time = เอาไว้ใส่ sleep() เพื่อหน่วงเวลา

t = Tello()
t.connect()          # ต้องเชื่อม Wi-Fi ของ Tello แล้ว
print("Battery:", t.get_battery()) 
t = Tello()
t.connect()          # ต้องเชื่อม Wi-Fi ของ Tello แล้ว
print("Battery:", t.get_battery())
#Tello() → สร้าง object ของโดรน
#t = Tello()
#T.connect()          # ต้องเชื่อม Wi-Fi ของ Tello แล้ว
#print("Battery:", t.get_battery())
#Tello() → สร้าง object ของโดรน
#connect() → เปิด socket UDP → ส่ง "command" ไปยัง Tello → เข้าสู่ SDK mode
#get_battery() → ขอค่าแบตเตอรี่ (%) จากโดรน → เอามา print

t.takeoff()
time.sleep(3)
t.send_rc_control(0, 50, 0, 0)  # vx vy vz yaw (ตัวอย่าง)
time.sleep(2)
##t.land()
#t.streamon()
#frame_read = t.get_frame_read()  # background frame reader (ให้ OpenCV เอาไปใช้ได้)
#streamon() → บอกให้ Tello เปิด video stream (ส่ง H.264 มาทาง UDP port 11111)
#get_frame_read() → สร้าง thread พิเศษที่ อ่านภาพจาก stream ตลอดเวลา


