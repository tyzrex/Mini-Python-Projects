from bs4 import BeautifulSoup as soup
import requests
from simple_term_menu import TerminalMenu
import os


class WebScraper:
    def __init__(self):
        self.fourth_semester_subjects = ["toc", "os", "dbms", "ai", "cn"]
        self.toc_chapter_keywords = {
            "Chapter 1": ["introduction", "prefix", "suffix"],
            "Chapter 2": ["finite automata", "dfa", "nfa", "extended transition function", "conversion", "nfa to dfa", "dfa to nfa"],
            "Chapter 3": ["regular grammar", "regular expression", "regular language", "expression", "regular"],
            "Chapter 4": ["context free grammar", "cfg", "pda", 'chomsky normal form', 'cnf'],
            "Chapter 5": ["pushdown automata", "pda"],
            "Chapter 6": ["turing machine", "tm", "turning machine"],
            "Chapter 7": ["undecidability", "halting problem"],
        }

    def get_all_questions(self, url):
        results = []
        data_html = requests.get(url)
        data_soup = soup(data_html.text, "html.parser")
        question_container = data_soup.find_all('div', class_='qnbank_content')
        for question in question_container:
            question = question.find_all('p')
            for q in question:
                results.append(q.text)
        return results

    def write_to_file(self, questions):
        with open("questions.md", "w") as question_file:
            question_file.write("# Questions\n\n")
            for question in questions:
                chapter = self.identify_chapter(question)
                question_file.write("## " + chapter + "\n\n")
                question_file.write("- " + question + "\n\n")

    def get_subjects_year(self):
        print("Enter your semester: ")
        user_semester = "fourth"
        print("Enter the subject which you want to scrape: ")
        subject = TerminalMenu(self.fourth_semester_subjects).show()

        print("Enter the year: ")
        options = ["2079", "2078", "2076"]
        year = TerminalMenu(options).show()

        print("You have selected: ")
        print(f"Semester: {user_semester}")
        print(f"Subject: {self.fourth_semester_subjects[subject]}")
        print(f"Year: {options[year]}")

        return user_semester, options[year], self.fourth_semester_subjects[subject]

    def identify_chapter(self, text):
        text = text.lower()
        for chapter, keywords in self.toc_chapter_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return chapter
        return "Unknown Chapter"

    def merge_questions_from_file(self):
        merged_questions = []
        with open("questions.md", "r") as file:
            lines = file.readlines()
            chapter = None
            for line in lines:
                if line.startswith("##"):
                    chapter = line.strip("##").strip()
                elif line.startswith("-"):
                    merged_questions.append((chapter, line.strip("-").strip()))

        merged_questions.sort(key=lambda x: x[0])
        return merged_questions

    def scrape_questions(self):
        semester, year, subject = self.get_subjects_year()
        url = f"https://hamrocsit.com/semester/{semester}/{subject}/question-bank/{year}"
        questions = self.get_all_questions(url)
        self.write_to_file(questions)

    def print_sorted_questions(self):
        merged_questions = self.merge_questions_from_file()
        chapters = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6", "Chapter 7",
                    "Unknown Chapter"]

        with open("sorted_questions.md", "w") as file:
            for chapter in chapters:
                file.write("# " + chapter + "\n")
                print("===", chapter, "===")
                for chap, question in merged_questions:
                    if chap == chapter:
                        file.write("- " + question + "\n")
                        print(question)
                print("--------------------")


scraper = WebScraper()
scraper.scrape_questions()
scraper.print_sorted_questions()

os.system(
    "mdpdf -o sorted_questions.pdf sorted_questions.md"
)
