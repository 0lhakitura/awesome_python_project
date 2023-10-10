import datetime
import json
import os
from Functions.homework_4 import *
import csv
import string
import xml.etree.ElementTree as ET


class Record:
    def __init__(self):
        self.timestamp = datetime.datetime.now()

    def formatted_record(self):
        raise NotImplementedError("Subclasses should implement this method.")


class NewsRecord(Record):
    def __init__(self, text, city):
        super().__init__()
        self.text = text
        self.city = city

    def formatted_record(self):
        timestamp_str = self.timestamp.strftime("%d/%m/%Y %H.%M")
        return f"News -------------------------\n{self.text}\n{self.city}, {timestamp_str}\n"


class PrivateAdRecord(Record):
    def __init__(self, text, expiration_date):
        super().__init__()
        self.text = text
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%d/%m/%Y")

    def formatted_record(self):
        days_left = (self.expiration_date - self.timestamp).days
        expiration_date_str = self.expiration_date.strftime("%d/%m/%Y")
        return f"Private Ad ------------------\n{self.text}\nActual until: {expiration_date_str}, {days_left} days left\n"


class BirthdayWishRecord(Record):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def formatted_record(self):
        timestamp_str = self.timestamp.strftime("%d %B")
        return f"Happy Birthday Wish ----------------\n{self.text}\nP.S. You see, I remember the day of your Birthday. It is {timestamp_str}!"


