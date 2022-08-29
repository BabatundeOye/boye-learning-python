
message = input('enter a message')

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalize:", message.capitalize())
print("Title Case:", message.title())

words = message.split()
print("Words:", words)

sorted = sorted(words)
print("Alphabetic First Word:", sorted[0])
print("Alphabetic Lsst Word:", sorted[-1])