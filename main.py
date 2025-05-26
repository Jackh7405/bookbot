from stats import word_count, char_count, sort_dict
import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

file_path = sys.argv[1] 

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
		return file_contents



def main():
	counts = char_count(file_path)
	sorted_chars = sort_dict(counts)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}")
	print("----------- Word Count ----------")
	print(f"Found {word_count(file_path)} total words")
	print("--------- Character Count -------")
	for char_dict in sorted_chars:
		if char_dict["char"].isalpha():
			print(f"{char_dict['char']}: {char_dict['num']}")
		
main()