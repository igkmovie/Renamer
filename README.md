# ReNamer アドオン - ReadMe ドキュメント

## 概要

**アドオン名**: ReNamer  
**作者**: ig_k  
**バージョン**: 1.0.0  
**対応 Blender バージョン**: 2.83.0 以上  
**カテゴリ**: UI  

## 説明

ReNamer アドオンは、CSVファイルに基づいて Blender のアーマチュアボーンやシェイプキーの名前を変更するためのアドオンです。名前付けの標準化やモデルのエクスポート準備など、さまざまな目的でオブジェクトの名前を一括変更する必要があるユーザーに特に便利です。

## 特徴

- CSVマッピングに基づいたアーマチュアボーンおよびメッシュシェイプキーの名前変更。
- 名前変更の方向（左から右、右から左）を選択可能。
- 簡単で直感的なUIパネルによる操作。

## インストール方法

1. Blender を開きます。
2. `編集` -> `プリファレンス` に移動します。
3. サイドバーから `アドオン` を選択します。
4. 右上の `インストール...` をクリックします。
5. ReNamer アドオンファイル (`Renamer.py`) を選択します。
6. アドオンが有効になっていることを確認します（チェックボックスをオンにします）。

## 使用方法

1. Blender の 3D ビューポートを開きます。
2. サイドバーに `ReNamer` という新しいタブが表示されます（サイドバーが表示されていない場合は `N` キーを押します）。
3. ReNamer パネルで次のプロパティを設定します:
   - **Target_List**: 名前変更の方向を選択します（`Left>Right` または `Right>Left`）。
   - **CSV_Path**: 名前変更マッピングを含むCSVファイルのパスを指定します。
4. `StartRename` ボタンをクリックして名前変更プロセスを実行します。

## CSVファイル形式

CSVファイルには次の2列が含まれている必要があります:
- 最初の列は、ボーンやシェイプキーの現在の名前を表します。
- 2列目は、新しい名前を表します。

例:
OldName,NewName
左目,eye.L
まばたき,blink

# 使用例

1. 次の内容の `rename_mappings.csv` というCSVファイルを作成します:
2. ReNamer パネルの `CSV_Path` に `rename_mappings.csv` のパスを設定します。
3. オブジェクトモードで `ARMATURE` または `MESH` タイプのオブジェクトを選択します。
4. `StartRename` ボタンをクリックして、CSVファイルに指定された通りにボーンやシェイプキーの名前を変更します。

# サンプルCSV
- MMD_Vroid.csv　PMXの標準ボーンと一般的なモーフをVroid形式のボーン名に変更するもの
- MMD_Vroid[.L][.R].csv　MMDToolsでインポートしたPMXをVroid形式のボーン名に変更するもの
- MMD_blender.csv　MMDTools以外で読み込んだPMXのボーン名をミラーにする