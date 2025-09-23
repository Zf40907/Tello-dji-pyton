# 🚀 Tello – DJI – Python

โดรน (Drone) เป็นเทคโนโลยีที่ฮอตสุด ๆ ในตอนนี้ ทั้งการศึกษา การถ่ายภาพ และงานวิจัย โดยเฉพาะ **Tello** ของ Ryze Tech (ร่วมกับ DJI และ Intel) ที่ออกแบบมาเพื่อ **เรียนรู้การบินและเขียนโปรแกรมควบคุมโดรน**  

Python ด้วยความง่ายและไลบรารีเพียบ ทำให้เราเขียนโค้ดควบคุม Tello ได้ตรง ๆ แบบ Developer สาย Tech  

---

## 🛸 DJI Tello – Quick Specs

![DJI Tello](https://www.dji.com/tello/info#downloads)  
- น้ำหนักเบา ~80 กรัม  
- กล้อง HD 720p  
- ควบคุมได้ทั้ง **Smartphone / Wi-Fi / Python**  
- Vision Positioning System → บินนิ่งในร่ม  
- Perfect สำหรับ **Education & Experimentation**

---

## 🐍 Python + Tello (djitellopy)

ไลบรารี **[djitellopy](https://github.com/damiafuentes/DJITelloPy)** ทำให้เราสั่ง Tello ง่าย ๆ  
- Takeoff / Land  
- RC Control (x, y, z, yaw)  
- Video Streaming  
- Sensor Data Feedback  

### ตัวอย่างโค้ดเบื้องต้น

```python
from djitellopy import Tello
import time

# สร้าง Object ของ Tello
tello = Tello()
tello.connect()

print("🔋 Battery:", tello.get_battery())

# เปิด Video Stream
tello.streamon()

# 🚀 Takeoff
tello.takeoff()
time.sleep(3)

# ✈️ บินไปข้างหน้า 50 cm
tello.send_rc_control(0, 50, 0, 0)
time.sleep(2)

# 🛬 Land
tello.land()

