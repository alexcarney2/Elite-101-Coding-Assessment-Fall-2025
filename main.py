from datetime import datetime, timedelta
from library_books import library_books


class Book:
    def __init__(self, id, title, author, genre, available, due_date, checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def display(self):
        status = "Available" if self.available else f"Checked Out (Due: {self.due_date})"
        print(f"{self.id} | {self.title} | {self.author} | {status}")

    def checkout(self):
        # Set due date 2 weeks from today and increment checkout count
        if not self.available:
            return False, f"'{self.title}' is already checked out (Due: {self.due_date})."

        due = datetime.now().date() + timedelta(weeks=2)
        self.available = False
        self.due_date = due.strftime("%Y-%m-%d")
        self.checkouts += 1

        return True, f"You checked out '{self.title}'. Due date: {self.due_date}"

    def return_book(self):
        # Reset availability and due date
        if self.available:
            return False, f"'{self.title}' is not currently checked out."

        self.available = True
        self.due_date = None
        return True, f"You returned '{self.title}'. Thank you!"


