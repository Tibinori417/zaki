from typing import Any, Callable

global_namespace: dict[str, Any] = ...

def dispatch(*types, namespace=..., on_ambiguity=...) -> Callable[..., Any]: ...
def ismethod(func) -> bool: ...