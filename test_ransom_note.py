from ransom_note import can_construct

def test_basic_false():
    """Letters in magazine don't cover the note."""
    assert can_construct("a", "b") == False

def test_insufficient_count():
    """Magazine has the letter but not enough copies."""
    assert can_construct("aa", "ab") == False

def test_basic_true():
    """Magazine contains exactly the right letters."""
    assert can_construct("aa", "aab") == True

def test_empty_note():
    """An empty ransom note can always be constructed."""
    assert can_construct("", "anything") == True

def test_empty_magazine():
    """A non-empty note cannot be built from an empty magazine."""
    assert can_construct("a", "") == False

def test_exact_match():
    """Magazine and note are identical."""
    assert can_construct("hello", "hello") == True

def test_extra_letters_in_magazine():
    """Magazine has more than enough letters."""
    assert can_construct("note", "thequickbrownfoxnote") == True

def test_case_sensitive():
    """Uppercase and lowercase are treated as different characters."""
    assert can_construct("A", "a") == False

def test_spaces():
    """Spaces count as characters too."""
    assert can_construct("hi there", "hi there friend") == True

if __name__ == "__main__":
    tests = [
        test_basic_false,
        test_insufficient_count,
        test_basic_true,
        test_empty_note,
        test_empty_magazine,
        test_exact_match,
        test_extra_letters_in_magazine,
        test_case_sensitive,
        test_spaces,
    ]

    passed = 0
    for test in tests:
        try:
            test()
            print(f"  PASS  {test.__name__}")
            passed += 1
        except AssertionError:
            print(f"  FAIL  {test.__name__}")

    print(f"\n{passed}/{len(tests)} tests passed.")