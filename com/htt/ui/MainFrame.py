import os
from tkinter import *
import tkinter.filedialog

from PIL import Image, ImageTk


class MainFrame(Frame):
    topFrame:Frame
    addButton:Button
    createButton:Button


    def __init__(self,parent=None):
        super().__init__(parent)
        parent.rowconfigure(0, weight=1);
        parent.columnconfigure(0, weight=1)

        self.grid(row=0,column=0,sticky=NSEW)
        self.rowconfigure(1,weight=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1,weight=1)

        self.createWidgets()

    def createWidgets(self):
        #顶部操作按钮
        self.topFrame=Frame(self)
        self.topFrame.columnconfigure(0,weight=1)
        self.topFrame.columnconfigure(1,weight=1)
        self.topFrame.grid(row=0,column=0,columnspan=2,padx=15,pady=15,sticky=NSEW)

        self.addButton = Button(self.topFrame, text='添加图片',width=10,command=self.chooseImageFile)
        self.addButton.grid(row=0, column=0, columnspan=1,sticky=E,padx=50)

        self.createButton=Button(self.topFrame,text='生成图片',width=10,command=self.add)
        self.createButton.grid(row=0,column=1,columnspan=1,sticky=W,padx=50)

        #左侧输入图片区域
        self.leftFrame=Frame(self,bg='green')
        self.propagate(False)
        self.leftFrame.grid(row=1,column=0,columnspan=1,sticky=NSEW)
        self.leftLabelText=Label(self.leftFrame,text="添加的图片:")
        self.leftLabelText.pack(side=TOP,anchor=CENTER)

        self.leftLabelImage=Label(self.leftFrame)
        self.leftLabelImage.pack(padx=20,pady=20)



        self.rightFrame=Frame(self,bg='red')
        self.rightFrame.grid(row=1,column=1,columnspan=1,sticky=NSEW)
        #
        # self.imageLabel = Label(self.leftFrame)
        # self.imageLabel.pack(expand='true',fill='both')



    def chooseImageFile(self):
        default_dir = r"C:\Users\14683\Pictures"
        filePath:str=tkinter.filedialog.askopenfilename(title=u"选择文件",
                                                    filetypes=[("PNG", ".png"),(".jpg","JPG"),(".jpeg","JPEG")],
                                                   initialdir=(os.path.expanduser(default_dir)))

        print("leftFrameHeight:%s" % self.leftFrame.winfo_height())
        print("leftLabelTextHeight:%s" % self.leftLabelImage.winfo_height())


        if filePath.strip() is not "":
            openImage: Image = Image.open(filePath)
            w, h = openImage.size

            maxLabelW=self.leftFrame.winfo_width()-40
            maxLabelH=self.leftFrame.winfo_height()-self.leftLabelText.winfo_height()-40

            openImage.thumbnail((maxLabelW, maxLabelH))

            photoImage: ImageTk.PhotoImage = ImageTk.PhotoImage(openImage)
            self.leftLabelImage.config(image=photoImage)
            self.leftLabelImage.image = photoImage



    def add(self):
        pass




