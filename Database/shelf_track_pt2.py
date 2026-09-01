import sqlite3

db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

cursor.execute('''DROP TABLE IF EXISTS book''')
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER(4) PRIMARY KEY,
        title TEXT,
        authorID INTEGER(4),
        qty INTEGER
    )'''
    )
db.commit()
'''Create table'''

books = [
    (3001, 'A Tale of Two Cities', 1290, 30),
    (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
    (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
    (3004, 'The Lord of the Rings', 6380, 37),
    (3005, "Alice's Adventures in Wonderland", 5620, 12)
]

cursor.executemany(
    '''
    INSERT INTO book(id, title, authorID, qty)
    VALUES(?, ?, ?, ?)
    ''',
    books
    )
print("\nBook info added to table")
db.commit()
'''Add books into table'''
'''Complete book section'''

cursor.execute('''DROP TABLE IF EXISTS author''')
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS author (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country INTEGER
    )'''
    )
db.commit()
'''Create table'''

authors = [
    (1290, 'Charles Dickens', 'England'),
    (8937, 'J.K. Rowling', 'England'),
    (2356, 'C.S. Lewis', 'Ireland'),
    (6380, 'J.R.R. Tolkien', 'South Africa'),
    (5620, 'Lewis Carroll', 'England')
]

cursor.executemany(
    '''
    INSERT INTO author(id, name, country)
    VALUES(?, ?, ?)
    ''',
    authors
    )
print("\nAuthor info added to table")
db.commit()
'''Add authors into table'''
'''Complete authors section'''

menu = (
    '''\nChoose an option from the menu below:
    1. Enter/Add book
    2. Update book
    3. Delete book
    4. Search books
    5. View all book details
    0. Exit
    : '''
)


def display_authorID(self):
    query = '''SELECT book.id, book.qty, book.title,
                    book.authorID, name, country FROM author
                    INNER JOIN book on book.authorID = author.id
                    WHERE book.authorID = ?'''
    cursor.execute(query, ((self),))
    look = cursor.fetchone()
    if look:
        print(f'''Book information:
              Book ID: {look[0]}
              Book qty: {look[1]}
              Book Title: {look[2]}
              Book Author ID: {look[3]}
              Book Author: {look[4]}
              Book Author Country: {look[5]}''')
    else:
        print("Unsuccessful. Please try again.")


def display_bookID(self):
    query = '''SELECT book.id, book.qty, book.title,
                    book.authorID, name, country FROM author
                    INNER JOIN book on book.authorID = author.id
                    WHERE book.id = ?'''
    cursor.execute(query, ((self),))
    look = cursor.fetchone()
    if look:
        print(f'''Book information:
              Book ID: {look[0]}
              Book qty: {look[1]}
              Book Title: {look[2]}
              Book Author ID: {look[3]}
              Book Author: {look[4]}
              Book Author Country: {look[5]}''')
    else:
        print("Unsuccessful. Please try again.")


def display_all():
    cursor.execute('''SELECT book.id, book.qty, book.title, book.authorID,
                name, country FROM author
                INNER JOIN book on book.authorID = author.id''')
    all = cursor.fetchall()
    if all:
        for x in all:
            print("-" * 30)
            print(f"Title: {x[2]}")
            print(f"Author's name: {x[4]}")
            print(f"Author country: {x[5]}")
    else:
        print("Unable to display all books")


