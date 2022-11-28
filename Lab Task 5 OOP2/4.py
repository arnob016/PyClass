book_info = (("Best Mystery & Thriller","The Silent Patient",68821), ("Best Horror","The Institute",75717),("Best History & Biography","The five",31783 ), ("Best Fiction","The Testaments",98291))

for i in book_info:
    print(*i[1:3], "won the", i[0], "category with", i[2], "votes")