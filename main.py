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


class Library:
    def __init__(self):
        # Convert dictionary data into Book objects
        self.books = [Book(**book) for book in library_books]

    def find_book(self, book_id):
        for book in self.books:
            if book.id.upper() == book_id.upper():
                return book
        return None

    def view_available_books(self):
        print("--- Available Books ---")
        found = False
        for book in self.books:
            if book.available:
                book.display()
                found = True
        if not found:
            print("No available books.")
        print("-----------------------")

    def view_all_books(self):
        print("--- Library Catalog ---")
        for book in self.books:
            book.display()
        print("-----------------------")

    def search(self, query):
        print(f"--- Search Results for '{query}' ---")
        found = False
        query_lower = query.lower()

        for book in self.books:
            # Check if query matches author or genre
            if query_lower in book.author.lower() or query_lower in book.genre.lower():
                book.display()
                found = True

        if not found:
            print("No books matched your search.")
        print("-----------------------")

    def checkout_book(self, book_id):
        book = self.find_book(book_id)
        if not book:
            return False, f"No book found with ID '{book_id}'."
        return book.checkout()

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if not book:
            return False, f"No book found with ID '{book_id}'."
        return book.return_book()

    def list_overdue(self):
        print("--- Overdue Books ---")
        today = datetime.now().date()
        found = False

        for book in self.books:
            if not book.available and book.due_date:
                due = datetime.strptime(book.due_date, "%Y-%m-%d").date() #https://docs.python.org/3/library/datetime.html documentation i used to learn date time
                if due < today:
                    book.display()
                    found = True

        if not found:
            print("No overdue books.")
        print("---------------------")

    def top_checkouts(self):
        print("--- Top 3 Most Checked-Out Books ---")
        top = sorted(self.books, key=lambda b: b.checkouts, reverse=True)[:3]

        for i, book in enumerate(top, start=1):
            print(f"{i}. {book.title} by {book.author} ({book.checkouts} checkouts)")

        print("-----------------------------------")


def main():
    library = Library()

    while True:
        print("====================================")
        print("     Library Management System      ")
        print("====================================")
        print("1. View available books")
        print("2. View all books")
        print("3. Search books by author or genre")
        print("4. Checkout a book")
        print("5. Return a book")
        print("6. View overdue books")
        print("7. View top 3 most checked-out books")
        print("8. Exit")
        print("====================================")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            library.view_available_books()

        elif choice == "2":
            library.view_all_books()

        elif choice == "3":
            query = input("Enter author or genre: ")
            library.search(query)

        elif choice == "4":
            book_id = input("Enter book ID to checkout: ")
            _, message = library.checkout_book(book_id)
            print(message)

        elif choice == "5":
            book_id = input("Enter book ID to return: ")
            _, message = library.return_book(book_id)
            print(message)

        elif choice == "6":
            library.list_overdue()

        elif choice == "7":
            library.top_checkouts()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number 1–8.")


if __name__ == "__main__":
    main()