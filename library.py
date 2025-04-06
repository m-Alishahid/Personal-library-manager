import json
import os

LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    original_len = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]
    if len(library) < original_len:
        print("🗑️ Book removed successfully!\n")
    else:
        print("⚠️ Book not found.\n")

def search_books(library):
    keyword = input("Search by title or author: ").strip().lower()
    results = [book for book in library if keyword in book['title'].lower() or keyword in book['author'].lower()]
    if results:
        print(f"\n🔍 Found {len(results)} matching book(s):")
        for book in results:
            display_book(book)
    else:
        print("😕 No matching books found.\n")

def display_books(library):
    if not library:
        print("📚 No books in the library yet.\n")
        return
    print(f"\n📘 Listing {len(library)} book(s):")
    for book in library:
        display_book(book)

def display_book(book):
    read_status = "✅ Read" if book["read"] else "📖 Unread"
    print(f'''
    Title : {book["title"]}
    Author: {book["author"]}
    Year  : {book["year"]}
    Genre : {book["genre"]}
    Status: {read_status}
    ''')

def display_stats(library):
    total = len(library)
    if total == 0:
        print("📊 No books to analyze.\n")
        return
    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total) * 100
    print(f'''
📚 Total books   : {total}
📖 Books read    : {read_books}
📈 Read percent  : {percent_read:.2f}%
''')

def main():
    library = load_library()
    
    while True:
        print('''
======== 📚 Library Manager (create by Ali shahid)========
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
''')
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_stats(library)
        elif choice == '6':
            save_library(library)
            print("💾 Library saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()