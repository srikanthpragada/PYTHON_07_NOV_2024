st = "how do you do"

chars = {}  # Empty dict
for c in set(st):
    chars[c] = st.count(c)

print(chars)
