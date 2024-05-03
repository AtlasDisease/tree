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
    __path: Iterable[Node] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name

    def __iter__(self) -> Iterable[Node]:
        return self.__path

    def __len__(self) -> int:
        return len(self.__path)

    @property
    def root(self) -> Node:
        """Get the root of the tree (first node in a tree)"""
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

    def open(self, name: str) -> Node:
        node = self.__path[-1].get_child_by_name(name)
        if node is None:
            raise ValueError(f"Invalid node, {name} not found.")
        self.__path.append(node)
        
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
