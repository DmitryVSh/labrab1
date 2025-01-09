# дискета
disk_size_mb = 1.44
disk_size_bytes = disk_size_mb * 1024 * 1024

# Параметры книги
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Объем одной книги в байтах
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

books = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books))
