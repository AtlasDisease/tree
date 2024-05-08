# --- Imports --- #

try:
    from .fs_tree import FSTree, FSNode
    from .skill_tree import FocusTree, FocusTreeNode, SkillTree, SkillTreeNode
    #from .tree import Tree, Node
except ImportError:
    from fs_tree import FSTree, FSNode
    from skill_tree import FocusTree, FocusTreeNode, SkillTree, SkillTreeNode
    #from tree import Tree, Node


# --- Main --- #

if __name__ == "__main__":
    def main():
        node = FSNode("Users")
        node2 = FSNode("SpartanOS")
        node3 = FSNode("Apps")
        root = FSNode("C:", [node, node2, node3])
        tree = FSTree("ATFS", [root])

        tree.open("SpartanOS")
        tree.open("..")
        tree.open("Apps")
        tree.add("Aurora")
        tree.open("Aurora")
        print(tree, tree.path, tree.dir, sep="\n")

        tree.open("../..")
        print()
        print(tree, tree.path, tree.dir, sep="\n")

        print("\n")

        node6 = FocusTreeNode("Speed I")
        node5 = FocusTreeNode("Movement III")
        node4 = FocusTreeNode("Movement II", [node5])
        node = FocusTreeNode("Movement I", [node4])
        #node.active = True
        node2 = FocusTreeNode("Triple Jump")
        node3 = FocusTreeNode("Double Jump", [node2])        
        root = FocusTreeNode("Agility", [node, node3, node6], True)
        #root.active = True
        
        focustree = FocusTree("Skill Tree", [root])
        print(focustree,
              [str(node) for node in focustree.available_nodes(root)],
              sep="\n")
        focustree.buy_node(node)
        print()
        print(focustree,
              [str(node) for node in focustree.available_nodes(root)],
              sep="\n")

    main()
