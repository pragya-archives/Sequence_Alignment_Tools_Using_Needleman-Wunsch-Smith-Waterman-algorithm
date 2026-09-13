"""
Sequence Alignment Tool

Performs pairwise sequence alignment using:
- Needleman-Wunsch (Global)
- Smith-Waterman (Local)
"""

from alignment_stats import calculate_statistics
from alignment import needleman_wunsch, smith_waterman
from visualization import plot_scoring_matrix


def get_integer_input(prompt: str, default: int) -> int:
    """Get an integer from the user, using a default if left blank."""

    value = input(f"{prompt} [{default}]: ").strip()

    if value == "":
        return default

    try:
        return int(value)
    except ValueError:
        print("Invalid input. Using default value.")
        return default


def display_alignment(
    sequence1: str,
    sequence2: str,
    score: int
) -> None:
    """Display the final alignment and score."""

    match_line = ""

    for char1, char2 in zip(sequence1, sequence2):
        if char1 == char2 and char1 != "-":
            match_line += "|"
        elif char1 == "-" or char2 == "-":
            match_line += " "
        else:
            match_line += "."

    print("\nAlignment:")
    print(sequence1)
    print(match_line)
    print(sequence2)
    print(f"\nAlignment score: {score}")


def main() -> None:
    """Run the Sequence Alignment Tool."""

    print("=" * 50)
    print("       SEQUENCE ALIGNMENT TOOL")
    print("=" * 50)

    sequence1 = input("\nEnter sequence 1: ").strip()
    sequence2 = input("Enter sequence 2: ").strip()

    if not sequence1 or not sequence2:
        print("\nError: Both sequences are required.")
        return

    print("\nChoose alignment algorithm:")
    print("1. Needleman-Wunsch (Global)")
    print("2. Smith-Waterman (Local)")

    choice = input("\nEnter choice [1]: ").strip()

    if choice not in ("1", "2"):
        choice = "1"

    print("\nScoring parameters:")

    match_score = get_integer_input("Match score", 1)

    mismatch_penalty = -abs(
        get_integer_input("Mismatch penalty", -1)
    )

    gap_penalty = -abs(
        get_integer_input("Gap penalty", -2)
    )

    if choice == "1":
        aligned1, aligned2, score, matrix = needleman_wunsch(
            sequence1,
            sequence2,
            match_score,
            mismatch_penalty,
            gap_penalty
        )

        algorithm = "Needleman-Wunsch (Global)"

    else:
        aligned1, aligned2, score, matrix = smith_waterman(
            sequence1,
            sequence2,
            match_score,
            mismatch_penalty,
            gap_penalty
        )

        algorithm = "Smith-Waterman (Local)"

    print(f"\nAlgorithm: {algorithm}")

    display_alignment(
        aligned1,
        aligned2,
        score
    )

    statistics = calculate_statistics(
        aligned1,
        aligned2
    )

    print("\nAlignment Statistics:")
    print(f"Alignment length : {statistics['alignment_length']}")
    print(f"Matches          : {statistics['matches']}")
    print(f"Mismatches       : {statistics['mismatches']}")
    print(f"Gaps             : {statistics['gaps']}")
    print(f"Identity         : {statistics['identity']:.2f}%")

    plot_scoring_matrix(
        matrix,
        sequence1,
        sequence2,
        f"{algorithm} Scoring Matrix"
    )


if __name__ == "__main__":
    main()

 