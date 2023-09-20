import datetime
import os
from Functions.homework_4 import *


class Records:
    def __init__(self):
        self.filename = "news_feed.txt"

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
        with open(self.filename, "a") as file:
            file.write(record)
            file.write("\n")

    def run(self):
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


class RecordProvider:
    def __init__(self, filename="default_records.txt"):
        self.filename = filename

    def process_records(self, num_records_to_process):
        if not os.path.isfile(self.filename):
            print(f"File '{self.filename}' not found.")
            return

        with open(self.filename, "r") as file:
            records = file.read().splitlines()

        print("Processing records:")
        processed_count = 0
        for record in records:
            processed_count += 1
            sentences = split_into_sentences(record)
            formatted_sentences = [format_sentence(sentence) for sentence in sentences]
            formatted_sentences = create_new_paragraph(formatted_sentences)
            print(formatted_sentences)
            if processed_count >= num_records_to_process:
                break

        remove_file = input(f"Do you want to remove the processed file '{self.filename}'? (yes/no): ").lower()
        if remove_file == "yes":
            os.remove(self.filename)
            print(f"{self.filename} removed.")
        else:
            print(f"{self.filename} not removed.")


if __name__ == "__main__":
    records_app = Records()
    records_app.run()

    file_path = "news_feed.txt"
    num_records = int(input("Enter the number of records to process: "))
    record_provider = RecordProvider(file_path)
    record_provider.process_records(num_records)
