print("本程序使用牛顿切线法求多项式根。")
func = input("请输入表达式：")
orix = float(input("请输入初始值："))
def tocodeobject(func):
    func = func.replace("^","**")
    returnstring ="def f(x): return " + func
    return compile(returnstring,"","exec")
exec(tocodeobject(func))
for i in range(100000):
    tupl = [orix-0.00000001,orix+0.00000001]
    deltay = f(tupl[1]) - f(tupl[0])
    secf = deltay/0.00000002
    orix = -f(orix)/secf + orix
print(orix)
input()

