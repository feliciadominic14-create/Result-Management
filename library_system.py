books_data = {
    "B101": {"title": "Python Basics", "author": "Anu", "copies": 2},
    "B102": {"title": "Data Science 101", "author": "Binu", "copies": 1},
    "B103": {"title": "AWS Guide", "author": "Cathy", "copies": 3},
    "B104": {"title": "Statistics Made Easy", "author": "Dev", "copies": 1},
}
 
members_data = [
    {"id": "M1", "name": "Anu", "type": "student"},
    {"id": "M2", "name": "Binu", "type": "teacher"},
    {"id": "M3", "name": "Cathy", "type": "student"},
]
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__copies = copies 
 
    def available_copies(self):
        return self.__copies
 
    def issue(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        return False
 
    def give_back(self):
        self.__copies += 1
 
    def __str__(self):
        return f"{self.book_id} | {self.title} by {self.author} | Copies: {self.__copies}"
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed = []
 
    def max_books(self):
        return 1
 
    def member_type(self):
        return "Member"
 
    def can_borrow(self):
        return len(self.borrowed) < self.max_books()
 
    def __str__(self):
        return (f"{self.member_id} | {self.name} | {self.member_type()} | "
                f"Borrowed: {len(self.borrowed)}/{self.max_books()}")
 
 
class Student(Member):
    def max_books(self):
        return 2
 
    def member_type(self):
        return "Student"
 
 
class Teacher(Member):
    def max_books(self):
        return 4
 
    def member_type(self):
        return "Teacher"
 
 

class Guest(Member):
    def max_books(self):
        return 1
 
    def member_type(self):
        return "Guest"
 
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
 
    def load_books(self, data):
        for book_id, info in data.items():
            self.books[book_id] = Book(book_id, info["title"], info["author"], info["copies"])
 
    def load_members(self, data):
        for m in data:
            kind = m["type"].lower()
            if kind == "teacher":
                self.members[m["id"]] = Teacher(m["id"], m["name"])
            elif kind == "guest":
                self.members[m["id"]] = Guest(m["id"], m["name"])
            else:
                self.members[m["id"]] = Student(m["id"], m["name"])
 
    def issue_book(self, member_id, book_id):
        if member_id not in self.members:
            return "Member not found"
        if book_id not in self.books:
            return "Book not found"
        member = self.members[member_id]
        book = self.books[book_id]
        if not member.can_borrow():
            return f"{member.name} has reached the limit"
        if not book.issue():
            return f"{book.title} is not available"
        member.borrowed.append(book_id)
        return f"{member.name} issued {book.title}"
 
    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member is None or book is None or book_id not in member.borrowed:
            return "Cannot return"
        member.borrowed.remove(book_id)
        book.give_back()
        return f"{member.name} returned {book.title}"
 
    def show_books(self):
        for book in self.books.values():
            print(book)
 
    def show_members(self):
        for member in self.members.values():
            print(member)
 
    def search(self, keyword):
        keyword = keyword.lower()
        return [b.title for b in self.books.values() if keyword in b.title.lower()]
 
    def members_with_books(self):
        return [m.name for m in self.members.values() if m.borrowed]
 
 
if __name__ == "__main__":
    library = Library()
    library.load_books(books_data)
    library.load_members(members_data)
    print("Task 1: Book catalogue")
    library.show_books()
    print("\nTask 2: Members")
    library.show_members()
    print("\nTask 3: Issue books")
    print(library.issue_book("M1", "B101"))
    print(library.issue_book("M1", "B102"))
    print(library.issue_book("M1", "B103"))
    print(library.issue_book("M3", "B102"))
    print(library.issue_book("M3", "B999"))
    print("\nTask 4: Teacher borrows")
    for bid in ["B101", "B103", "B104", "B102"]:
        print(library.issue_book("M2", bid))
    print(library.members["M2"])
    print("\nTask 5: Return books")
    print(library.return_book("M1", "B102"))
    print(library.return_book("M1", "B102"))
    print(library.issue_book("M3", "B102"))
    print("\nTask 6: Final status")
    library.show_books()
    library.show_members()
    total = sum(len(m.borrowed) for m in library.members.values())
    print(f"Books on loan: {total}")
    print("Challenge")
    print(library.search("data"))
    print(library.members_with_books())
 