# --- Imports --- #

from dataclasses import dataclass, field
from typing import Iterable, Self, Tuple


# --- Node Class --- #

@dataclass(slots=True)
class Node:
    """Node to create a tree, can be subclassed to fit your needs"""
    name: str
    children: list[Self] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def __bool__(self) -> bool:
        return bool(self.children)

    def __len__(self) -> int:
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

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


# --- Tree Class --- #

@dataclass(slots=True)
class Tree:
    """A generic tree, can be subclassed to fit your needs"""
    name: str
    __root: Node

    def __str__(self) -> str:
        return self.name

    def __iter__(self) -> Iterable[Node]:
        return iter(self.__root)

    def __len__(self) -> int:
        return len(self.__root)

    @property
    def root(self) -> Node:
        return self.__root

    def __get_node(self, name: str, root: Node) -> Node | None:
        for node in root:
            if len(node) > 0:
                return_node = self.__get_node(name, node)

            if name == str(node):
                return node

        return return_node

    def get_node(self, name: str) -> Node:
        return self.__get_node(name, self.root)


# --- MultiRootTree Class --- #

@dataclass(slots=True)
class MultiRootTree:
    name: str
    __trees: list[Tree]

    def __str__(self) -> str:
        return self.name

    def __iter__(self) -> Iterable[Tree]:
        return iter(self.__trees)

    def __len__(self) -> int:
        return len(self.__trees)