class RecordsProcessor:
    def __init__(self, input_filename="provided_records.txt", output_filename="news_feed.txt"):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def get_file_path(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def get_records_from_file(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def add_record(self, record):
        with open(self.output_filename, "a") as file:
            formatted_record = record.formatted_record()
            file.write(formatted_record)
            file.write("\n")
            stats_provider = TextAnalyzer(self.output_filename)
            stats_provider.analyze_text()
            stats_provider.create_word_csv("word_count.csv")
            stats_provider.create_letter_csv("letter_statistics.csv")

    def remove_processed_file(self):
        remove_file = input(f"Do you want to remove the processed file '{self.input_filename}'? (yes/no): ").lower()
        if remove_file == "yes":
            os.remove(self.input_filename)
            print(f"{self.input_filename} removed.")
        else:
            print(f"{self.input_filename} not removed.")

    def process_and_add_record(self, record):
        sentences = split_into_sentences(record)
        formatted_sentences = [format_sentence(sentence) for sentence in sentences]
        formatted_paragraph = create_new_paragraph(formatted_sentences)
        self.add_record(formatted_paragraph)

    def get_num_records_to_process(self):
        while True:
            try:
                num_records = int(input("Enter the number of records to process: "))
                return num_records
            except ValueError:
                print("Invalid input. Please enter a valid number.")


class UserInputs(RecordsProcessor):
    def __init__(self, output_filename="news_feed.txt"):
        super().__init__(output_filename)
        self.output_filename = output_filename

    def process_user_inputs(self):
        while True:
            print("1. Create News")
            print("2. Create Private Ad")
            print("3. Create Happy Birthday Wish")
            print("4. Quit")

            choice = input("Select a record type (1/2/3/4): ")

            if choice == '1':
                text = input("Enter the news text: ")
                city = input("Enter the city: ")
                record = NewsRecord(text, city)
            elif choice == '2':
                text = input("Enter the ad text: ")
                expiration_date = input("Enter the expiration date (dd/mm/yyyy): ")
                record = PrivateAdRecord(text, expiration_date)
            elif choice == '3':
                text = input("Enter the happy birthday wish: ")
                record = BirthdayWishRecord(text)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            self.add_record(record)


class JSONRecordsProcessor(RecordsProcessor):
    def __init__(self, input_filename="provided_records.json"):
        super().__init__(input_filename)
        self.input_filename = input_filename

    def get_records_from_file(self, file_path):
        try:
            with open(file_path, "r") as json_file:
                records_data = json.load(json_file)
            return records_data
        except FileNotFoundError:
            print(f"JSON file '{file_path}' not found.")
            return None

    def get_file_path(self):
        use_default = input("Use default JSON file path? (yes/no): ").lower()
        if use_default == "yes":
            return self.input_filename
        else:
            custom_file_path = input("Enter custom JSON file path: ")
            return custom_file_path

    def process_file(self):
        json_file_path = self.get_file_path()
        records_data = self.get_records_from_file(json_file_path)

        num_records_to_process = self.get_num_records_to_process()

        processed_count = 0

        if not records_data:
            return

        for record_type, record_content in records_data.items():
            if processed_count >= num_records_to_process:
                break
            if record_type == "news":
                record = NewsRecord(record_content["text"], record_content["city"])
            elif record_type == "private_ad":
                record = PrivateAdRecord(record_content["text"], record_content["expiration_date"])
            elif record_type == "birthday_wish":
                record = BirthdayWishRecord(record_content["text"])
            else:
                print(f"Invalid record type '{record_type}' in JSON file.")
                continue

            self.add_record(record)
            processed_count += 1

        self.remove_processed_file()


class XMLRecordsProcessor(RecordsProcessor):
    def __init__(self, input_filename="provided_records.xml"):
        super().__init__(input_filename)
        self.input_filename = input_filename

    def get_records_from_file(self, file_path):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            records_data = {}

            for record_element in root:
                record_type = record_element.tag
                record_content = {}
                for field_element in record_element:
                    record_content[field_element.tag] = field_element.text
                records_data[record_type] = record_content

            return records_data
        except FileNotFoundError:
            print(f"XML file '{self.input_filename}' not found.")
            return None

    def get_file_path(self):
        use_default = input("Use default file path? (yes/no): ").lower()
        if use_default == "yes":
            return self.input_filename
        else:
            custom_file_path = input("Enter custom file path: ")
            return custom_file_path



    def process_file(self):
        xml_file_path = self.get_file_path()
        records_data = self.get_records_from_file(xml_file_path)

        num_records_to_process = self.get_num_records_to_process()

        processed_count = 0


        if not records_data:
            return

        for record_type, record_content in records_data.items():
            if processed_count >= num_records_to_process:
                break
            if record_type == "news":
                record = NewsRecord(record_content["text"], record_content["city"])
            elif record_type == "private_ad":
                record = PrivateAdRecord(record_content["text"], record_content["expiration_date"])
            elif record_type == "birthday_wish":
                record = BirthdayWishRecord(record_content["text"])
            else:
                print(f"Invalid record type '{record_type}' in XML file.")
                continue

            self.add_record(record)
            processed_count += 1

        self.remove_processed_file()


class TextRecordsProcessor(RecordsProcessor):
    def __init__(self, input_filename="provided_records.txt"):
        super().__init__(input_filename)
        self.input_filename = input_filename

    record_type_mapping = {
        "news": NewsRecord,
        "private_ad": PrivateAdRecord,
        "birthday_wish": BirthdayWishRecord,
    }

    def get_records_from_file(self, file_path):
        try:
            with open(file_path, "r") as text_file:
                records_data = text_file.readlines()
            return records_data
        except FileNotFoundError:
            print(f"Text file '{file_path}' not found.")
            return None

    def get_file_path(self):
        use_default = input("Use default file path? (yes/no): ").lower()
        if use_default == "yes":
            return self.input_filename
        else:
            custom_file_path = input("Enter custom file path: ")
            return custom_file_path

    def process_file(self):
        text_file_path = self.get_file_path()
        records_data = self.get_records_from_file(text_file_path)

        if not records_data:
            return

        num_records_to_process = self.get_num_records_to_process()
        processed_count = 0

        for record in records_data:
            processed_count += 1
            record_type, record_content = self.parse_record(record)

            if not record_type:
                print(f"Invalid record type '{record_type}' in text file.")
            else:
                record_class = self.record_type_mapping.get(record_type)
                if record_class:
                    try:
                        if record_type == "news":
                            text_parts = record_content.split(": ", 1)
                            if len(text_parts) == 2:
                                text = text_parts[1]
                                city_parts = text_parts[0].split(" in ")
                                city = city_parts[-1] if len(city_parts) > 1 else ""
                                record = NewsRecord(text, city)
                        elif record_type == "private_ad":
                            text_parts = record_content.split(": ", 1)
                            if len(text_parts) == 2:
                                text = text_parts[1]
                                expiration_parts = text_parts[0].split(" - Expires on ")
                                expiration_date = expiration_parts[-1] if len(expiration_parts) > 1 else ""
                                record = PrivateAdRecord(text, expiration_date)
                        elif record_type == "birthday_wish":
                            record = BirthdayWishRecord(record_content)

                        if isinstance(record, Record):
                            self.process_and_add_record(record)
                        else:
                            print(f"Invalid {record_type} record format: {record}")
                    except Exception as e:
                        print(f"Error creating {record_type} record: {e}")
                else:
                    print(f"Invalid record type '{record_type}' in text file.")

            if processed_count >= num_records_to_process:
                break

        self.remove_processed_file()

    def parse_record(self, record):
        parts = record.split(": ", 1)
        if len(parts) == 2:
            return parts[0].lower(), parts[1]
        return None, None


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
    # analyzer = TextAnalyzer(text_file)
    # analyzer.analyze_text()
    # analyzer.create_word_csv(word_csv_file)
    # analyzer.create_letter_csv(letter_csv_file)

    # records_app = UserInputs()
    # records_app.process_user_inputs()

    # file_path = "provided_records.txt"
    # num_records = int(input("Enter the number of records to process: "))
    # record_provider = TextRecordsProcessor()
    # record_provider.process_file()
    records_json = JSONRecordsProcessor()
    records_json.process_file()
    # records_xml = XMLRecordsProcessor()
    # records_xml.process_file()


