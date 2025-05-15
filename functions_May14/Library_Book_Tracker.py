library = {}

def add_book(title, author, pages):
    if title in library:
        return "This book already exists in the library."
    else:
        library[title] = {"author": author, "pages": pages}
        return f"Book '{title}' by {author} added."

def find_book(title):
    if title in library:
        return library[title]
    else:
        return "Book not found."

def show_books():
    return list(library.keys())

