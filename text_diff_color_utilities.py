"""
diff the strings and highlight in different colors, e.g. removed in red, add in green (amend), and change without lengthening in blue (emend)
"""
import difflib

red = lambda text: f"\033[38;2;255;0;0m{text}\033[38;2;255;255;255m"
green = lambda text: f"\033[38;2;0;255;0m{text}\033[38;2;255;255;255m"
blue = lambda text: f"\033[38;2;0;0;255m{text}\033[38;2;255;255;255m"
white = lambda text: f"\033[38;2;255;255;255m{text}\033[38;2;255;255;255m"
black = lambda text: f"\033[38;2;0;0;0m{text}\033[38;2;255;255;255m"

def get_edits_string(old, new):
    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    for code in codes:
        if code[0] == "equal":
            result += black(old[code[1]:code[2]])
        elif code[0] == "delete":
            result += red(old[code[1]:code[2]])
        elif code[0] == "insert":
            result += green(new[code[3]:code[4]])
        elif code[0] == "replace":
            result += (red(old[code[1]:code[2]]) + blue(new[code[3]:code[4]]))
    return result

# Usage
str1 = "The quick brown fox jumps over the lazy dog."
str2 = "The quick black dog jumps over the lazy cat."

diff = get_edits_string(str1, str2)
print(diff)

str1 = "The quick brown dog jumps quickly over the lazy cat."
str2 = "The quick black dog jumps over the lazy cat."

diff = get_edits_string(str1, str2)
print(diff)

diff = get_edits_string(str2, str1)
print(diff)


