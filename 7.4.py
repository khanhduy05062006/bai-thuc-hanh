text = """
Python is a powerful programming language that allows developers 
to build efficient applications quickly and effectively.
"""


words = [word.strip(".,!?;:()") for word in text.split()]


max_len = max(len(word) for word in words)


longest_words = [word for word in words if len(word) == max_len]

print("Độ dài lớn nhất:", max_len)
print("Những từ dài nhất:", longest_words)


