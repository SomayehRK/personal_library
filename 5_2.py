from tabulate import tabulate


class Books:
    def __init__(self, title=None, author=None, publish_year=None, pages=None, book_language=None, price=None):
        
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.residue_pages = self.pages
        self.book_language = book_language
        self.price = price
        self.progress = 0

    def get_data(self):
        """
        :return: by this method we receive the object attributes, make a class object and return it
        """
        title = input('enter these information:\ntitle of book:')
        author = input('author(s) of book (split names with ,):')
        publish_year = int(input('the year of publication:'))
        pages = int(input('the numbers of pages:'))
        book_language = input('its language:')
        price = input('its price:')

        return Books(title, author, publish_year, pages, book_language, price)

    def read(self, page_number):
        """

        :param page_number: Last page number read
        :return: in this method, the number of remaining pages and media progress attribute are determined
        """
        if page_number > self.pages:
            print(f'you completed this book!!!')
        else:
            self.residue_pages = self.pages - page_number
            self.progress = ((self.pages - self.residue_pages)/self.pages)*100
            print(f'you have read {page_number} more pages from {self.title}. '
                  f'There are {self.residue_pages} pages left')

    def get_reading_status(self):
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
              f' language of book:{self.book_language} and its price:{self.price}')


class Magazine(Books):
    def __init__(self, title=None, author=None, publish_year=None, pages=None, magazine_language=None, price=None,
                 issue=None):
        self.issue = issue
        Books.__init__(self, title, author, publish_year, pages, magazine_language, price)

    def get_data(self):
        title = input('enter these information:\ntitle of magazine:')
        author = input('author(s) of magazine (split names with ,):')
        publish_year = int(input('the year of publication:'))
        pages = int(input('the numbers of pages:'))
        magazine_language = input('its language:')
        issue = input('its issue:')
        price = input('its price:')

        return Magazine(title, author, publish_year, pages, magazine_language, price, issue)

    def __str__(self):
        print(f'title:{self.title}, author(s):{self.author}, '
              f'year of publish:{self.publish_year}, number of pages:{self.pages},'
              f' language of book:{self.book_language}, its issue:{self.issue} and its price:{self.price}')


class PodcastEpisode:
    def __init__(self, title=None, speaker=None, publish_year=None, time=None, audio_language=None, price=None):
        self.title = title
        self.speaker = speaker
        self.publish_year = publish_year
        self.time = time
        self.residue_time = self.time
        self.audio_language = audio_language
        self.price = price
        self.progress = 0

    def get_data(self):
        title = input('enter these information:\ntitle of podcast episode:')
        speaker = input('speaker(s) of podcast (split names with ,):')
        publish_year = int(input('the year of publication:'))
        time = int(input('its time:'))
        audio_language = input('its language:')
        price = input('its price:')

        return PodcastEpisode(title, speaker, publish_year, time, audio_language, price)

    def listen(self, elapsed_time):
        """

        :param elapsed_time: minutes of the audio file is listened to.
        :return: in this method, the number of remaining minutes of audio and media progress attribute are determined
        """
        if elapsed_time > self.time:
            print(f'this episode is finished!!!')
        else:
            self.residue_time = self.time - elapsed_time
            self.progress = ((self.time - self.residue_time) / self.time) * 100
            print(f'you have listened {elapsed_time} more minutes from {self.title}. '
                  f'There are {self.residue_time} minutes left')    

    def get_listening_status(self):
        """

        :return: based on number of listened minutes, return 3 statues:
                    1- "Not heard" ( no minute has been listened yet)
                    2- "listening" ( listening the audio)
                    3- "finished" ( whole audio file has been listened )
        """
        if self.residue_time == self.time:
            return 'Not heard'
        if (self.residue_time > 0) and (self.residue_time < self.time):
            return 'listening'
        if self.residue_time == 0:
            return 'finished'

    def __str__(self):
        print(f'title:{self.title}, speaker(s):{self.speaker}, '
              f'year of publish:{self.publish_year}, its time:{self.time},'
              f' language of audio:{self.audio_language} and its price:{self.price}')


class AudioBook(Books, PodcastEpisode):
    def __init__(self, title=None, speaker=None, author=None, publish_year=None, pages=None, book_language=None,
                 audio_language=None, time=None, price=None):
        Books.__init__(self, title, author, publish_year, pages, book_language, price)
        PodcastEpisode.__init__(self, title, speaker, publish_year, time, audio_language, price)

    def get_data(self):
        title = input('enter these information:\ntitle of book:')
        speaker = input('speaker(s) of audio (split names with ,):')
        author = input('author(s) of book (split names with ,):')
        publish_year = int(input('the year of publication:'))
        pages = int(input('number of pages:'))
        book_language = input('book language:')
        audio_language = input('audio language:')
        time = int(input('its time:'))
        price = input('its price:')

        return AudioBook(title, speaker, author, publish_year, pages, book_language, audio_language, time, price)

    def __str__(self):
        print(f'title:{self.title}, speaker(s):{self.speaker}, book author:{self.author} '
              f'year of publish:{self.publish_year}, its time:{self.time}, language of book:{self.book_language},'
              f' language of audio:{self.audio_language} and its price:{self.price}')    


def sort_func(lst, metric, reverse):
    """

    :param lst: a list of class object
    :param metric: the list will be sorted based on this metric
    :param reverse: determines whether the list is ascending or descending.
    :return: this function will sorts all shelf items(descending) based on progress and print
            items in this form: {media type,name,progress}
    """
    table = []
    lst = sorted(lst, key=lambda x: x.__getattribute__(metric), reverse=reverse)
    for i in range(len(lst)):
        table.append([i + 1, lst[i].__class__.__name__, lst[i].title, lst[i].progress])
    print(tabulate(table, headers=['id', 'media_type', 'title', 'progress(%)']))
    # for _ in lst:
    #     print({_.__class__.__name__, _.title, _.progress})


