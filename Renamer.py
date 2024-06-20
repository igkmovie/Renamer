import bpy
import logging
from bpy.props import (
    EnumProperty,
    StringProperty
)
import csv


bl_info = {
    "name" : "ReNamer",
    "author" : "ig_k",
    "version" : (1, 0, 0),
    "blender" : (2, 83, 0),
    "location" : "hoge",
    "description" : "hoge",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : "UI"
}


class ReNamerOnPushButton(bpy.types.Operator):
   
    bl_idname = "object.renamer"
    bl_label = "Start Rename"
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

        for old_name, new_name in namelist:
            if(obj.type == "ARMATURE"):
                pb = obj.pose.bones.get(old_name)
                if pb is None:
                    continue
                pb.name = new_name
            elif(obj.type == "MESH"):
                for key in shape_keys:
                    if(key.name == old_name):
                        key.name = new_name               

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

        layout.label(text="CSV_Path")
        layout.prop(scene, "CSV_Path", text="CSV_Path")

        layout.separator()

        layout.label(text="ボタン:")
        layout.operator(ReNamerOnPushButton.bl_idname, text="StartRename")


def init_props():
    scene = bpy.types.Scene
    scene.CSV_Path = StringProperty(name="CSVFile", subtype="FILE_PATH")


def clear_props():
    scene = bpy.types.Scene
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
