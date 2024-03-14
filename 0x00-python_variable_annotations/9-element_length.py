#!/usr/bin/env python3
""""
Task 9: Annotate the below function’s parameters
and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calcul of the length of list of sequance
    """
    return [(i, len(i)) for i in lst]
