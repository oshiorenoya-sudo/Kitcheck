import bpy
PREFIX ="KT"

def check_names():
    incorrect_names = []
    Naming_objects = []
    for i in bpy.data.objects:
        Naming_objects.append(i.name)
    
    print(Naming_objects)
    
    for i in bpy.data.objects:
        if i.name.startswith(PREFIX):
            print(f"{i.name}: correct naming convention")
        else:
            print(f"{i.name}: incorrect naming convention. Please add {PREFIX} to the beginning")
            incorrect_names.append(i.name)
    
    print(f"These are the incorrect names: {incorrect_names}" )
    
    return incorrect_names
            
            


if __name__ =="__main__":
    check_names()
    