def print_all_shelf(lst):
    """

    :param lst: a list of class object
    :return: print all items in main shelf in form of table
    """
    print('all your medias are:\n')
    show_list = []
    for i in range(len(lst)):
        show_list.append([i + 1, lst[i].__class__.__name__, lst[i].title,
                          lst[i].get_reading_status()
                          if lst[i].__class__.__name__ == 'Books' or lst[i].__class__.__name__ == 'Magazine'
                          else lst[i].get_listening_status()])
    print(tabulate(show_list, headers=['id', 'media_type', 'title', 'status']))


print('test modifying')
main_shelf = []
book_shelf = []
magazine_shelf = []
podcast_shelf = []
audioBook_shelf = []


print('\n*********************************  <<< welcome to Meimanat media shelf >>>  *********************************')

while True:
    selection = int(input('\n------------------------------------------------------------------\n'
                          '1 - record a file\n2 - record reading or listening history\n'
                          '3 - see your sorted shelf based on media progress\n'
                          '4 - see your shelf base on media status\n5 - Quit\n'))
    if selection == 5:
        break
    elif selection == 1:
        while True:
            type_record = int(input('------------------------------------------------------------------\n'
                                    '1 - Book\n2 - Magazine\n3 - Podcast episode\n4 - Audio book\n5 - back\n'))
            if type_record == 5:
                break
            elif type_record == 1:
                book = Books().get_data()
                book_shelf.append(book)
                main_shelf.append(book)
            elif type_record == 2:
                mag = Magazine().get_data()
                magazine_shelf.append(mag)
                main_shelf.append(mag)
            elif type_record == 3:
                pod = PodcastEpisode().get_data()
                podcast_shelf.append(pod)
                main_shelf.append(pod)
            elif type_record == 4:
                aud = AudioBook().get_data()
                audioBook_shelf.append(aud)
                main_shelf.append(aud)
            else:
                print('please enter a correct choice:\n')
    elif selection == 2:
        while True:
            function = int(input('------------------------------------------------------------------\n'
                                 '1 - Record the last page read\n'
                                 '2 - record how long you have listened an audio media (in minute).\n3 - back\n'))
            if function == 3:
                break
            elif function == 1:
                while True:
                    type_record = int(input('------------------------------------------------------------------\n'
                                            '1 - book\n2 - Magazine\n3 - Audio book\n4 - back\n'))
                    if type_record == 4:
                        break
                    elif type_record == 1:
                        if len(book_shelf) == 0:
                            print('you do not have any book in your shelf!!!')
                        else:
                            print('------------------------------------------------------------------\n'
                                  'books are:\n')
                            for i in range(len(book_shelf)):
                                print(f'{i + 1} : {book_shelf[i].title}\n')
                            id = int(input('select the number of the book you want:'))
                            page = int(input('enter the number of last page you read:'))
                            book_shelf[id - 1].read(page)
                    elif type_record == 2:
                        if len(magazine_shelf) == 0:
                            print('you do not have any magazine in your shelf!!!')
                        else:
                            print('------------------------------------------------------------------\n'
                                  'magazines are:\n')
                            for i in range(len(magazine_shelf)):
                                print(f'{i + 1} : {magazine_shelf[i].title}\n')
                            id = int(input('select the number of the magazine you want:'))
                            page = int(input('enter the number of last page you read:'))
                            magazine_shelf[id - 1].read(page)
                    else:
                        if len(audioBook_shelf) == 0:
                            print('you do not have any audio book in your shelf!!!')
                        else:
                            print('------------------------------------------------------------------\n'
                                  'audio books are:\n')
                            for i in range(len(audioBook_shelf)):
                                print(f'{i + 1} : {audioBook_shelf[i].title}\n')
                            id = int(input('select the number of the audio book you want:'))
                            page = int(input('enter the number of last page you read:'))
                            audioBook_shelf[id - 1].read(page)
            elif function == 2:
                while True:
                    type_record = int(input('------------------------------------------------------------------\n'
                                            '1 - podcast\n2 - Audio book\n3 - back\n'))
                    if type_record == 3:
                        break
                    elif type_record == 1:
                        if len(podcast_shelf) == 0:
                            print('you do not have any podcast in your shelf!!!')
                        else:
                            print('------------------------------------------------------------------\n'
                                  'podcasts are:\n')
                            for i in range(len(podcast_shelf)):
                                print(f'{i + 1} : {podcast_shelf[i].title}\n')
                            id = int(input('select the number of the podcast you want:'))
                            time_audio = int(input('enter the number of minutes you listened:'))
                            podcast_shelf[id - 1].listen(time_audio)
                    else:
                        if len(audioBook_shelf) == 0:
                            print('you do not have any audio book in your shelf!!!')
                        else:
                            print('------------------------------------------------------------------\n'
                                  'audio books are:\n')
                            for i in range(len(audioBook_shelf)):
                                print(f'{i + 1} : {audioBook_shelf[i].title}\n')
                            id = int(input('select the number of the audio book you want:'))
                            time_audio = int(input('enter the number of minutes you listened:'))
                            audioBook_shelf[id - 1].listen(time_audio)
            else:
                print('please enter a correct choice:\n')
    elif selection == 3:
        if len(main_shelf) == 0:
            print('you do not have any media in your shelf!!!')
        else:
            sort_func(main_shelf, 'progress', True)
    elif selection == 4:
        if len(main_shelf) == 0:
            print('you do not have any media in your shelf!!!')
        else:
            print_all_shelf(main_shelf)
    else:
        print('please enter a correct choice:\n')