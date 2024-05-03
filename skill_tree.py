# --- Imports --- #

from dataclasses import dataclass, field
from typing import Self
from tree import Tree, Node


# --- FocusTreeNode Class --- #

@dataclass(slots=True)
class FocusTreeNode(Node):
    __active: bool = False

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, value):
        if not isinstance(value, bool):
            raise ValueError(f"Expected boolean, got {value}")
        self.__active = value


# --- FocusTree Class --- #

@dataclass(slots=True)
class FocusTree(Tree):
    def __available_nodes(self, returnList: list[FocusTreeNode],
                          root: FocusTreeNode) -> None:
        for node in root:
            if node.active:
                returnList.extend(list(filter(
                    lambda subnode: not subnode.active, node)))
                continue

            returnList.append(node)

        return returnList
            
    def available_nodes(self, root: Node) -> list[FocusTreeNode]:
        return self.__available_nodes([], root)

    def buy_node(self, node: FocusTreeNode):
        node.active = True


# --- Main --- #

if __name__ == "__main__":
    def main():
        node = FocusTreeNode("Movement II")
        node2 = FocusTreeNode("Triple Jump")
        node3 = FocusTreeNode("Double Jump", [node2])
        node3.active = True
        root = FocusTreeNode("Agility", [node, node3])
        root.active = True
        focustree = FocusTree("Skill Tree", [root])
        print(focustree,
              [str(node) for node in focustree.available_nodes(root)],
              sep="\n")
        focustree.buy_node(node)
        print("\n",
              focustree,
              [str(node) for node in focustree.available_nodes(root)],
              sep="\n")
  
    main()
