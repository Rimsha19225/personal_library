import json
import os

class PersonalLibraryManager:
    def __init__(self):
        self.library = []

    def add_book(self, title, author, year, genre, read):
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read
        }
        self.library.append(book)

    def remove_book(self, title):
        original_len = len(self.library)
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        return original_len != len(self.library)

    def search_book(self, query, search_by="title"):
        return [book for book in self.library if query.lower() in book[search_by].lower()]

    def view_books(self):
        return self.library

    def get_statistics(self):
        total_books = len(self.library)
        read_books = len([book for book in self.library if book["read"]])
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        return total_books, percentage_read

    def save_library(self, filename="library.json"):
        try:
            with open(filename, 'w') as f:
                json.dump(self.library, f, indent=4)
        except Exception as e:
            print(f"Error saving library: {e}")

    def load_library(self, filename="library.json"):
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.library = json.load(f)
            except Exception as e:
                print(f"Error loading library: {e}")

def main():
    manager = PersonalLibraryManager()
    manager.load_library()

    while True:
        print("\n📚 Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Save & Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            genre = input("Genre: ")
            read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
            if year.isdigit():
                manager.add_book(title, author, int(year), genre, read)
                print("✅ Book added.")
            else:
                print("❌ Invalid year. Book not added.")

        elif choice == "2":
            title = input("Enter the title to remove: ")
            if manager.remove_book(title):
                print("✅ Book removed.")
            else:
                print("❌ Book not found.")

        elif choice == "3":
            field = input("Search by (title/author): ").strip().lower()
            query = input("Enter your query: ")
            results = manager.search_book(query, field)
            if results:
                print("\n🔍 Matching Books:")
                for book in results:
                    read_status = "Read" if book["read"] else "Unread"
                    print(f"- {book['title']} by {book['author']} ({book['year']}) [{book['genre']}] - {read_status}")
            else:
                print("⚠️ No matching books found.")

        elif choice == "4":
            books = manager.view_books()
            if books:
                print("\n📖 All Books:")
                for i, book in enumerate(books, 1):
                    read_status = "Read" if book["read"] else "Unread"
                    print(f"{i}. {book['title']} by {book['author']} ({book['year']}) [{book['genre']}] - {read_status}")
            else:
                print("📭 Your library is empty.")

        elif choice == "5":
            total, percentage = manager.get_statistics()
            print(f"\n📊 Total Books: {total}")
            print(f"✅ Percentage Read: {percentage:.1f}%")

        elif choice == "6":
            manager.save_library()
            print("📁 Library saved. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
