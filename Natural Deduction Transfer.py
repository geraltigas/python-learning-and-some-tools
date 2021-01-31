import pyperclip
while True:
    a = input("typein the string to be format:")
    a = a.replace("js","Γ")
    a = a.replace("dl","┠")
    a = a.replace("ji","∧")
    a = a.replace("bi","∨")
    a = a.replace("yh","→")
    a = a.replace("dj","↔")
    a = a.replace("cz","∃")
    a = a.replace("sy","∀")
    a = a.replace("fe","┓")
    pyperclip.copy(a)
    i = input("")