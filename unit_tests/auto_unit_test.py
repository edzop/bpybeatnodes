import bpy

# example usage:

# blender -b ../wave_generator.blend -P auto_unit_test.py

# loads ../wave_generator.blend and runs auto_unit_test.py after loading the blend file. 

class auto_unit_test:


    def __init__(self):

        print("Auto Unit Test Generator")


    def process_node(self,node_group):
        
        print("----------------------------")
        print(node_group.name)
        print("----------------------------")
        
        for node_input in node_group.inputs:
            print("%s - %s"%(node_input.name,node_input.type))

            # Todo - Create text label for each input


    def list_all_node_trees(self):

        for node_group in bpy.data.node_groups:
            
            self.process_node(node_group)

auto_test = auto_unit_test()

auto_test.list_all_node_trees()