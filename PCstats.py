import psutil
from pypresence import Presence
import time

client_id = ''  # 디스코드 개발자, 봇 아이디 입력
RPC = Presence(client_id,pipe=0)
RPC.connect() # Start the handshake loop


while True:
    cpu_per = round(psutil.cpu_percent(),1)
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    print(RPC.update(details="CPU: "+str(cpu_per)+"%", state="RAM: "+str(mem_per)+"%"))  # Set the presence
    time.sleep(15) # 새로고침 시간
