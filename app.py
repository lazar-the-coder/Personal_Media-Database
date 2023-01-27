from models import Base, Book, session, engine
import datetime

def menu():
    print('''
        \nBooks Database
        \r1) View Books
        \r2) Add Book
        \r3) Search Books
        \r4) Exit''')
    while True:
        try:
            choice = int(input('What do you want to do?   '))
        except ValueError:
            print('please enter a number.')
        else:
            if choice > 4 or choice < 1:
                print('please enter a number between 1 and 5.')
            else:
                return choice

def app():
    app_running = True
    while app_running:
        choice = menu()
        match choice:
            case 1:
                show_books()
            case 2:
                add_book()
            case 3:
                search_book()
            case 4:
                print('goodbye')
                app_running = False

def add_book():
    while True:
        title = input('Title: ').title()
        writer = input('Writer (Author): ').title()
        visionary = input('Visionary (Artist or Director): ').title()
        medium = input('Medium ').title()
        genre = input('Genres (Separate by Commas) ').title()
        date = input('Year Published (YYYY-MM-DD) ')
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            print('Sorry, didn\'t understand')
        try:
            item_adder([title, writer, visionary, medium, genre, date])
        except ValueError:
            print('sorry, didn\'t understand what you entered.')
            try_again = input('Would you like to try again, or return to the main menu? (q to return, enter to try again) ')
            if try_again == 'q':
                return
        else:
            print('Added successfully')
            session.commit()
            return

def item_adder(item):
    book_title, book_writer, book_visionary, book_medium, book_genre, book_date = item[0:]
    new_book = Book(
        title=book_title,
        writer=book_writer,
        visionary=book_visionary,
        date=book_date,
        medium=book_medium,
        status="To Read",
        genre=book_genre
        )
    session.add(new_book)

def show_books():
    for book in session.query(Book).all():
        print(book)

def search_book():
    print('''
        \r1) Title
        \r2) Writer
        \r3) Visionary
        \r4) Medium
        \r5) Century
        \r6) Genre
        \r7) Quit''')
    while True:
        try:
            choice = int(input('What do you want to do?   '))
        except ValueError:
            print('please enter a number.')
        else:
            if choice > 7 or choice < 1:
                print('please enter a number between 1 and 5.')
            else:
                break
    match choice:
        case 1:
            piece = Book.title
            choice_2 = input("Enter full title or a part  ").title()
        case 2:
            piece =  Book.writer
            choice_2 = input("Enter first or last name of writer  ").title()
        case 3:
            piece =  Book.visionary
            choice_2 = input("Enter first or last name of visionary  ").title()
        case 4:
            piece = Book.medium
            choice_2 = input("Enter medium  ").title()
        case 5:
            piece = Book.date
            choice_2 = input("Enter date  (YYYY)  ")
        case 6:
            piece = Book.genre
            choice_2 = input("Enter a genre  ").title()
        case 7:
            return
    if type(choice_2) == str:
        for book in session.query(Book).filter(piece.like("%" + choice_2 + "%")).all():
            print(book)
    else:
        for book in session.query(Book).filter(piece.like(choice_2 + "%")).all():
            print(book)

def start():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    start()
    app()