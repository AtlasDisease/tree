# --- Imports --- #

from dataclasses import dataclass, field
from typing import Iterable, Self
from pathlib import PureWindowsPath


# --- Node Class --- #

@dataclass(slots=True)
class Node:
    """Node to create a tree"""
    name: str
    children: list[Self] = field(default_factory=list)
    data: str = ""

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return bool(self.children)

    def __len__(self) -> int:
        return len(self.children)

    @property
    def eob(self) -> bool:
        """Is end of branch"""
        return bool(self)

    def add_child(self, node: Self) -> None:
        """Add a child to the current node"""
        self.children.append(node)

    def add_children(self, nodes: Iterable[Self]) -> None:
        """Add children nodes to the current node"""
        for node in nodes:
            self.children.append(node)

    def remove_child(self, node: Self) -> None:
        """Remove child from the current node"""
        self.children.remove(node)

    def remove_children(self, nodes: Iterable[Self]) -> None:
        """Remove children from the current node"""
        for node in nodes:
            self.remove_child(node)

    def get_children_by_name(self, name: str) -> Iterable[Self]:
        """Get the children that contains name"""
        return filter(lambda node: name in str(node), self.children)

    def get_child_by_name(self, name: str) -> Self:
        """Get the child that contains name"""
        return next(self.get_children_by_name(name), None)


# --- Path Class --- #

class Path(PureWindowsPath):
    def __init__(self, *pathsegments) -> Self:
        super().__init__(*pathsegments)

    def __str__(self) -> str:
        return "/".join(self.parts).replace("\\", "/")


# --- Main --- #

if __name__ == "__main__":
    def main():
        node = Node("Users")
        node2 = Node("SpartanOS")
        node3 = Node("Apps")
        tree = Node("C:", [node, node2, node3])

        path = [tree]
        path.append(path[-1].get_child_by_name("SpartanOS"))
        path.pop()
        path.append(path[-1].get_child_by_name("Apps"))

        path[-1].add_child(Node("Aurora"))
        path.append(path[-1].get_child_by_name("Aurora"))

        mypath = Path(*[str(item) for item in path])

        print(tree, mypath, sep="\n")

    main()
