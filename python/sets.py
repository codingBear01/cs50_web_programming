# Create an empty set
s = set()

# Add elements to set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)  # set은 elment를 중복해서 가질 수 없음. 따라서 4는 하나만 존재.
s.remove(4)
print(s)

print(f"The set has {len(s)} elements.")
