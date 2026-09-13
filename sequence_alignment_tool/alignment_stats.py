"""Alignment statistics for pairwise sequence alignments."""
def calculate_statistics(
    aligned_sequence1: str,
    aligned_sequence2: str
) -> dict:
    """Calculate matches, mismatches, gaps and identity."""

    matches = 0
    mismatches = 0
    gaps = 0

    for char1, char2 in zip(aligned_sequence1, aligned_sequence2):

        if char1 == "-" or char2 == "-":
            gaps += 1

        elif char1 == char2:
            matches += 1

        else:
            mismatches += 1

    alignment_length = len(aligned_sequence1)

    identity = (
        (matches / alignment_length) * 100
        if alignment_length > 0
        else 0
    )

    return {
        "alignment_length": alignment_length,
        "matches": matches,
        "mismatches": mismatches,
        "gaps": gaps,
        "identity": identity
    }