import datetime
import os
from Functions.homework_4 import *
import csv
import string


class Records:
    def __init__(self, input_filename="provided_records.txt"):
        self.output_filename = "news_feed.txt"
        self.input_filename = input_filename

    def create_news_record(self):
        text = input("Enter the news text: ")
        city = input("Enter the city: ")
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H.%M")
        return f"News -------------------------\n{text}\n{city}, {timestamp}\n"

    def create_private_ad_record(self):
        text = input("Enter the ad text: ")
        expiration_date = input("Enter the expiration date (dd/mm/yyyy): ")
        expiration_date = datetime.datetime.strptime(expiration_date, "%d/%m/%Y")
        days_left = (expiration_date - datetime.datetime.now()).days
        return f"Private Ad ------------------\n{text}\nActual until: {expiration_date.strftime('%d/%m/%Y')}, {days_left} days left\n"

    def create_custom_record(self):
        text = input("Enter the happy birthday wish: ")
        timestamp = datetime.datetime.now().strftime('%d %B')
        return f"Happy Birthday Wish ----------------\n{text}\n P.S. You see, I remember the day of your Birthday. It is {timestamp}!"

    def add_record(self, record):
        with open(self.output_filename, "a") as file:
            file.write(record)
            file.write("\n")
            word_csv_file = "word_count.csv"
            letter_csv_file = "letter_statistics.csv"
            stats_provider = TextAnalyzer(self.output_filename)
            stats_provider.analyze_text()
            stats_provider.create_word_csv(word_csv_file)
            stats_provider.create_letter_csv(letter_csv_file)

    def process_user_inputs(self):
        while True:
            print("1. Create News")
            print("2. Create Private Ad")
            print("3. Create Happy Birthday Wish")
            print("4. Quit")

            choice = input("Select a record type (1/2/3/4): ")

            if choice == '1':
                record = self.create_news_record()
            elif choice == '2':
                record = self.create_private_ad_record()
            elif choice == '3':
                record = self.create_custom_record()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            self.add_record(record)

    def process_text_file(self):
        file_path = self.get_file_path()
        if not file_path:
            return

        records = self.read_records(file_path)

        num_records_to_process = self.get_num_records_to_process()
        processed_count = 0

        for record in records:
            processed_count += 1
            sentences = split_into_sentences(record)
            formatted_sentences = [format_sentence(sentence) for sentence in sentences]
            formatted_sentences = create_new_paragraph(formatted_sentences)
            self.add_record(formatted_sentences)
            if processed_count >= num_records_to_process:
                break

        self.remove_processed_file()

    def get_file_path(self):
        file_path = input("Default folder? yes/no: ")
        if file_path.lower() == "yes":
            return self.input_filename
        else:
            return input("Provide your filepath: ")

    def read_records(self, file_path):
        try:
            with open(file_path, "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None

    def get_num_records_to_process(self):
        while True:
            try:
                num_records = int(input("Enter the number of records to process: "))
                return num_records
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def remove_processed_file(self):
        remove_file = input(f"Do you want to remove the processed file '{self.input_filename}'? (yes/no): ").lower()
        if remove_file == "yes":
            os.remove(self.input_filename)
            print(f"{self.input_filename} removed.")
        else:
            print(f"{self.input_filename} not removed.")




class TextAnalyzer:
    def __init__(self, text_file):
        self.text_file = text_file
        self.word_count = None
        self.letter_count = None
        self.uppercase_count = {}

    def analyze_text(self):
        with open(self.text_file, 'r') as file:
            text = file.read()
            words = text.split()
            self.word_count = len(words)

            text_cleaned = text.translate(str.maketrans('', '', string.punctuation))
            # text_cleaned = text_cleaned.lower()
            letter_count = {}
            for letter in text_cleaned:
                if letter.isalpha():
                    if letter.isupper():
                        if letter in self.uppercase_count:
                            self.uppercase_count[letter] += 1
                        else:
                            self.uppercase_count[letter] = 1
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1
            self.letter_count = letter_count

    def create_word_csv(self, word_csv_file):
        with open(word_csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['word', 'count'])

            with open(self.text_file, 'r') as text_file:
                text = text_file.read()
                word_count = {}
                words = text.split()
                for word in words:
                    word = word.strip(string.punctuation).lower()
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
                for word, count in word_count.items():
                    writer.writerow([word, count])

    def create_letter_csv(self, letter_csv_file):
        with open(letter_csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['letter', 'count', 'uppercase_count', 'percentage'])

            total_letters = sum(self.letter_count.values())
            for letter, count in self.letter_count.items():
                uppercase_count = self.uppercase_count.get(letter.upper(), 0)
                percentage = (count / total_letters) * 100 if total_letters > 0 else 0
                rounded_percentage = round(percentage, 2)
                writer.writerow([letter, count, uppercase_count, rounded_percentage])


if __name__ == "__main__":
    # text_file = 'news_feed.txt'
    # word_csv_file = 'word_count.csv'
    # letter_csv_file = 'letter_statistics.csv'
    #
    # analyzer = TextAnalyzer(text_file)
    # analyzer.analyze_text()
    # analyzer.create_word_csv(word_csv_file)
    # analyzer.create_letter_csv(letter_csv_file)

    records_app = Records()
    records_app.process_user_inputs()

    file_path = "provided_records.txt"
    # num_records = int(input("Enter the number of records to process: "))
    record_provider = Records(file_path)
    record_provider.process_text_file()
