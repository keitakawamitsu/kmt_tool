# kmt_export
![kmt_exportの説明](https://user-images.githubusercontent.com/69702777/167659724-f32f9b32-a091-413f-84f3-786a2b6ee024.png)

アセット出力ツール。<br>
出力先を保存できるすることでパスを探索する時間を削減。
出力のイテレーションを向上。

## kmt_toolのインストール手順
### < 手順① >
ダウンロードファイルを解凍後、[kmt_tool]フォルダを、Pythonのパスが通ってる階層にコピーします。

（例「C:\Users\kawamitsu\Documents\maya\scripts」）

### < 手順② >
スクリプトエディタのpythonタブで、以下のコマンド実行します。

```python
from kmt_tool import kmt_menu
kmt_menu.main_menu()
```

![Mayaのメニューに登録されてる様子](https://user-images.githubusercontent.com/69702777/167659731-ab4b0c4a-1d0a-42d3-8295-747df97845b0.png)<br>
mayaのメニューに[kmt_tool]が追加されます。

### 出力ツールの起動

kmt_tool > motion > export より該当のツールを起動します。

## ブックマークの登録と削除
![ブックマークの登録と削除](https://user-images.githubusercontent.com/69702777/167282847-75476e83-9b8b-41e5-a73b-096461738d22.gif)

1. ツールを起動させパスを入力
2. テキストフィールド右側の『 + 』をクリック
3. 下のリストにパスが登録されていく

## 登録したパスをエクスプローラーで開く

![登録したパスをエクスプローラーで開く](https://user-images.githubusercontent.com/69702777/167283705-0501d227-5673-4552-b559-82d7de186bde.gif)

1. リスト上で開きたいパスを選択
2. 右クリック > フォルダを開く
