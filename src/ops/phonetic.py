import numpy as np

from pyphonetics import RefinedSoundex
from typing import List


rs = RefinedSoundex()


def phonetically_closest(candidates: List[str], query: str) -> int:
    """
    Returns `query`'s phonetically closest word in `candidates`
    Uses the levenshtein method to find the distance between 2 phonetic representations.
    """
    distances = [rs.distance(query, c) for c in candidates]
    argmin = np.argmin(distances)
    return argmin

