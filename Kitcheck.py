import bpy
PREFIX ="KT"

def check_names():
    incorrect_names = []
   #This was me mainly testing out my code through putting the items in a different list at first
   #
   # Naming_objects = []
   # for i in bpy.data.objects:
  #      Naming_objects.append(i.name)
    
  #  print(Naming_objects)
    
# For loop to check the incorrect names
    for i in bpy.data.objects:
        if i.name.startswith(PREFIX):
            print(f"{i.name}: correct naming convention")
        else:
            print(f"{i.name}: incorrect naming convention. Please add {PREFIX} to the beginning")
            incorrect_names.append(i.name)
            
 # For loop to check the incorrect numbers           
    if len(incorrect_names)== 0:
        print("All naming conventions are correct.")
    
    No_incorrect = len(incorrect_names)
    print(f"These are the incorrect names: {incorrect_names}" )
    print(f"These are the number of incorrect names: {No_incorrect}")
    
    return No_incorrect

# Button
class KITCHECK_OT_main(bpy.types.Operator):
    bl_idname = "kitcheck.assets"   
    bl_label = "Find the improperly named assets"

    def execute(self, context):
        bad = check_names()
        self.report({'INFO'}, F"{bad} incorrect names have been found")
        return {'FINISHED'}

class KITCHECK_PT_second(bpy.types.Panel):
    bl_label = "Validation check"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Kitcheck for objects"
    
    def draw(self, context):
        self.layout.operator("kitcheck.assets")
            
#Registration of the button to ensure that it works.    
def register():
    bpy.utils.register_class(KITCHECK_OT_main)
    bpy.utils.register_class(KITCHECK_PT_second)
    
def unregister():
    bpy.utils.unregister_class(KITCHECK_PT_second)
    bpy.utils.unregister_class(KITCHECK_OT_main)
    

 
            


if __name__ =="__main__":
    register()
    