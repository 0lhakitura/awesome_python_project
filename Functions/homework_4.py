import re


def count_whitespace(text):
    return sum(1 for char in text if char.isspace())


def fix_spelling_mistake(text):
    pattern = r'\biz\b'
    return re.sub(pattern, 'is', text, flags=re.IGNORECASE)


def split_into_sentences(text):
    return text.split('.')


def format_sentence(sentence):
    stripped_sentence = sentence.strip()
    if stripped_sentence:
        return stripped_sentence[0].capitalize() + stripped_sentence[1:].lower()
    else:
        return ''


def extract_last_words(sentences):
    last_words = []
    for sentence in sentences:
        words = sentence.split()
        if words:
            last_words.append(words[-1])
    return last_words


def create_new_sentence(last_words):
    return " ".join(last_words) + "."


def create_new_paragraph(formatted_sentences):
    return '. '.join(formatted_sentences) + '.'


def main():
    original_text = """tHis iz your homeWork, copy these Text to variable. You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

    # Count whitespace characters
    whitespace_count = count_whitespace(original_text)

    # Fix spelling mistake
    fixed_text = fix_spelling_mistake(original_text)

    # Split text into sentences
    sentences = split_into_sentences(fixed_text)

    # Format each sentence
    formatted_sentences = [format_sentence(sentence) for sentence in sentences]

    # Extract last words from sentences
    last_words = extract_last_words(sentences)

    # Create a new sentence and a new paragraph
    new_sentence = create_new_sentence(last_words)
    new_paragraph = create_new_paragraph(formatted_sentences)

    # Combine the new sentence and new paragraph
    final_paragraph = new_paragraph + " " + new_sentence

    print(final_paragraph)
    print(f"Number of whitespace characters: {whitespace_count}")


if __name__ == "__main__":
    main()
