"""Scoring functions for sequence alignment.
Supports:
- Match score
- Mismatch penalty
- Gap penalty
"""
def score_pair(
    char1: str,
    char2: str,
    match_score: int = 1,
    mismatch_penalty: int = -1
) -> int:
    """Return the score for aligning two characters."""

    if char1 == char2:
        return match_score

    return mismatch_penalty


def gap_score(gap_penalty: int = -2) -> int:
    """Return the score for introducing a gap."""

    return gap_penalty