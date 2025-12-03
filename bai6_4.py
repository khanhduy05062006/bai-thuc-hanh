
class py_solution:
    def roman_to_int(self, s):
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            
            if i + 1 < len(s) and roman_val[s[i]] < roman_val[s[i+1]]:
                int_val -= roman_val[s[i]]
            else:
                int_val += roman_val[s[i]]

        return int_val


sol = py_solution()

print(sol.roman_to_int("MMVIII"))   
print(sol.roman_to_int("MCMXC"))    
print(sol.roman_to_int("LVIII"))    
print(sol.roman_to_int("CM"))  
