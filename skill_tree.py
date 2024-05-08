# --- Imports --- #

from dataclasses import dataclass, field
from typing import Self
from tree import MultiRootTree, Tree, Node


# --- FocusTreeNode Class --- #

@dataclass(slots=True)
class FocusTreeNode(Node):
    __active: bool = False

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError(f"Expected boolean, got {value}")
        self.__active = value


# --- FocusTree Class --- #

@dataclass(slots=True)
class FocusTree(MultiRootTree):
    def __available_nodes(self,
                          returnList: list[FocusTreeNode],
                          root: FocusTreeNode) -> None:
        for node in root:
            if node.active:
                returnList.extend(
                    [subnode for subnode in node if not subnode.active])
                continue

            returnList.append(node)

        return returnList
            
    def available_nodes(self, root: Node) -> list[FocusTreeNode]:
        return self.__available_nodes([], root)

    def buy_node(self, node: FocusTreeNode) -> None:
        node.active = True

    def all_available_nodes(self) -> list[list[FocusTreeNode]]:
        return [self.available_nodes(root) for root in iter(self)]


SkillTree = FocusTree #Alias
SkillTreeNode = FocusTreeNode #Alias


# --- Main --- #

if __name__ == "__main__":
    def main():
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

        #focustree = Tree("Skill Tree", [root, root2])
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
