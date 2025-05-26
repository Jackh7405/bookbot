
def word_count(file_path):
	num_words = 0
	with open(file_path) as f:
		file_contents = f.read()
		for word in file_contents.split():
			num_words +=1
	return num_words

def char_count(file_path):
	char_counts = {}
	with open(file_path) as f:
		file_contents = f.read()
		for word in file_contents.split():
			for char in (list(word)):
				if char.lower() not in char_counts:
					char_counts[char.lower()] = 1
				else:
					char_counts[char.lower()] += 1
	return char_counts

def sort_on(char_counts):
    return char_counts["num"]

def sort_dict(char_counts):
	sorted_chars = []
	for key, value in char_counts.items():	
		sorted_chars.append({"char": key, "num": value})	
	sorted_chars.sort(reverse=True, key=sort_on)
	return sorted_chars