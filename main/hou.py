import hou

nodes = hou.selectedNodes()
for node in nodes:
    print(node.name())
 