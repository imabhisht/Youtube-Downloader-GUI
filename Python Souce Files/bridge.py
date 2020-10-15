from PyQt5 import QtWidgets, QtCore , QtGui 
import os
from gui import Ui_MainWindow
import backend
import time
class  Window(QtWidgets.QMainWindow,Ui_MainWindow):
        context = None


        def __init__(self):

            Window.context = self
            super().__init__()
            self.setupUi(self)
            self.show()
            self.message_credit()


            #Button Pressed Event
            self.download.pressed.connect(self.download_check)
            self.url_check.pressed.connect(self.checking_url)
            self.pushButton.pressed.connect(self.browser_location)
            
        global title_video

        def download_check(self):
            try:
                self.start_download()
            except:
                self.errrormessage_pass()

        def errrormessage_pass(self):
            
            emsg = QtWidgets.QMessageBox(self)
            emsg.setWindowModality(QtCore.Qt.WindowModal)
            self.Current_Status_Update("Waiting for Correct Values.")
            msg="Not able to Download. \n\nFill all the Boxes Correctly. Be sure to check the Link and Select the Quality."
            emsg.setText(msg)
            emsg.setIcon(emsg.Critical)
            emsg.setWindowTitle("Incorrect Values")
            emsg.exec_()
            return

        def browser_location(self):
            global path_save
            path_save = QtWidgets.QFileDialog.getExistingDirectory()
            path_save = path_save + "/"
            self.lineEdit_2.setText(path_save)

        def Current_Status_Update(self,text_update):
            self.label_4.setFont(QtGui.QFont("Miriam", 11))
            self.label_4.setText("Current Status: "+ text_update)
        
        def message_pass(self,msg):
            
            emsg = QtWidgets.QMessageBox(self)
            emsg.setWindowModality(QtCore.Qt.WindowModal)


            emsg.setText(msg)
            emsg.setIcon(emsg.Information)
            emsg.setWindowTitle("Sucessful")
            emsg.exec_()
            self.clear_program()

        def message_credit(self):
            
            emsg = QtWidgets.QMessageBox(self)
            emsg.setWindowModality(QtCore.Qt.WindowModal)

            msg = "Thanks for using this Application.For more Cool Stuffs & Source Code, Check my other Repositories on GitHub!! [https://github.com/imabhisht]\n\t\t\t\t\t\t\t\t\t-Abhisht"
            emsg.setText(msg)
            emsg.setIcon(emsg.Information)
            emsg.setWindowTitle("Startup Message")
            emsg.exec_()

        def checking_url(self):
            global url
            global check
            check = 0
            url = self.lineEdit.text()
            alpha = backend.check_url(url)
            if alpha == "correct":
                self.label_5.setText("")
                self.label_6.setPixmap(QtGui.QPixmap("Resources/tick.png"))
                list_rev = backend.get_resolutions()
                self.quality_enable_control(list_rev)
                metdata = backend.metadata()
                self.get_metdata(metdata)
                self.lineEdit_2.clear()
                check = 1
                
            else:
                self.label_5.setText("Check Internet Connection or Insert valid link")
                self.label_6.setPixmap(QtGui.QPixmap("Resources/wrong.png"))

        def quality_enable_control(self,list_rev):
            if "1080p" in list_rev:
                self.comboBox.model().item(1).setEnabled(True)
            if "720p" in list_rev:
                self.comboBox.model().item(2).setEnabled(True)
            if "480p" in list_rev:
                self.comboBox.model().item(3).setEnabled(True)
            if "360p" in list_rev:
                self.comboBox.model().item(4).setEnabled(True)
            if "240p" in list_rev:
                self.comboBox.model().item(5).setEnabled(True)
            if "144p" in list_rev:
                self.comboBox.model().item(6).setEnabled(True)
 

        def get_metdata(self,metdata):
            global title_video
            title_video = metdata[0]
            self.preview_image.setPixmap(QtGui.QPixmap(r"Cache\local_image.jpg"))
            self.title_preview.setFont(QtGui.QFont("Miriam", 11))
            self.title_preview.setText("Title: " + metdata[0])
            self.publisher_preview.setFont(QtGui.QFont("Miriam", 11))
            self.publisher_preview.setText("Author: "+metdata[1])
            self.views_preview.setFont(QtGui.QFont("Miriam", 11))
            self.views_preview.setText("Views : "+str(metdata[2]))
            self.size_preview.setFont(QtGui.QFont("Miriam", 11))
            self.size_preview.setText("Length : "+str(metdata[3]))
            self.Current_Status_Update("Ready to Download")

        def clear_program(self):
            self.Current_Status_Update("Waiting for Next Video")
            self.label_6.setPixmap(QtGui.QPixmap("Resources/white.png"))
            self.label_5.setText("Inset New Link")
            self.comboBox.setCurrentIndex(0)
            self.label_4.setText("Current Status: ")
            self.lineEdit_2.clear()
            self.lineEdit.clear()
            self.preview_image.setPixmap(QtGui.QPixmap("Resources/white.png"))
            self.title_preview.setText("Title: ")
            self.publisher_preview.setText("Author: ")
            self.views_preview.setText("Views: ")
            self.size_preview.setText("Length: ")
            self.progressBar.setValue(0)

        def start_download(self):

            cout = 0
            while cout < 15:
                self.progressBar.setValue(cout)
                cout+=1

            self.Current_Status_Update("Current Status: Downloading Video & Audio") 
            rev = self.comboBox.currentText()
            backend.download(rev)
            while cout < 60:
                self.progressBar.setValue(cout)
                cout+=1
            self.Current_Status_Update("Current Status: Merging into one File...")
            print("Downloaded Source Files...Going for Converting")
            backend.compiling_files(path_save)
            while cout < 99:
                self.progressBar.setValue(cout)
                cout+=1
            self.message_pass("The Video " + title_video + " has been Successfully Downloaded!!\n\n Thanks for using!!")
            self.clear_program()
            
            