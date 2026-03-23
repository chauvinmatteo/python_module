import sys


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    score_processed: list[int] = []

    for score in sys.argv[1:]:
        try:
            valid_score: int = int(score)
            score_processed.append(valid_score)
        except ValueError:
            print(f"Invalid parameter: '{score}'")

    if not score_processed:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {score_processed}")
        print(f"Total players: {len(score_processed)}")
        print(f"Total score: {sum(score_processed)}")
        print("Average score:", sum(score_processed) / len(score_processed))
        print(f"High score: {max(score_processed)}")
        print(f"Low score: {min(score_processed)}")
        print("Score range:", max(score_processed) - min(score_processed))


if __name__ == "__main__":
    score_analytics()
