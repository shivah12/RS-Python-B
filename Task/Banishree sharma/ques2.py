class CharOccur:
	def __init__(self, character, occurrence):
		
		self.character = character
		self.occurrence = occurrence

def frequency(s: str):
	if not s:
		print("Empty string")
		return

	occurrences = []
	
    for c in s:
		found = False
		for occur in occurrences:
			
			if occur.character == c:
				occur.occurrence += 1
				found = True
				break
		if not found:
			occurrences.append(CharOccur(c, 1))

	# Printing the character - occurrences pair
	for occur in occurrences:
		print(occur.character, occur.occurrence)


s1 = "GFG"
print("For " + s1)
frequency(s1)

s2 = "aaabccccffgfghc"
print("For " + s2)
frequency(s2)


