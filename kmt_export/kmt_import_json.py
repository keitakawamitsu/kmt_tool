# coding: utf-8
"""ブックマークの登録/読み込み/削除を行う

name：kmt_import_json

"""
import os
import getpass
import json

class ImportJson:
    def __init__(self):
        self.BOOKMARK_PATH = self.make_json_file()
    
    def make_json_file(self):
        """ ブックマークファイルの有無を判定 
        
        所定のディレクトリにブックマーク用のJsonファイルがなければ新規作成。

        :return: ブックマーク用のファイルがあるディレクトリのフルパス
        
        """

        JSON_FILE = "bookmark.json"
        USER_NAME = getpass.getuser()
        
        #BOOKMARK_PATH = ("C:/Users/{}/Documents/maya/scripts/kmt_tool/kmt_export/{}").format(USER_NAME,JSON_FILE) # 業務用パス
        BOOKMARK_PATH = ("C:/work/05_mayaTool/kmt_tool/kmt_export/{}").format(JSON_FILE) # ローカル用パス

        if os.path.exists(BOOKMARK_PATH):
            print(u"ブックマークファイルは既にある")
            return BOOKMARK_PATH

        current_path = os.getcwd()
        new_current_path = current_path.replace("\\","/")
        
        with open(BOOKMARK_PATH,mode = "w") as f:
            f.write('["{}"]'.format(new_current_path))
        return BOOKMARK_PATH

    def re_json(self):
        """ ブックマークの更新時に使用
        
        ;return: 登録されたブックマーク

        """
        
        with open(self.BOOKMARK_PATH,"r") as f:
            json_object = json.load(f)
        
        bookmark_list = json_object
        return bookmark_list
    
    def write_json(self,bookMK):
        """ GUIからパスを受け取りJsonファイルにブックマークを登録していく
        
        :param str bookMK: GUIから受け取ったパス

        """

        with open(self.BOOKMARK_PATH,"r") as f:
            json_object = json.load(f)
        j_list = json_object
        j_list.insert(0,bookMK)

        js_r = open(self.BOOKMARK_PATH, "w")
        json.dump(j_list,js_r, indent = 2)
        js_r.close()

    def remove_json(self, crnt_list = "NONE"):
        """ ブックマークの削除
        
        :param str crnt_list: GUIで選択されてるパス
        :raises ValueError: ブックマークファイルに何も書かれてない場合

        """

        with open(self.BOOKMARK_PATH,"r") as f:
            json_object = json.load(f)
        j_list = json_object
        try:
            j_list.remove(crnt_list)
        except ValueError:
            print(u"パスが存在しない")
        
        js_r=open(self.BOOKMARK_PATH,'w')
        json.dump(j_list,js_r,indent=2)
        js_r.close()