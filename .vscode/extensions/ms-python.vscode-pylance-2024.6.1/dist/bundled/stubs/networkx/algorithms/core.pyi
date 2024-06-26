from typing import Mapping

from ..classes.graph import Graph
from ..exception import NetworkXError
from ..utils import not_implemented_for

__all__ = [
    "core_number",
    "find_cores",
    "k_core",
    "k_shell",
    "k_crust",
    "k_corona",
    "k_truss",
    "onion_layers",
]

def core_number(G: Graph) -> Mapping: ...
def find_cores(G: Graph): ...
def k_core(G: Graph, k: int | None = None, core_number: Mapping | None = None): ...
def k_shell(G: Graph, k: int | None = None, core_number: Mapping | None = None): ...
def k_crust(G: Graph, k: int | None = None, core_number: Mapping | None = None): ...
def k_corona(G: Graph, k: int, core_number: Mapping | None = None): ...
def k_truss(G: Graph, k: int): ...
def onion_layers(G: Graph) -> Mapping: ...
