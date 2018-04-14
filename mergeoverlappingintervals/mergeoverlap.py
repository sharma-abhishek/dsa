a = [(1,3), (8,11), (2,6)]

b = sorted(a, key=lambda x: x[0])
time = list()

i = 0

def isOverlap(current, top):
    if current[0] >= top[0] and current[0] <= top[1]:
        return (top[0], current[1])
    else:
        return None

while i < len(b):
    current = b[i]
    if len(time) == 0:
        time.append(current)
    else:
        top = time.pop()
        merge = isOverlap(current, top)
        if merge is None:
            time.append(top)
            time.append(current)
        else:
            time.append(merge)
    i = i + 1

print time