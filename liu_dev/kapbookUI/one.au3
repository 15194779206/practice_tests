ControlFocus("文件上传", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("文件上传", "", "Edit1", "C:\Users\lenovo\Desktop\图片\1.jpg")
Sleep(2000)
ControlClick("文件上传", "","Button1");