# --- Imports --- #

from dataclasses import dataclass
from typing import Self
from pathlib import PureWindowsPath
from tree import Tree, Node


# --- Path Class --- #

class Path(PureWindowsPath):
    def __init__(self, *pathsegments) -> Self:
        super().__init__(*pathsegments)

    def __str__(self) -> str:
        return "/".join(self.parts).replace("\\", "/")


# --- FSNode Class --- #

@dataclass(slots=True)
class FSNode(Node):
    data: str = ""


# --- FSTree Class --- #

@dataclass(slots=True)
class FSTree(Tree):
    def open(self, name: str) -> Node:
        if "/" in name:
            self.__open_path(name)
            return self.current
        
        if name == "*":
            self.clear()
        elif name == "..":
            self.back()
        else:
            Tree.open(self, name)
            
        return self.current

    def __open_path(self, name: str) -> None:
        for item in name.split("/"):
            self.open(item)

    def __str__(self) -> Path:
        return str(Path(*self.path))


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
        print("\n", tree, tree.path, tree.dir, sep="\n")

    main()
