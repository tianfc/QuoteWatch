import os
import tkinter as tk
from datetime import datetime
 
import requests
 
 
def search(gp_dm):
    # tx接口
    res = ""
    for i in gp_dm:
        url = f'http://qt.gtimg.cn/q={i}'
        resp = requests.get(url)
        name = resp.text.split('~')[1]
        price = resp.text.split('~')[3]
        fl = resp.text.split('~')[32]
        res += f"{name} {price} {fl}%\n"
    return res
 
 
a1 = datetime.strptime('09:15:00', '%H:%M:%S').time()
a2 = datetime.strptime('11:30:00', '%H:%M:%S').time()
 
p1 = datetime.strptime('13:00:00', '%H:%M:%S').time()
p2 = datetime.strptime('15:00:00', '%H:%M:%S').time()
 
 
def main():
    # 工作日
    tod = datetime.now().weekday()
 
    if 0 <= tod <= 4:
        # 开市时间
        s = datetime.now().time()
 
        if s.__lt__(a1):
            dt = datetime.now().strftime("%Y/%m/%d")
            st = datetime.strptime(f'{dt} 09:15:00', '%Y/%m/%d %H:%M:%S') - datetime.now()
            return f"{st.seconds}秒后开市\n" + search(gp_list)
        elif s.__ge__(a1) and s.__le__(a2):
            return f"{datetime.now().strftime('%H:%M:%S')}\n" + search(gp_list)
        elif s.__gt__(a2) and s.__lt__(p1):
            dt = datetime.now().strftime("%Y/%m/%d")
            st = datetime.strptime(f'{dt} 13:00:00', '%Y/%m/%d %H:%M:%S') - datetime.now()
            return f"{st.seconds}秒后开市\n" + search(gp_list)
        elif s.__ge__(p1) and s.__le__(p2):
            return f"{datetime.now().strftime('%H:%M:%S')}\n" + search(gp_list)
        elif s.__gt__(p2):
            return '今天已休市\n' + search(gp_list)
    else:
        return '今天休市\n' + search(gp_list)
 
 
def showtime():
    """
    定时展示res内容
    :return:
    """
    res = main().strip()
    lb.config(text=str(res))
    lb.after(2000, showtime)
 
 
def tk_exit(event):
    """
    退出函数
    :param event:
    :return:
    """
    # 1.关闭窗口
    root.destroy()
 
 
# def on_resize(evt):
#     root.configure(width=evt.width, height=evt.height)
#     cv.create_rectangle(0, 0, cv.winfo_width(), cv.winfo_height(), fill="gray", outline="gray")
#     print(cv.winfo_width())
 
class FloatingWindow:
    """
    移动窗口
    """
 
    def __init__(self, rt):
        self.rt = rt
        self.x = 0
        self.y = 0
 
        # 设置按键
        lb.bind("<ButtonPress-1>", self.start_move)
        lb.bind("<ButtonRelease-1>", self.stop_move)
        lb.bind("<B1-Motion>", self.on_motion)
 
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
 
    def stop_move(self, event):
        self.x = None
        self.y = None
 
    def on_motion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.rt.winfo_x() + deltax
        y = self.rt.winfo_y() + deltay
        self.rt.geometry("+%s+%s" % (x, y))
 
 
def validate_file():
    """
    校验配置文件是否存在，存在则读取
    :return:
    """
    # 校验是否存在代码配置文件
    if not os.path.exists('./config.txt'):
        assert False, "请在本程序下配置config.txt文件，内容为股票代码，多个代码用换行隔开"
 
    # 读取代码配置
    temp_gp_list = []
    f = open('./config.txt', 'r')
    for line in f:
        temp_code = line.strip()
        if temp_code[0].isalpha():  # 自行配置sz/sh开头，直接读取，注意要用小写
            temp_gp_list.append(temp_code)
        elif temp_code:
            if temp_code.startswith('60') or temp_code.startswith('688'):
                gp_code = f'sh{temp_code}'
            elif temp_code.startswith('83') or temp_code.startswith('87') or temp_code.startswith('88') or temp_code.startswith('920'):
                gp_code = f'bj{temp_code}'
            elif temp_code.startswith('30'):
                gp_code = f'sz{temp_code}'
            else:
                gp_code = f'sz{temp_code}'
            temp_gp_list.append(gp_code)
    if len(temp_gp_list) < 1:
        assert False, "config文件未配置股票代码"
 
    # 校验是否存在ui配置文件
    get_ui_config = {}
    if os.path.exists('./ui.txt'):
        f = open('./ui.txt', 'r', encoding='utf-8')
        for line in f:
            shuxing, value = line.strip().split('：')
            get_ui_config[shuxing] = value
 
    return temp_gp_list, get_ui_config
 
 
if __name__ == '__main__':
    # 读取代码配置
    gp_list, ui_config = validate_file()
    # GUI
    root = tk.Tk()
    root.overrideredirect(True)  # 无标题栏窗体
    # 透明度
    root.attributes('-alpha', int(ui_config.get('透明度'))/100 if ui_config.get('透明度') else 0.2)
 
    width = 150
    height = 5 + 16 * (len(gp_list) + 1)
    screen_width = root.winfo_screenwidth()
    x = int((screen_width - width) / 2)
    # screen_height = root.winfo_screenheight()
    # y = int(screen_height - height - 75)
    root.geometry(f'{width}x{height}+0+0')
    root.attributes("-topmost", 1)
 
    root.wm_attributes("-transparentcolor", "gray")
    root.bind("<ButtonRelease-3>", tk_exit)
 
    lb = tk.Label(root)
    lb.pack(fill='both', side='top')
    showtime()
    root.floater = FloatingWindow(root)
    root.mainloop()