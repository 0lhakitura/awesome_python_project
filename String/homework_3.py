import re

pattern = r'\biz\b'  # \b: a word boundary anchor || r: raw string

original_text = """
    tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

whitespace_count = sum(1 for char in original_text if char.isspace())  # char.isspace() method checks whether a given character char is a whitespace character.

fixed_text = re.sub(pattern, 'is', original_text, flags=re.IGNORECASE)  # re.sub() performs regular expression-based substitutions in strings. re.IGNORECASE makes the pattern matching case-insensitive.
sentences = fixed_text.split('.')  # Each element in the resulting list will be a sentence from the original text.

formatted_sentences = []
last_words = []
for sentence in sentences:
    stripped_sentence = sentence.strip()  # sentence.strip() removes leading and trailing whitespace characters
    if stripped_sentence:
        formatted_sentence = stripped_sentence[0].capitalize() + stripped_sentence[1:].lower()  # stripped_sentence[0]: extracts the first character (character at index 0) of stripped_sentence. stripped_sentence[1:]: extracts the rest characters
        formatted_sentences.append(formatted_sentence)
        last_words.append(stripped_sentence.split()[-1])   # split(): splits a string into a list of substrings based on whitespace characters. After splitting the sentence, [-1] accesses the last element (the last word) of the resulting list.

new_sentence = " ".join(last_words) + "."
new_paragraph = '. '.join(formatted_sentences) + '.'  # '. '.join(formatted_sentences):  concatenates the sentences in the formatted_sentences list into a single string and places a period and a space ('. ') between each pair of sentences.

final_paragraph = new_paragraph + " " + new_sentence

print(final_paragraph)
print(f"Number of whitespace characters: {whitespace_count}")
