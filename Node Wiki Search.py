import bpy
import webbrowser

bl_info = {
    "name": "Node Wiki Search",
    "author": "Anec",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "location": "Node Editor",
    "description": "Searches the name of the selected node in the Blender Wiki",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Node"
}

class NODE_OT_wiki_search(bpy.types.Operator):
    """Searches the name of the selected node in the Blender Wiki"""
    bl_idname = "node.wiki_search"
    bl_label = "Search Node in Wiki"

    def execute(self, context):
        node = context.active_node
        if node:
            webbrowser.open(f'https://docs.blender.org/manual/en/3.5/search.html?q={node.name}')
        else:
            self.report({'WARNING'}, "No node selected")
        return {'FINISHED'}


class NODE_PT_wiki_search(bpy.types.Panel):
    """Creates a button in the node editor"""
    bl_label = "Node Wiki Search"
    bl_idname = "NODE_PT_wiki_search"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Wiki"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.wiki_search")

def register():
    bpy.utils.register_class(NODE_OT_wiki_search)
    bpy.utils.register_class(NODE_PT_wiki_search)

def unregister():
    bpy.utils.unregister_class(NODE_OT_wiki_search)
    bpy.utils.unregister_class(NODE_PT_wiki_search)


if __name__ == "__main__":
    register()
