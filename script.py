

def sort(width, height, length, mass):
    """
    Parameters
    ---------
    widht (cm): int
    height (cm): int
    length (cm): int
    mass (g): int

    Implementation Rules
    ---------

    dimensions = 1 -> not bulky
    dimensions = 2 -> bulky

    weight = 1 -> not heavy
    weight = 2 -> heavy

    dimensions + weight = 2 -> STANDARD
    dimensions + weight = 3 -> SPECIAL
    dimensions + weight > 3 -> REJECTED

    if any dimension is negative or zero the package is REJECTED
    if any dimension is not int the package is REJECTED

    """
    dimensions = None
    weight = None

    # Guard clause for data validation
    if not all(isinstance(x, int) for x in [width, height, length, mass]):
        return "REJECTED"
    if (width <= 0) or (height <= 0) or (length <= 0) or (mass <= 0):
        return "REJECTED"
    

    volume = width * height * length
    if volume >= 1000000:
        dimensions = 2
    elif (width >= 150) or (height >= 150) or (length >= 150):
        dimensions = 2
    else:
        dimensions = 1

    if mass >= 20000:
        weight = 2
    else:
        weight = 1

    label = dimensions + weight

    if label == 2:
        return "STANDARD"
    elif label == 3:
        return "SPECIAL"
    else:
        return "REJECTED"


# I used CHATGPT to create the main function with test some cases for validation
def main():
    print("Running test cases...\n")

    test_cases = [
        # STANDARD
        ((100, 100, 10, 10000), "STANDARD"),
        # SPECIAL: heavy
        ((100, 100, 10, 20000), "SPECIAL"),
        # SPECIAL: bulky
        ((150, 100, 100, 10000), "SPECIAL"),
        # SPECIAL: exactly 1,000,000 volume
        ((100, 100, 1000, 10000), "SPECIAL"),
        # REJECTED: bulky + heavy
        ((200, 200, 200, 30000), "REJECTED"),
        # Invalid: non-integer
        (("150", 100, 100, 10000), "REJECTED"),
        # Invalid: negative input
        ((100, -50, 100, 10000), "REJECTED"),
        # Invalid: zero mass
        ((100, 100, 100, 0), "REJECTED"),
    ]

    for i, (args, expected) in enumerate(test_cases):
        try:
            result = sort(*args)
            status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected}, got {result})"
        except Exception as e:
            if isinstance(e, expected):
                status = f"✅ PASS (raised {type(e).__name__})"
            else:
                status = f"❌ FAIL (raised {type(e).__name__}, expected {expected})"
        print(f"Test {i + 1}: {status}")

if __name__ == "__main__":
    main()