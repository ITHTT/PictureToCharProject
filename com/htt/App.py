import tkinter
from com.htt.ui.MainFrame import MainFrame


def showLocation(tk, w=600, h=400):
    screenWidth = tk.winfo_screenwidth()
    screenHeight = tk.winfo_screenheight()
    w=screenWidth//2
    h=screenHeight//2
    tk.geometry("{}x{}+{}+{}".format(w, h, (screenWidth - w) // 2, (screenHeight - h) // 2))


appUI = tkinter.Tk()
appUI.title("图片转字符图")
MainFrame(appUI)
showLocation(appUI)
appUI.resizable(False,False)
appUI.mainloop()
