"""
Visualization functions for sequence alignment.

Displays the dynamic programming scoring matrix
used by Needleman-Wunsch and Smith-Waterman.
"""

import matplotlib.pyplot as plt


def plot_scoring_matrix(
    matrix: list[list[int]],
    sequence1: str,
    sequence2: str,
    title: str = "Scoring Matrix"
) -> None:
    """Display the alignment scoring matrix as a heatmap."""

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.imshow(matrix, cmap="Blues")

    row_labels = ["-"] + list(sequence1.upper())
    column_labels = ["-"] + list(sequence2.upper())

    ax.set_xticks(range(len(column_labels)))
    ax.set_yticks(range(len(row_labels)))

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ax.text(
                j,
                i,
                str(matrix[i][j]),
                ha="center",
                va="center"
            )

    ax.set_xlabel("Sequence 2")
    ax.set_ylabel("Sequence 1")
    ax.set_title(title)

    plt.tight_layout()
    plt.show()