# coding: utf-8
"""アセット出力ツールのGUIクラス

name: kmt_export_gui

"""

import os
import sys
import subprocess

from PySide2.QtGui import*
from PySide2.QtCore import*
from PySide2.QtWidgets import*

from maya import OpenMayaUI
from shiboken2 import wrapInstance

from kmt_tool.kmt_export import kmt_import_json
from kmt_tool.kmt_export import kmt_maya_module
from kmt_tool.kmt_export import kmt_export


def get_main_window():
    """Maya画面の後ろにいかせない"""

    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr),QWidget)
    return mayaMainWindow

def close_child(app):
    """ ウィンドウの重複回避 """

    parent_list =  app.parent().children()
    for i in parent_list:
        if app.__class__.__name__ == i.__class__.__name__:
            i.close()

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        close_child(self)
        self.import_json = kmt_import_json.ImportJson()
        self.exp = kmt_export.ExportFile()
        self.mainGUI()
        self.reload_bookMK_list()
        self.set_style_sheet()

    def mainGUI(self):
        path = os.getcwd()
        self.setWindowTitle("kmt_export")
        self.resize(750, 300)
        self.file_label01 = QLabel("出力パス")
        self.text_field01 = QLineEdit(path)
        
        self.button01 = QPushButton("")
        self.button01.setIcon(QIcon(':/fileOpen.png'))
        self.button01.clicked.connect(self.folder_open)

        self.button02 = QPushButton("+") # ブックマークボタン
        self.button02.clicked.connect(self.make_bookMK)

        self.top_h_layout = QHBoxLayout()
        self.top_h_layout.addWidget(self.file_label01)
        self.top_h_layout.addWidget(self.text_field01)
        self.top_h_layout.addWidget(self.button01)
        self.top_h_layout.addWidget(self.button02)

        self.name_label01 = QLabel("ファイル名")
        self.name_field01 = QLineEdit()
        self.get_name_button = QPushButton(u"ファイル名取得")
        self.get_name_button.clicked.connect(self.get_file_name)

        self.name_h_layout = QHBoxLayout()
        self.name_h_layout.addWidget(self.name_label01)
        self.name_h_layout.addWidget(self.name_field01)
        self.name_h_layout.addWidget(self.get_name_button)

        self.top_v_layout = QVBoxLayout()
        self.top_v_layout.addLayout(self.top_h_layout)
        self.top_v_layout.addLayout(self.name_h_layout)

        self.file_list01 = QListWidget()
        self.file_list01.setContextMenuPolicy(Qt.CustomContextMenu)
        self.file_list01.customContextMenuRequested.connect(self.context01)
        self.file_list01.itemDoubleClicked.connect(self.add_text_field)
        
        self.exp_button = QPushButton(u"出力")
        self.exp_button.setObjectName("export")
        self.exp_button.clicked.connect(self.exp_file)

        self.button_h_layout = QHBoxLayout()
        self.button_h_layout.addWidget(self.exp_button)

        self.filde_v_layout = QVBoxLayout()
        self.filde_v_layout.addWidget(self.file_list01)

        main_v_widget = QVBoxLayout()
        main_v_widget.setContentsMargins(20, 20, 20, 20)
        main_v_widget.addLayout(self.top_v_layout)
        main_v_widget.addLayout(self.filde_v_layout)
        main_v_widget.addLayout(self.button_h_layout)

        widget = QWidget()
        widget.setLayout(main_v_widget)
        self.setCentralWidget(widget)

    def exp_file(self):
        """ 出力用メソッド """
        exp_path = self.text_field01.text()
        file_name = self.name_field01.text()

        self.exp.main(exp_path,file_name)

    # ========================================================================
    # ブックマーク関連の処理
    # ========================================================================

    def reload_bookMK_list(self):
        self.file_list01.clear()
        filelist = self.import_json.re_json()
        for i in filelist:
            self.file_list01.addItem(i)
    
    def add_bookMK(self):
        bookMK_path = self.text_field01.text()
        self.import_json.write_json(bookMK_path)
        self.reload_bookMK_list()

    def make_bookMK(self):
        text01 = self.text_field01.text()
        self.import_json.write_json(text01)
        self.reload_bookMK_list()

    def add_text_field(self):
        bookMK_directory = self.file_list01.currentItem().text()
        self.text_field01.setText(bookMK_directory)
        print(bookMK_directory)

    # ========================================================================
    # ========================================================================
    
    def folder_open(self):
        text01 = self.text_field01.text()
        set_directory = kmt_maya_module.folder_opne(text01)

        try:
            self.text_field01.setText(set_directory[0])
        except TypeError:
            print(u"フォルダは選ばれなかったのでテキストフィールドは据え置き")

    def get_file_name(self):
        file_name = kmt_maya_module.get_file_name()
        self.name_field01.setText(file_name)

    def get_path(self):
        self.text01 = self.text_field01.text()
        self.widgetItem = QListWidgetItem()
        
        self.filelist = os.listdir(self.text01)
        list_num = self.file_list01.count()
        if 0 < list_num:
            self.clear_list()
        self.add_item()

    # ========================================================================
    # コンテキストメニュー 
    # ========================================================================       

    def context01(self, pos):
        menu = QMenu(self.file_list01)
        action_01 = menu.addAction(u'ブックマークの削除')
        action_01.triggered.connect(self.remove_bookMK)
        action_02 = menu.addAction(u'フォルダを開く')
        action_02.triggered.connect(self.open_folder)
        menu.exec_(self.file_list01.mapToGlobal(pos))

    def remove_bookMK(self):
        list_in_bookMK_path = self.file_list01.currentItem().text()
        self.import_json.remove_json(list_in_bookMK_path)
        self.reload_bookMK_list()
    
    def open_folder(self):
        """ ブックマークされたディレクトリを開く
        
        Raises:UnicodeEncodeError
            ディレクトリに日本語が入っている場合はエラー
        
        """
        list_in_bookMK_path = self.file_list01.currentItem().text()
        list_in_bookMK_path = list_in_bookMK_path.replace('/', '\\')

        try:
            subprocess.Popen(["explorer", list_in_bookMK_path ], shell=True)
        
        except UnicodeEncodeError:
            kmt_maya_module.directory_error()

    # ========================================================================
    # ========================================================================
    
    def set_style_sheet(self):
        """ 装飾の読み込み """

        style_file = os.path.join(os.path.dirname(__file__),'kmt_style_sheet.qss')
        with open(style_file, 'r') as f:
            style = f.read()    
        self.setStyleSheet(style)


def main():
    app = QApplication.instance()
    maya_main_window = get_main_window()
    main_window = MainWindow(maya_main_window)
    main_window.show()
    sys.exit()
    app.exec_()

if __name__ == "__main__":
    main()