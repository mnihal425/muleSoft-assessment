import sqlite3

conn = sqlite3.connect('Movies.db')

c = conn.cursor()
#CREATION OF MOVIES TABLE
# c.execute("""
#     CREATE TABLE MOVIES(
#         MOVIE_NAME TEXT PRIMARY KEY,
#         ACTOR_NAME TEXT,
#         ACTRESS_NAME,
#         DIRECTOR_NAME,
#         YEAR_OF_RELEASE INTEGER)""")

def insertData():
    movieName = input('Enter the name of the movie: ')
    actorName = input('Enter the name of the lead actor: ')
    actressName = input('Enter the name of the lead actress: ')
    directorName = input('Enter the name of the director: ')
    movieYear = int(input('Enter the year the movie was released: '))
    with conn:
        c.execute("""INSERT INTO MOVIES VALUES 
        (:movieName, :actorName, :actressName, :directorName, :movieName)
        """,{'movieName': movieName, 'actorName': actorName, 'actressName': actressName, 'directorName': directorName, 'movieYear': movieYear})

def displayData():
    with conn:
        c.execute('SELECT * FROM MOVIES')
        allMovies = c.fetchall()
        for movie in allMovies:
            print('Movie name: ',movie[0])
            print('Lead actor: '+str(movie[1]))
            print('Lead actress: '+str(movie[2]))
            print('Director: '+str(movie[3]))
            print('Year of release: '+str(movie[4]))

def displayActor(actorName):
    with conn:
        c.execute('SELECT * FROM MOVIES WHERE ACTOR_NAME = (:actorName)',{'actorName':actorName})
        allMovies = c.fetchall()
        if allMovies == []:
            print('No entry of such actor found in the database')
        else:
            print('Movies the actor has acted in: ')
            for movie in allMovies:
                print('Movie name: ',movie[0])

def displayActress(actressName):
    with conn:
        c.execute('SELECT * FROM MOVIES WHERE ACTRESS_NAME = (:actressName)',{'actressName':actressName})
        allMovies = c.fetchall()
        if allMovies == []:
            print("No entry of such actress found in the database")
        else: 
            print('Movies the actress has acted in: ')
            for movie in allMovies:
                print('Movie name: ',movie[0])

def displayDirector(directorName):
    with conn:
        c.execute('SELECT * FROM MOVIES WHERE DIRECTOR_NAME = (:directorName)',{'directorName':directorName})
        allMovies = c.fetchall()
        if allMovies == []:
            print('No entry of such director found in the database')
        else:
            print('Movies the director has directed: ')
            for movie in allMovies:
                print('Movie name: ',movie[0])

conn.commit()
conn.close()

while True:
    print('\n-------Movie Database-------')
    print('1. Insert a new movie')
    print('2. Display details of all the movies')
    print('3. Show all the movies a particular actor has acted in')
    print('4. Show all the movies a particular actress has acted in')
    print('5. Show all the movies a particular director has directed')
    print('6. Exit \n')

    op = int(input('Enter the option: '))

    if op == 1:
        insertData()
    elif op == 2:
        displayData()
    elif op == 3:
        actorName = input('Enter the name of the actor: ')
        displayActor(actorName)
    elif op == 4:
        actressName = input('Enter the name of the actress: ')
        displayActress(actressName)
    elif op == 5:
        directorName = input('Enter the name of the director: ')
        displayDirector(directorName)
    elif op == 6:
        break
        

