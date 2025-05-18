import pyperclip
import re
with open("cfg/Custom_Clash.ini", 'r', encoding="utf-8") as f:
    s = f.read()
s = re.sub("[\U0001F300-\U0001F6FF] ", "", s, flags=re.UNICODE)
s = re.sub("♻️ ", "", s, flags=re.UNICODE)
s = re.sub("🤖 ", "", s, flags=re.UNICODE)
s = re.sub("Ⓜ️ ", "", s, flags=re.UNICODE)
s = re.sub("(?:[\U0001F1E6-\U0001F1FF]){2} ", "", s, flags=re.UNICODE)
s = re.sub("🇬 ", "", s, flags=re.UNICODE)
sL = s.split("\n")
for i in sL[:]:
    if "custom_proxy_group=手动选择" in i:
        print(i.replace("手动选择", "节点选择"))
pyperclip.copy("[]节点选择`")

with open("cfg/Custom_Clash.ini", 'w', encoding="utf-8") as f:
    f.write(s)
