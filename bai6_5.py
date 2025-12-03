
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
sol = py_solution()
print(sol.reverse_words("hello .py"))   
