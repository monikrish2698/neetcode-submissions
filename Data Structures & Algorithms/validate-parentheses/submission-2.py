class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        visit_stack = []
        for i in s:
            if i in char_dict and visit_stack:
                poped = visit_stack.pop()
                if poped != char_dict[i]:
                    return False
            else:
                visit_stack.append(i)
            
        return True if len(visit_stack) == 0 else False
        