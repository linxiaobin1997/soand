from mainUI import Ui_MainWindow
from PyQt5 import QtWidgets

from PyQt5.QtCore import QStringListModel,QThread,pyqtSignal

import sys
import os
import pyperclip


from concurrent.futures import ThreadPoolExecutor

class main_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    #init thread Pool
    executor = ThreadPoolExecutor(max_workers = 5)

    listViewFlag = 1
    listViewNames_1 = []
    listViewUrls_1 = []

    listViewNames_2 = []
    listViewUrls_2 = []
    videoName = ''

    downloadThreadNum = 0
    download_dict = {}


    def __init__(self,parent=None):
        super(main_ui,self).__init__(parent)
        self.setupUi(self)
        # self.setStyleSheet("#MainWindow{background-color:black}")
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_series.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.pushButton_search.clicked.connect(self.search)
        self.listView.doubleClicked.connect(self.showSeries)
        self.listView_series.doubleClicked.connect(self.playByDoubleClicked)
        self.pushButton_play.clicked.connect(self.playByPlayButton)
        self.pushButton_copyUrl.clicked.connect(self.copyUrl)
        self.pushButton_download.clicked.connect(self.download)


    def keyReleaseEvent(self,event, *args, **kwargs):
        print("press ")
        print(event.key())
        #Enter
        if event.key() == 16777220:
            self.search()


    def download(self):
        selectedUrl = self.listViewUrls_2[self.listView_series.currentIndex().row()]
        selectedSeries = self.listViewNames_2[self.listView_series.currentIndex().row()].split('$')[0]
        selectedName = self.videoName
        fileName1 = './mydownload'
        fileName2 = fileName1+'/'+selectedName
        fileName3 = fileName2+'/'+selectedSeries+'.'+selectedUrl.split('.')[-1]


        if os.path.exists(fileName1)==0:
            os.mkdir(fileName1)
        if os.path.exists(fileName2)==0:
            os.mkdir(fileName2)
        if len(self.download_dict)>=5:
            amb = autoMessageBox()
            amb.setText('can not download 5 item at the same time')
            amb.setStandardButtons(QtWidgets.QMessageBox.Ok)
            amb.autoClose = True
            amb.timeout = 3
            amb.exec()
            return
        if selectedUrl in self.download_dict.keys():
            amb = autoMessageBox()
            amb.setText('this item is downloading')
            amb.setStandardButtons(QtWidgets.QMessageBox.Ok)
            amb.autoClose = True
            amb.timeout = 3
            amb.exec()
            return
        self.dlt = DownLoadThread(selectedUrl,fileName3)
        self.dlt.downDone.connect(self.reduceDlt)
        self.dlt.downError.connect(self.downloadError)
        self.dlt.start()
        self.download_dict[selectedUrl] = fileName3
        # self.downloadThreadNum +=1

    def downloadError(self,error,url,dst):
        self.download_dict.pop(url)
        amb = autoMessageBox()
        amb.setText('down Error!\n'+error+'\nin: '+url)
        amb.setStandardButtons(QtWidgets.QMessageBox.Ok)
        amb.autoClose = True
        amb.timeout = 100
        amb.exec()

    def reduceDlt(self,url,dst):
        #reduce downloadThread num
        self.download_dict.pop(url)
        amb = autoMessageBox()
        amb.setText('download finshed')
        amb.setStandardButtons(QtWidgets.QMessageBox.Ok)
        amb.autoClose = True
        amb.timeout = 10
        amb.exec()



    def copyUrl(self):
        selected = self.listView_series.selectedIndexes()
        for i in selected:
            pyperclip.copy(self.listViewUrls_2[i.row()])
            # QtWidgets.QMessageBox.information(self,'tips','copy to clipboard')
            # self.th3 = Thread3()
            # self.th3.start()
            amb = autoMessageBox()
            amb.setText('copy to clipboard')
            amb.setStandardButtons(QtWidgets.QMessageBox.Ok)
            amb.autoClose = True
            amb.timeout = 1
            amb.exec()





    def playByPlayButton(self):
        if self.comboBox_way.currentIndex() == 0:
            print("play")
            # win32api.ShellExecute(0,'open','.\\potplayerlsb\\PotPlayer_1.7.19722\\PotPlayerMini.exe',self.listViewUrls_2[qModelindex.row()],'',1)
            os.system('start .\\potplayerlsb\\PotPlayer_1.7.19722\\PotPlayerMini.exe '+self.listViewUrls_2[self.listView_series.currentIndex().row()])
            print("end")

        elif self.comboBox_way.currentIndex() ==1:
            print("play")
            # win32api.ShellExecute(0,'open',self.listViewUrls_2[qModelindex.row()],'','',1)
            os.system('start '+self.listViewUrls_2[self.listView_series.currentIndex().row()])


    def playByDoubleClicked(self,qModelindex):
        if self.comboBox_way.currentIndex() == 0:
            print("play")
            # win32api.ShellExecute(0,'open','.\\potplayerlsb\\PotPlayer_1.7.19722\\PotPlayerMini.exe',self.listViewUrls_2[qModelindex.row()],'',1)
            os.system('start .\\potplayerlsb\\PotPlayer_1.7.19722\\PotPlayerMini.exe '+self.listViewUrls_2[qModelindex.row()])
            print("end")

        elif self.comboBox_way.currentIndex() ==1:
            print("play")
            # win32api.ShellExecute(0,'open',self.listViewUrls_2[qModelindex.row()],'','',1)
            os.system('start '+self.listViewUrls_2[qModelindex.row()])


    def showSeries(self,qModelindex):
        print('showSeries')
        self.videoName = self.listViewNames_1[qModelindex.row()]
        self.th2 = Thread2(self.listViewUrls_1[qModelindex.row()])
        self.th2.threadout.connect(self.showUrls)
        self.th2.start()


    def search(self):
        print("search")
        print(self.lineEdit_search.text())

        #new Thread

        self.th1 = Thread1(self.lineEdit_search.text())
        self.th1.threadout.connect(self.showlistView)

        self.th1.start()
        print('search wait')


    def showlistView(self,names,urls):
        print('show listview')
        self.listViewNames_1 = names
        self.listViewUrls_1 = urls
        # print(self.listViewNames_1)
        slm = QStringListModel(self.listView)
        slm.setStringList(self.listViewNames_1)
        self.listView.setModel(slm)

    #     # self.listViewFlag = 1
    def showUrls(self,names,urls):
        print('show urls')
        self.listViewNames_2 = names
        self.listViewUrls_2 = urls
        slm = QStringListModel(self.listView_series)
        slm.setStringList(self.listViewNames_2)
        self.listView_series.setModel(slm)

