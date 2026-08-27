class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in matches:
                stack.append(char)
            else:
                if not stack or stack[-1] != matches[char]:
                    return False

                stack.pop()

        return len(stack) == 0