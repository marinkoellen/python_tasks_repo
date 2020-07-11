class Book:
    # Method inside a class - not a function
    def __init__(self,title,author, num_pages,current_page):
        self.title = title #for the class - book, each have a title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1
    
    def move_bookmark(self):
        self.bookmarked_page = self.current_page
    
    def turn_page(self,foward):
        if foward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.num_pages



book_1 = Book("Food book","Ellen",8888,1)
print(book_1)
print(len(book_1))
book_2 = Book("Dogs","Samara",8888,1)
print(book_2)

book_2.turn_page(True)
book_2.turn_page(True)
book_2.turn_page(True)
book_2.turn_page(True)
book_2.move_bookmark()
book_2.turn_page(True)
print(book_2.current_page,book_2.bookmarked_page)