while True:
    try:
        option = int(input(menu))
        '''Request user input from menu'''
    except (TypeError, ValueError):
        print("That is not an integer. Try again.")

    if option == 1:  # Add book
        new_title = input("Book title: ")
        try:
            while True:
                new_id = int(input("Book ID #(4 digits): "))
                new_authorID = int(input("Author ID #(4 digits): "))
                if new_id > 999 and new_id < 10000:
                    if new_authorID > 999 and new_authorID < 10000:
                        break
                    else:
                        print("Id and authorID must be 4 integers")
                else:
                    print("Id and authorID must be 4 integers")

            new_qty = int(input("Quantity: "))
        except (TypeError, ValueError):
            print("That is not an integer. Try again.")

        new_name = input("Author name: ")
        new_country = input("Author country: ")

        '''request info for new book and author'''
        new_b = (new_id, new_title, new_authorID, new_qty)
        new_a = (new_authorID, new_name, new_country)

        cursor.execute('''
            INSERT INTO book(id, title, authorID, qty)
            VALUES(?, ?, ?, ?)''', (new_b))
        db.commit
        '''Update Book table'''

        cursor.execute('''
            INSERT INTO author(id, name, country)
            VALUES(?, ?, ?)''', (new_a))
        db.commit
        '''Update Author table'''

        display_authorID(new_authorID)
        '''display updated book info'''

        '''Confirm addition'''

    elif option == 2:  # Update book
        while True:
            try:
                id = int(input("Enter book ID # to update: "))
                cursor.execute('''SELECT book.id, book.qty, book.title,
                           book.authorID, name, country FROM author
                           INNER JOIN book on book.authorID = author.id
                           WHERE book.id = ?''', (id,))
                found_book = cursor.fetchone()
                if found_book:
                    break
                else:
                    print("Unable to find book")
            except (TypeError, ValueError):
                print("That is not an integer. Try again.")

        display_bookID(id)
        '''Search book and display book info to update'''
        
        while True:
            update = int(input('''
        Select a category to update:
        1. Quantity
        2. Title
        3. Author Id
        4. Author Name
        5. Author Country
        0. Exit
                : '''))

            if update == 1:
                '''Quantity'''
                up_qty = int(input("Enter updated quantity for the book: "))
                cursor.execute('''UPDATE book SET qty = ?
                               WHERE id = ?''', (up_qty, id))
                db.commit()
                '''update quantity'''

                display_bookID(id)
                '''display updated book info'''

            elif update == 2:
                '''Title'''
                up_title = input("Enter updated title: ")
                cursor.execute('''UPDATE book SET title = ?
                               WHERE id = ?''', (up_title, id))
                db.commit()
                '''update book title'''

                display_bookID(id)
                '''display updated book info'''

            elif update == 3:
                '''Author ID'''
                up_authorID = int(input("Enter updated Author ID #: "))
                cursor.execute('''UPDATE book SET authorID = ? WHERE id = ?''',
                               (up_authorID, id))
                cursor.execute('''UPDATE author SET id = ? WHERE id = ?''',
                               (up_authorID, id))
                db.commit()
                '''update author id number'''

                display_bookID(id)
                '''display updated book info'''

            elif update == 4:
                '''Author Name'''
                up_auth_name = input("Enter updated Author name: ")
                cursor.execute('''UPDATE author SET name = ? FROM book
                               WHERE book.authorID = author.id
                               AND book.id = ?''', (up_auth_name, id))
                db.commit()
                '''update author name '''

                display_bookID(id)
                '''display updated book info'''

            elif update == 5:
                '''Author Country'''
                up_country = input("Enter updated Author ID #: ")
                cursor.execute('''UPDATE author SET country = ?
                               WHERE id = ?''', (up_country, id))
                db.commit()
                '''update author country'''

                display_bookID(id)
                '''display updated book info'''

            elif update == 0:
                print("Returning to main menu")
                break

            else:
                print("Invalid option. Please try again.\n")

    elif option == 3:  # Delete book
        delete_id = int(input("Please enter book ID # to delete: "))

        cursor.execute('''SELECT * FROM book WHERE id = ?''', (delete_id,))
        book = cursor.fetchone()
        '''search for book to confirm deletion'''

        if book:
            try:
                cursor.execute('''DELETE FROM book WHERE id IN
                               (SELECT book.id FROM book
                               INNER JOIN author ON book.authorID = author.id
                               WHERE book.id = ?)''', (delete_id,))
                db.commit()
                '''delete book'''
            except SyntaxError:
                print("Unable to delete")

            print(f"Book with id {delete_id} was deleted")
        else:
            print(f"Book with id {delete_id} was not found")

        print("\nAvailable books:")
        display_all()

    elif option == 4:  # Search book
        search_id = input("Please enter book ID #:")
        try:
            display_bookID(search_id)
        except None:
            print("Unable to find book")
        '''display book info'''

    elif option == 5:  # View all books
        print("\nAvailable books:")
        display_all()

    elif option == 0:  # End session
        cursor.execute('''DROP TABLE book''')
        print('\nBook table deleted!')
        db.commit()
        db.close()
        print('Connection to database closed.')
        print("Goodbye!")
        '''drop table and close connection'''
        break
        '''end loop'''

    else:
        print("That is not valid option. Please try again.")
