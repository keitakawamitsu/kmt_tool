# coding: utf-8
"""出力用のモジュール

name: kmt_kmt_export

"""

import os
from maya import cmds

class ExportFile:

    def main(self,exp_path,file_name):
        """GUIからパスとファイル名を受け取り、出力用のメソッドに渡す

        :param str exp_path: 出力先のフルパス
        :param str file_name: 出力するファイル名
        
        """
        if file_name:
            file_name = file_name + ".fbx"
        else:
            cmds.confirmDialog(m = u'ファイル名を入力して下さい', b=[u'閉じる'])
            return

        exp_path = exp_path.replace("\\","/")
        self.new_exp_path = exp_path +  "/" + file_name
        
        if os.path.exists(exp_path):
            self.file_export()
        else:
            cmds.confirmDialog(m = u'フォルダがありません', b=[u'閉じる'])
            return

    def file_export(self):
        """ 出力用のメソッド

        ここの処理にはプロジェクトのレギュレーションに沿って変更します。
        今回は便宜上、FBXファイルの出力処理のみを記載しております。
        
        """
        cmds.file(self.new_exp_path, ellipsis =1 , f = 1, typ = "FBX export")

