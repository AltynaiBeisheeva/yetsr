import psycopg2

conn = psycopg2.connect("dbname = films user = 'altynai' password = '1'")
cur = conn.cursor()
while True:
    print('1 - Посмотреть фильмы')
    print('2 - Добавить фильм')
    vybor = input()
    if vybor == '1':
        cur.execute('select * from films;')
        for i in cur.fetchall():
            print(f'Жанр - {i[4]}\nНазвание - {i[1]}\nВозрастное ограничение - {i[2]}\nГод выпуска - {i[3]}')
    if vybor == '2':
        cur.execute(f"insert into films(title, age, year, janr) values('{input()}', {int(input())}, {int(input())}, '{input()}')")
        conn.commit()
        print('Фильм добавился')