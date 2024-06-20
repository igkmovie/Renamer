import bpy
import logging
from bpy.props import (
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    EnumProperty,
    BoolProperty,
    PointerProperty,
    StringProperty
)
import csv


bl_info = {
    "name" : "ReNamer", #des アドオン名
    "author" : "ig_k", #des 作者の名前
    "version" : (1, 0, 0), #des バージョン数
    "blender" : (2, 83, 0),#des 対応バージョン
    "location" : "hoge", #des アドオンの場所(ショートカットやパネルの表示場所など)
    "description" : "hoge", #des アドオンの解説
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "UI"
}


class ReNamerOnPushButton(bpy.types.Operator, bpy.types.Panel):
   
    bl_idname = "object.renamer"
    bl_label = "NOP"
    bl_description = "処理スタート"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        csv_file = bpy.path.abspath(bpy.context.scene.CSV_Path)
        logging.info(csv_file)

        with open(csv_file, "r", encoding="utf-8") as f:
            namelist = list(csv.reader(f))
        if(obj.type == "MESH"):
            shape_keys = obj.data.shape_keys.key_blocks

        if(bpy.context.scene.List_enum == "Left>Right"):
            for leftName, RightName in namelist:
                name = leftName
                newname = RightName
     
                if(obj.type == "ARMATURE"):
                    pb = obj.pose.bones.get(name)
                    if pb is None:
                        continue
                    pb.name = newname
                elif(obj.type == "MESH"):
                    for key in shape_keys:
                        if(key.name == name):
                            key.name = newname               
        else:
            for leftName, RightName in namelist:
                name = RightName
                newname = leftName

                if(obj.type == "ARMATURE"):
                    pb = obj.pose.bones.get(name)
                    if pb is None:
                        continue
                    pb.name = newname
                elif(obj.type == "MESH"):
                    for key in shape_keys:
                        if(key.name == name):
                            key.name = newname   
                

        return{"FINISHED"}


class ReNamerCustomPanel(bpy.types.Panel):

    bl_label = "ReNamer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ReNamer"
    bl_context = "objectmode"

    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="PLUGIN")
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # # ドロップダウンプロパティを追加
        # layout.label(text="現在のArmature形式")
        # layout.prop(scene, "Current_Armature_enum", text="Current_Armature")
        
        # # セパレータを追加
        # layout.separator()

        # # ドロップダウンプロパティを追加
        # layout.label(text="変換するのArmature形式")
        # layout.prop(scene, "Target_Armature_enum", text="Target_Armature")
        
        layout.label(text="List_enum")
        layout.prop(scene, "List_enum", text="Target_List")

        # セパレータを追加
        layout.separator()
        layout.label(text="CSV_Path")
        layout.prop(scene, "CSV_Path", text="CSV_Path")
        # セパレータを追加
        layout.separator()

        layout.label(text="ボタン:")
        layout.operator(ReNamerOnPushButton.bl_idname, text="StartRename")


def init_props():
    scene = bpy.types.Scene
    # scene.Current_Armature_enum = EnumProperty(
    #     name="Current_Armature",
    #     description="Current_Armature_enum",
    #     items=[
    #         ('pmx', "pmx", "pmx"),
    #         ('Vroid', "Vroid", "Vroid"),
    #         ('AutoRigPro', "AutoRigPro", "AutoRigPro"),
    #         ('UnityChan', "UnityChan", "UnityChan")
    #     ],
    #     default='Vroid'
    # )
    # scene.Target_Armature_enum = EnumProperty(
    #     name="Target_Armature",
    #     description="Target_Armature_enum",
    #     items=[
    #         ('pmx', "pmx", "pmx"),
    #         ('Vroid', "Vroid", "Vroid"),
    #         ('AutoRigPro', "AutoRigPro", "AutoRigPro"),
    #         ('UnityChan', "UnityChan", "UnityChan")
    #     ],
    #     default='pmx'
    # )
    scene.List_enum = EnumProperty(
        name="Target_List",
        description="List_enum",
        items=[
            ('Left>Right', "Left>Right", "Left>Right"),
            ('Right>Left', "Right>Left", "Right>Left")
        ],
        default='Left>Right'
    )
    scene.CSV_Path = StringProperty(name="CSVFile", subtype="FILE_PATH")


def clear_props():
    scene = bpy.types.Scene
    # del scene.Target_Armature_enum
    # del scene.Current_Armature_enum
    del scene.List_enum
    del scene.CSV_Path


classes = [ReNamerOnPushButton, ReNamerCustomPanel] 


def register():
    for c in classes:
        bpy.utils.register_class(c)
    init_props()


def unregister():
    clear_props()
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()


