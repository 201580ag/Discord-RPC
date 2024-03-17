from pypresence import Presence
import time

client_id = "" # 디스코드 개발자, 봇 아이디 입력
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        large_image = "", # 사용자 이미지(디스코드 봇 개발자 512x512)
        small_image = "", # 사용자 이미지(디스코드 봇 개발자 512x512)
        large_text = "이걸 찾다니.. 대단하네(Easter egg)",
        small_text = "이것도 찾아?(Easter egg)",
        details = "I'm ROST Developer",
        state = "My favorite language is C++, Python",
        buttons = [{"label": "MY GITHUB", "url": "https://www.github.com/201580ag"},
                    {"label": "MY GIST", "url": "https://gist.github.com/201580ag"}]
    )
    time.sleep(1)
