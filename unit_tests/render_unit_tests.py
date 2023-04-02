import bpy
import os



class unit_test_renderer:
       

    def __init__(self):
        print("Unit Test Renderer - %s"%bpy.context.blend_data.filepath)

    def do_render(self,testname):

        print("Rendering test: %s"%(testname))

        bpy.context.scene.render.resolution_x=1920
        bpy.context.scene.render.resolution_y=1080
        bpy.context.scene.render.resolution_percentage=50

        bpy.context.scene.render.engine="CYCLES"
        bpy.context.scene.cycles.samples=200
        bpy.context.scene.cycles.use_denoising = True

        bpy.context.scene.render.image_settings.file_format = 'PNG'
      
        try:
            render_result = bpy.ops.render.render(animation=False, write_still=False, layer="", scene="")
        except Exception as e:
            print("Render Failed: d%s"%e)
            return False
        
        full_output_image_path="images%s%s.png"%(os.sep,testname)

        bpy.data.images['Render Result'].save_render(filepath=full_output_image_path)

    def evaluate_collection(self,collection):
        # store collection visibility
        collection_original_hide_viewport=collection.hide_viewport
        collection_original_hide_render=collection.hide_render
        
        for child_collection in collection.children:
        
            # store child collection visibility    
            child_collection_original_hide_viewport=child_collection.hide_viewport
            child_collection_original_hide_render=child_collection.hide_render
            
            testname=("%s-%s"%(collection.name,child_collection.name))

            print("Evaluating: %s"%testname)
            
            # ensure visibile for render
            child_collection.hide_viewport = False
            child_collection.hide_render = False

            self.do_render(testname)
            
            # restore original child collection visibility
            child_collection.hide_viewport=child_collection_original_hide_viewport
            child_collection.hide_render=child_collection_original_hide_render
            
        # restore original collection visibility
        collection.hide_viewport=collection_original_hide_viewport
        collection.hide_render=collection_original_hide_render



    def iterate_collections(self):
        print("\r\nCollections:")
        for collection in bpy.data.collections:

            print(" - %s"%collection.name)

            if collection.name=="unit_tests":
                self.evaluate_collection(collection)    



test_Renderer = unit_test_renderer()

test_Renderer.iterate_collections()
