"""
Pairwise sequence alignment algorithms.

Currently implemented:
- Needleman-Wunsch global alignment
"""
from scoring import score_pair, gap_score
def needleman_wunsch(
    sequence1: str,
    sequence2: str,
    match_score: int = 1,
    mismatch_penalty: int = -1,
    gap_penalty: int = -2
) -> tuple[str, str, int, list[list[int]]]:

    sequence1 = sequence1.upper()
    sequence2 = sequence2.upper()

    rows = len(sequence1) + 1
    columns = len(sequence2) + 1

    # Create scoring matrix
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    # Initialize first row and first column with gap penalties
    for i in range(1, rows):
        matrix[i][0] = matrix[i - 1][0] + gap_score(gap_penalty)

    for j in range(1, columns):
        matrix[0][j] = matrix[0][j - 1] + gap_score(gap_penalty)

    # Fill scoring matrix
    for i in range(1, rows):
        for j in range(1, columns):

            diagonal = (
                matrix[i - 1][j - 1]
                + score_pair(
                    sequence1[i - 1],
                    sequence2[j - 1],
                    match_score,
                    mismatch_penalty
                )
            )

            up = matrix[i - 1][j] + gap_score(gap_penalty)
            left = matrix[i][j - 1] + gap_score(gap_penalty)

            matrix[i][j] = max(diagonal, up, left)

    # Traceback
    aligned_sequence1 = []
    aligned_sequence2 = []

    i = len(sequence1)
    j = len(sequence2)

    while i > 0 or j > 0:

        if (
            i > 0
            and j > 0
            and matrix[i][j]
            == matrix[i - 1][j - 1]
            + score_pair(
                sequence1[i - 1],
                sequence2[j - 1],
                match_score,
                mismatch_penalty
            )
        ):
            aligned_sequence1.append(sequence1[i - 1])
            aligned_sequence2.append(sequence2[j - 1])
            i -= 1
            j -= 1

        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap_score(gap_penalty):
            aligned_sequence1.append(sequence1[i - 1])
            aligned_sequence2.append("-")
            i -= 1

        else:
            aligned_sequence1.append("-")
            aligned_sequence2.append(sequence2[j - 1])
            j -= 1

    aligned_sequence1 = "".join(reversed(aligned_sequence1))
    aligned_sequence2 = "".join(reversed(aligned_sequence2))

    alignment_score = matrix[-1][-1]

    return (
        aligned_sequence1,
        aligned_sequence2,
        alignment_score,
        matrix
    )
def smith_waterman(
    sequence1: str,
    sequence2: str,
    match_score: int = 1,
    mismatch_penalty: int = -1,
    gap_penalty: int = -2
) -> tuple[str, str, int, list[list[int]]]:

    """Perform local sequence alignment using Smith-Waterman.
        Returns:
        aligned_sequence1
        aligned_sequence2
        alignment_score
        scoring_matrix
    """

    sequence1 = sequence1.upper()
    sequence2 = sequence2.upper()

    rows = len(sequence1) + 1
    columns = len(sequence2) + 1

    # Create scoring matrix
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    max_score = 0
    max_position = (0, 0)

    # Fill scoring matrix
    for i in range(1, rows):
        for j in range(1, columns):

            diagonal = (
                matrix[i - 1][j - 1]
                + score_pair(
                    sequence1[i - 1],
                    sequence2[j - 1],
                    match_score,
                    mismatch_penalty
                )
            )

            up = matrix[i - 1][j] + gap_score(gap_penalty)
            left = matrix[i][j - 1] + gap_score(gap_penalty)

            # Zero is included because this is LOCAL alignment
            matrix[i][j] = max(0, diagonal, up, left)

            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_position = (i, j)

    # Traceback starts from highest-scoring cell
    aligned_sequence1 = []
    aligned_sequence2 = []

    i, j = max_position

    while i > 0 and j > 0 and matrix[i][j] > 0:

        if (
            matrix[i][j]
            == matrix[i - 1][j - 1]
            + score_pair(
                sequence1[i - 1],
                sequence2[j - 1],
                match_score,
                mismatch_penalty
            )
        ):
            aligned_sequence1.append(sequence1[i - 1])
            aligned_sequence2.append(sequence2[j - 1])
            i -= 1
            j -= 1

        elif matrix[i][j] == matrix[i - 1][j] + gap_score(gap_penalty):
            aligned_sequence1.append(sequence1[i - 1])
            aligned_sequence2.append("-")
            i -= 1

        else:
            aligned_sequence1.append("-")
            aligned_sequence2.append(sequence2[j - 1])
            j -= 1

    aligned_sequence1 = "".join(reversed(aligned_sequence1))
    aligned_sequence2 = "".join(reversed(aligned_sequence2))

    return (
        aligned_sequence1,
        aligned_sequence2,
        max_score,
        matrix
    )