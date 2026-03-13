def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines whether a ransom note can be constructed using
    letters from a given magazine.

    Approach:
        - Build a hash table (dictionary) of character frequencies
          from the magazine.
        - For each character in the ransom note, check if it exists
          in the hash table with a count > 0.
        - Decrement the count each time a character is used.
        - Return False immediately if a character is unavailable.

    Args:
        ransomNote (str): The string we want to construct.
        magazine (str): The source of available letters.

    Returns:
        bool: True if the ransom note can be built, False otherwise.

    Time Complexity:  O(m + n) — one pass each over magazine and ransomNote
    Space Complexity: O(m)     — hash table stores at most m unique chars
    """

    # Step 1: Build a frequency hash table from the magazine.
    # Each key is a character; each value is how many times it appears.
    char_count = {}
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Check whether the ransom note can be satisfied.
    # For every character needed, verify it exists and has supply remaining.
    for char in ransomNote:
        if char_count.get(char, 0) == 0:
            # Character is either absent or fully consumed — cannot construct.
            return False
        # Consume one use of this character from the available supply.
        char_count[char] -= 1

    # Step 3: All characters were successfully matched.
    return True