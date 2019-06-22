bl_info = {
    "name": "Power Clean Duplicate Material Names",
    "author": "ChaiBiQ",
    "version": (0,0,1),
    "blender": (2, 80,0),
    "description": "Merges all duplicate material names",
    "location": "Properties > Material > Slot > Right Menu > PowerCleanMats",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}

import bpy

class PowerCleanMats(bpy.types.Operator):
    """Merges duplicate materials.xxx"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.power_clean_mats"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Power Clean Material Names"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        mats_list = bpy.data.materials
        for obj in bpy.data.objects:
            for sl in obj.material_slots:
                if sl.material.name[-3:].isnumeric():
                    if sl.material.name[:-4] in mats_list:     #Find material.xxx
                        sl.material = mats_list[sl.material.name[:-4]]   #Replace
        return {'FINISHED'}

def register():
    bpy.utils.register_class(PowerCleanMats)
    bpy.types.MATERIAL_MT_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(PowerCleanMats)
    bpy.types.MATERIAL_MT_context_menu.remove(menu_func)

def menu_func(self, context):
    self.layout.separator()
    self.layout.operator(PowerCleanMats.bl_idname)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()