class Thread1(QThread):
    threadout = pyqtSignal(list,list)
    def __init__(self,searchword):
        super().__init__()
        self.searchword = searchword
    def run(self):
        names,urls = tool().searchPost(self.searchword)
        self.threadout.emit(names,urls)
class Thread2(QThread):
    threadout = pyqtSignal(list,list)
    def __init__(self,url):
        super().__init__()
        self.url = url
    def run(self):
        names,urls = tool().getSeries(self.url)
        self.threadout.emit(names,urls)
class Thread3(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        amb = autoMessageBox()
        amb.setText('copy to clipboard')
        amb.setStandardButtons(QtWidgets.QMessageBox.Ok)
        amb.autoClose = True
        amb.timeout = 3
        amb.exec()
class DownLoadThread(QThread):
    downError = pyqtSignal(str,str,str)
    downDone = pyqtSignal(str,str)
    def __init__(self,url,dst):
        super().__init__()
        self.url = url
        self.dst = dst
    def run(self):
        try:
            tool().download_from_url(self.url, self.dst)
        except Exception as e:
            self.downError.emit(e,self.url,self.dst)
            return
        self.downDone.emit(self.url,self.dst)





class tool(object):
    def searchPost(self,searchword):
        print("searchPost in thread1")
        print("search "+searchword)
        import requests
        import re
        url = 'http://www.kuyunzy1.com/search.asp'
        try:
            data = {'searchword':searchword.encode('gbk')}
            response = requests.post(url,data)
            response.encoding='gbk'
        except Exception as e:
            print(e)
            return None,None
        urls = re.compile('(/detail/\?\d*?.html)').findall(response.text)
        names = re.compile('target="_blank">(.*?)</a></td>').findall(response.text)
        urls = ['http://www.kuyunzy1.com'+x for x in urls]
        # return {'names':names,'urls':urls}
        # self.listViewNames_1 = names
        # self.listViewUrls_1 = urls
        print(names)
        return names,urls
    def getSeries(self,url):
        import requests
        import re
        print("get :" + url)
        html = requests.get(url)
        html.encoding = 'gbk'
        names = re.compile('<a>(.*?)</a><!--.*?-->').findall(html.text)
        urls = [x.split('$')[1] for x in names]
        return names,urls
    def download_from_url(self,url,dst):
        import requests
        if url.split('.')[-1] not in ['mp4','m3u8']:
            print('this type not support download')
            return 0
        print("download")
        print(url)
        print(dst)
        response = requests.get(url,stream=True)
        file_size = int(response.headers['content-length'])
        if os.path.exists(dst):
            first_byte = os.path.getsize(dst)
        else:
            first_byte = 0

        if first_byte>=file_size:
            return file_size

        header = {'Range':f"bytes={first_byte}-{file_size}"}
        # pbar = tqdm.tqdm(total=file_size,
        #             initial=first_byte,
        #             unit='B',
        #             unit_scale=True,
        #             desc=dst)
        req = requests.get(url,headers=header,stream=True)
        with open(dst,'ab') as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    # pbar.update(1024)
        # pbar.close()
        return file_size

class autoMessageBox(QtWidgets.QMessageBox):
    timeout = 0
    autoClose = False
    currentTime = 0
    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoClose:
            self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        print(self.currentTime)
        self.currentTime+=1
        if self.currentTime<=self.timeout:
            self.done(0)











if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    m = main_ui()
    m.show()
    app.exec_()
