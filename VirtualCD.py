from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from ui.mainw import Ui_MainWindow
import os, json
import subprocess

class VirtualCD_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(VirtualCD_Window, self).__init__()
        self.setupUi(self)
        self.setWindowOpacity(0.5)
        self.setWindowFlags(Qt.Qt.WindowCloseButtonHint | Qt.Qt.WindowMinimizeButtonHint | Qt.Qt.WindowStaysOnTopHint)
        self.wHeight = self.height()
        _result = subprocess.getstatusoutput('losetup -J')
        # print(_result)
        _loaded = False
        self._vcd_list = {}
        if _result[0] == 0:
            if _result[1] != '':
                self._vcd_list = json.loads(_result[1])
                # print(self._vcd_list)
                _loaded = True
                # print(_result[1].split('\n')[1])
        # print(_result)
        # print(type(_result))
        # print(_loaded)
        self.btnEject.setEnabled(_loaded)
        self.btnOpen.clicked.connect(self.loadISO)
        self.btnEject.clicked.connect(self.unloadISO)


    def loadISO(self):
        iso_file, file_type = QtWidgets.QFileDialog.getOpenFileName(self, caption='选择ISO文件', filter='光盘镜像文件(*.iso)')
        # print(iso_file, file_type)
        if iso_file != '':
            # print(f'选择文件为{iso_file}')
            result = subprocess.getstatusoutput(f'losetup -r /dev/loop0 {iso_file}')
            if result[0] != 0:
                result = subprocess.getstatusoutput(f'gksudo -m 加载虚拟光驱需要输入当前用户的密码才能继续 "losetup -r /dev/loop0 {iso_file}"')
            # print(result[0])
            if result[0] == 0:
                self.btnEject.setEnabled(True)
                _result = subprocess.getstatusoutput('losetup -J')
                self._vcd_list = json.loads(_result[1])
                # print(self._vcd_list)
            else:
                QtWidgets.QMessageBox.warning(self, '警告', f'文件"{iso_file}"加载失败！')
        # else:
            # print('没有选择任何文件')

    def unloadISO(self):
        iso_filename = os.path.basename(self._vcd_list['loopdevices'][0]['back-file'])
        iso_mnt_path = '/media/' + os.environ['USER'] + '/' +iso_filename[:iso_filename.rfind('.')]
        # print('iso filename', iso_filename, iso_mnt_path)
        if os.path.exists(iso_mnt_path):
            result = subprocess.getstatusoutput(f'umount {iso_mnt_path}')
            # print(result)
        result = subprocess.getstatusoutput('losetup -d /dev/loop0')
        # print(result)
        if result[0] != 0:
            result = subprocess.getstatusoutput('gksudo -m 弹出虚拟光驱需要输入当前用户的密码才能继续 "losetup -d /dev/loop0"')
            # print(result)
        if result[0]==0:
            self.btnEject.setEnabled(False)
        else:
            QtWidgets.QMessageBox.warning(self, '警告', '虚拟光驱弹出失败！')




if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainw = VirtualCD_Window()
    x = (app.desktop().width() - mainw.width()) / 2
    y = (app.desktop().height() - mainw.height()) / 2
    mainw.move(x, y)
    mainw.show()
    sys.exit(app.exec_())

