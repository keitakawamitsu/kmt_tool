# coding: utf-8
"""GUIのモジュールに使用するmayaコマンド

name: kmt_maya_module

"""

import os
import subprocess
from maya import cmds

def folder_opne(directory = 'c:'):
    """テキストフィールドのパスを開く
    
    :return: 出力先に指定したディレクトリのフルパス
    
    """
    export_dir_name = cmds.fileDialog2(fileMode=3,dialogStyle=2,dir=directory)
    return export_dir_name


def get_file_name():
    """現在のシーン名を取得してファイル名にする
    
    :return: 拡張子を除くファイル名

    """
    file_name = os.path.splitext(cmds.file(q=1, sn=1, shn=1))[0]
    return file_name

def directory_error():
    """右クリックでエクスプローラーを開こうとした際のエラー表示"""

    cmds.confirmDialog(m = u'日本語パスは開けません', b=[u'閉じる'])
