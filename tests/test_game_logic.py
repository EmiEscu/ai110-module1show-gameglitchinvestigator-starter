import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# ---------------------------------------------------------------------------
# Original tests (fixed: check_guess returns (outcome, message), not a string)
# ---------------------------------------------------------------------------

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# Bug 1 & 3 — Hints were backwards / score was driving direction not secret
# Reflection: "when I put 100 it said to go lower, but when I made it 50 it
#              said to go higher" and "the Score was managing direction instead
#              of the secret"
# ---------------------------------------------------------------------------

def test_high_guess_says_go_lower():
    """Regression for reversed-hint bug — guessing too high must say LOWER."""
    outcome, message = check_guess(100, 40)
    assert outcome == "Too High"
    assert "LOWER" in message.upper(), f"Expected go lower hint, got: {message}"

def test_low_guess_says_go_higher():
    """Regression for reversed-hint bug — guessing too low must say HIGHER."""
    outcome, message = check_guess(10, 40)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper(), f"Expected go higher hint, got: {message}"

def test_high_guess_does_not_say_higher():
    """The original bug: high guess incorrectly said go higher."""
    _, message = check_guess(100, 40)
    assert "HIGHER" not in message.upper(), f"Bug reproduced: {message}"

def test_low_guess_does_not_say_lower():
    """The original bug: low guess incorrectly said go lower."""
    _, message = check_guess(10, 40)
    assert "LOWER" not in message.upper(), f"Bug reproduced: {message}"

def test_check_guess_uses_secret_not_score():
    """Same guess, different secrets → opposite outcomes proves secret drives logic."""
    outcome_high, _ = check_guess(50, 20)  # 50 > 20 → Too High
    outcome_low,  _ = check_guess(50, 80)  # 50 < 80 → Too Low
    assert outcome_high == "Too High"
    assert outcome_low  == "Too Low"


# ---------------------------------------------------------------------------
# Bug 2 — Difficulty ranges didn't match labeled difficulty
# Reflection: "difficulty did not match the amount of attempts you were given"
#             Hard range was originally 1–50 (easier than Normal)
# ---------------------------------------------------------------------------

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_hard_range_is_actually_hard():
    """Regression: Hard was capped at 50 — easier than Normal (1-100)."""
    _, high = get_range_for_difficulty("Hard")
    assert high == 200, f"Hard should reach 200, got {high}"

def test_hard_harder_than_normal():
    _, hard_high   = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_normal_harder_than_easy():
    _, normal_high = get_range_for_difficulty("Normal")
    _, easy_high   = get_range_for_difficulty("Easy")
    assert normal_high > easy_high


# ---------------------------------------------------------------------------
# Bug 4 — Score logic was weird / unexpected
# Reflection: "the score was weird. I wasn't too sure behind the logic"
# ---------------------------------------------------------------------------

def test_win_adds_points():
    new_score = update_score(0, "Win", attempt_number=1)
    assert new_score > 0

def test_win_early_beats_win_late():
    """Winning sooner should award more points than winning late."""
    score_early = update_score(0, "Win", attempt_number=1)
    score_late  = update_score(0, "Win", attempt_number=8)
    assert score_early > score_late

def test_win_score_never_below_floor():
    """Even on a very late win the score should get at least 10 points."""
    score = update_score(0, "Win", attempt_number=50)
    assert score >= 10

def test_unknown_outcome_leaves_score_unchanged():
    score = update_score(42, "Some Random Outcome", attempt_number=3)
    assert score == 42


# ---------------------------------------------------------------------------
# Bug 5 — parse_guess edge cases
# Reflection: "you could not press enter to submit a response" (empty submit)
# ---------------------------------------------------------------------------

def test_valid_integer_string():
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None

def test_empty_string_returns_error():
    """Pressing enter with an empty input should give a clear error message."""
    ok, value, err = parse_guess("")
    assert ok is False and value is None and err is not None

def test_none_input_returns_error():
    ok, _, err = parse_guess(None)
    assert ok is False and err is not None

def test_non_numeric_string_returns_error():
    ok, _, err = parse_guess("abc")
    assert ok is False and err is not None

def test_decimal_input_truncates_to_int():
    ok, value, _ = parse_guess("7.9")
    assert ok is True and isinstance(value, int)

def test_whitespace_only_returns_error():
    ok, _, _ = parse_guess("   ")
    assert ok is False
