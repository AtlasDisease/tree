# --- Imports --- #

from dataclasses import dataclass, field
from typing import Self, Iterable, Tuple
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
    """Works, but does not work like I want"""
    __path: list[FSNode] = field(default_factory=list)

    def __post_init__(self):
        self.__path.append(self.root)
    
    def __str__(self) -> Path:
        return str(Path(*self.path))

    def __iter__(self) -> Iterable[Node]:
        return iter(self.__path)

    def __len__(self) -> int:
        return len(self.__path)

    @property
    def top(self) -> Node:
        """Get the top of the path (first path in a tree)"""
        return self.path[0]

    @property
    def dir(self) -> Tuple[str]:
        return tuple(map(lambda item: str(item), self.__path[-1].children))

    @property
    def current(self) -> Node:
        return self.__path[-1]

    @property
    def path(self) -> list[Node]:
        return [str(item) for item in self.__path]

    def __open(self, name: str) -> None:
        node = self.__path[-1].get_child_by_name(name)
        if node is None:
            raise ValueError(f"Invalid node, {name} not found.")
        self.__path.append(node)

    def __open_path(self, name: str) -> None:
        for item in name.split("/"):
            self.open(item)
    
    def open(self, name: str) -> Node:
        if "/" in name:
            self.__open_path(name)
            return self.current
        
        if name == "*":
            self.clear()
        elif name == "..":
            self.back()
        else:
            self.__open(name)
            
        return self.current

    def add(self, name: str) -> None:
        self.__path[-1].add_child(Node(name))

    def remove(self, name: str) -> None:
        if name not in self.__path[-1]:
            raise ValueError(f"Invalid node, {name} not found.")
        self.__path[-1].remove_child(name)
            
    def clear(self):
        del self.__path[1:]

    def back(self) -> Node:
        del self.__path[-1]


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
        print("\n", tree, tree.path, tree.dir, sep="\n")

    main()
