class Books:
    def __init__(self, title, author, publish_year, pages, language, price):

        """
        :param title: the title of book
        :param author: the name of author(s)
        :param publish_year: the year of book publication
        :param pages: the numbers of book pages
        :param language: the language of book
        :param price:the price of book
        """

        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.residue_pages = pages
        self.language = language
        self.price = price

    def read(self, page_number):

        """
        :param page_number: last page number read
        """
        if page_number > self.pages:
            print(f'you completed this book!!!')
        else:
            self.residue_pages = self.pages - page_number
            print(f'you have read {page_number} more pages from {self.title}. '
                  f'There are {self.residue_pages} pages left')

    def get_status(self):

        """
        :return: based on number of read pages, return 3 statues:
                 1- "unread" ( no pages has been read yet)
                 2- "reading" ( reading the book)
                 3- "finished" ( all pages has been read)
        """

        if self.residue_pages == self.pages:
            return 'unread'
        if (self.residue_pages > 0) and (self.residue_pages < self.pages):
            return 'reading'
        if self.residue_pages == 0:
            return 'finished'

    def __str__(self):
        print(f'title:{self.title}, author(s):{self.author}, '
              f'year of publish:{self.publish_year}, number of pages:{self.pages},'
              f' language of book:{self.language} and its price:{self.price}')


def get_data():
    """

    :return: receives book information, makes an instance of book class and returns it
    """
    print('enter these information:')
    title = input('title of book:')
    author = input('author(s) of book (split names with ,):')
    publish_year = int(input('the year of publication:'))
    pages = int(input('the numbers of pages:'))
    language = input('its language:')
    price = input('its price:')
    book = Books(title, author, publish_year, pages, language, price)

    return book


print('test pulling Git")
comment = ''
book_shelf = []
while comment != 'Quit':
    comment = input('if you have any data press enter - else enter Quit:')
    if comment == 'Quit':
        break
    else:
        book_shelf.append(get_data())

for item in book_shelf:
    item.__str__()

book_shelf[2].read(150)
book_shelf[0].read(15)
book_shelf[2].read(260)

print(book_shelf[0].get_status())
print(book_shelf[1].get_status())
