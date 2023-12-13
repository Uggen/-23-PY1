# TODO Найдите количество книг, которое можно разместить на дискете
full_size = 1.44 #перевод в килобайты
book_size = 100
line_size = 50
simbol_size = 25
one_simbol_size = 4/(1024*1024)

one_book_size = book_size * line_size * simbol_size * one_simbol_size
numbers_of_books = int(full_size//one_book_size)

print("Количество книг, помещающихся на дискету:", numbers_of_books)
