# --- Imports --- #

try:
    from .fs_tree import FSTree, FSNode
    from .skill_tree import FocusTree, FocusTreeNode, SkillTree, SkillTreeNode
    from .tree import Tree, Node
except ImportError:
    from fs_tree import FSTree, FSNode
    from skill_tree import FocusTree, FocusTreeNode, SkillTree, SkillTreeNode
    from tree import Tree, Node


# --- Main --- #

if __name__ == "__main__":
    def main():
        node = FSNode("Users")
        node2 = FSNode("SpartanOS")
        node3 = FSNode("Apps")
        root = FSNode("C:", [node, node2, node3])
        tree = FSTree("ATFS", root)

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
        
        node2 = FocusTreeNode("Triple Jump")
        node3 = FocusTreeNode("Double Jump", [node2])

        node9 = FocusTreeNode("Damage III")
        node8 = FocusTreeNode("Damage II", [node9])
        node7 = FocusTreeNode("Damage I", [node8], True)
        node10 = FocusTreeNode("Blast I")

        root = FocusTreeNode("Agility", [node, node3], True)
        root2 = FocusTreeNode("Damage", [node7, node10], True)
        
        focustree = Tree("Agility Tree", root)
        focustree2 = Tree("Damage Tree", root2)

        masterfocustree = FocusTree("Skill Tree", [focustree, focustree2])
        
        print(masterfocustree,
              [str(node) for node in masterfocustree.available_nodes(root)],
              sep="\n")
        masterfocustree.buy_node(node)
        print("\n",
              masterfocustree,
              [str(node) for node in masterfocustree.available_nodes(root)],
              sep="\n")
        print()
        print([[str(n) for n in node] for node in masterfocustree.all_available_nodes()])



    main()
