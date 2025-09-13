# ตัวอย่าง minimal — เชื่อมกับ WiFi ของ Tello ก่อนรัน
import socket, threading, time

TELLO_IP = '192.168.10.1'
TELLO_CMD_PORT = 8889
LOCAL_CMD_PORT = 9000   # พอร์ต local ที่เราจะ bind เพื่อรับ response
STATE_PORT = 8890       # พอร์ตสำหรับฟัง telemetry

# command socket (send/receive ack)
cmd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cmd_sock.bind(('', LOCAL_CMD_PORT))

def cmd_receiver():
    while True:
        try:
            data, addr = cmd_sock.recvfrom(1024)
            print("Response:", data.decode('utf-8'))
        except Exception as e:
            print("cmd recv err", e)
            break
#สร้าง function ในการรับส่งข้อมูล
threading.Thread(target=cmd_receiver, daemon=True).start()

# state socket (telemetry)
state_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
state_sock.bind(('', STATE_PORT))

def state_receiver():
    while True:
        data, addr = state_sock.recvfrom(1024)
        print("STATE:", data.decode('utf-8').strip())

threading.Thread(target=state_receiver, daemon=True).start()

def send(cmd, wait=0.1):
    cmd_sock.sendto(cmd.encode('utf-8'), (TELLO_IP, TELLO_CMD_PORT))
    time.sleep(wait)

# ตัวอย่าง flow
send('command')
send('streamon')   # ถ้าจะรับวีดีโอ (ต้องเตรียม ffplay/decoder นอกโค้ดหรือใช้ ffmpeg)
send('takeoff')
time.sleep(5)
send('forward 50')
time.sleep(2)
send('land')

#อยากในการเขียนให้ง่ายกว่าไป EX_03