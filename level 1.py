def print_all_books(books_list):
    if not books_list:
        print("There are no books currently in the system.")
        return

    print("--- Available Books (Simple Output) ---")

    for book in books_list:
        book_id = book.get('book_id', 'N/A')
        title = book.get('title', 'N/A')
        author = book.get('author', 'N/A')
        print(f"ID: {book_id}, Title: {title}, Author: {author}")
    
    print("---------------------------------------")


library_books = [
    {
        'book_id': 101,
        'title': 'The Hitchhiker\'s Guide to the Galaxy',
        'author': 'Douglas Adams'
    },
    {
        'book_id': 102,
        'title': '1984',
        'author': 'George Orwell'
    },
    {
        'book_id': 103,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen'
    }
]

print_all_books(library_books)