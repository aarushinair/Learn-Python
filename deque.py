import collections
days = collections.deque(["Mon","Tue","Wed"])
print (days)

print("Adding to the right: ")
days.append("Thu")
print (days)

print("Adding to the left: ")
days.appendleft("Sun")
print (days)

print("Removing from the right: ")
days.pop()
print (days)

print("Removing from the left: ")
days.popleft()
print (days)

print("Reversing the deque: ")
days.reverse()
print (days)
