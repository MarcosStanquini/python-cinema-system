from CinemaRoom import insertCinemaRoom, updateCinemaRoom, deleteCinemaRoom, showAllCinemaRoom, showCinemaRoom, loadCinemaRoomFile, saveCinemaRoomInFile
from Movie import insertMovie, showAllMovie, showMovie, deleteMovie, updateMovie, saveMovieInFile, loadMovieFile
from Session import insertSession, deleteSession, showSession, showAllSession, updateSession, saveSessionInFile, loadSessionFile
from Query import queryExibitionCapacity, queryActorReleaseYear, queryendDateEnd
from utils import hasFile

CINEMA_ROOM_FILE_PATH = 'files/CinemaRoom.txt'
MOVIE_FILE_PATH = 'files/Movies.txt'
SESSION_FILE_PATH = 'files/Sessions.txt'


def mainMenu():
    print()
    print("1. Submenu de Salas")
    print("2. Submenu de Filmes")
    print("3. Submenu de Sessões")
    print("4. Submenu Consultas")
    print("5. Sair")


def movieMenu():
    print()
    print("1 - Inserir Filme:")
    print("2 - Atualizar Filme:")
    print("3 - Excluir Filme:")
    print("4 - Mostrar todas os Filmes:")
    print("5 - Mostrar um Filme:")
    print("6 - Voltar")

def queryMenu():
    print("\n===== CONSULTAS =====")
    print("1 - Salas: tipo X e capacidade > Y")
    print("2 - Filmes: ano ≥ X e ator Y")
    print("3 - Sessões: entre datas X e Y")
    print("4 - Voltar")



def cinemaRoomMenu():
    print()
    print("1 - Inserir Sala de Cinema:")
    print("2 - Atualizar Sala de Cinema:")
    print("3 - Excluir Sala de cinema:")
    print("4 - Mostrar todas as Salas de Cinema:")
    print("5 - Mostrar uma sala de cinema:")
    print("6 - Voltar")


def SessionMenu():
    print()
    print("1 - Inserir Sessão:")
    print("2 - Atualizar Sessão:")
    print("3 - Excluir Sessão:")
    print("4 - Mostrar todas as Sessões:")
    print("5 - Mostrar uma Sessão:")
    print("6 - Voltar")


cinema_rooms = {}
if hasFile(CINEMA_ROOM_FILE_PATH):
    loadCinemaRoomFile(CINEMA_ROOM_FILE_PATH, cinema_rooms)

movies = {}
if hasFile(MOVIE_FILE_PATH):
    loadMovieFile(MOVIE_FILE_PATH, movies)


sessions = []
if hasFile(SESSION_FILE_PATH):
    loadSessionFile(SESSION_FILE_PATH, sessions)

option = "0"
while option != "5":
    mainMenu()
    option = input("Digite a opção do menu:")
    if option == "1":
        subOption = "0"
        while subOption != "6":
            cinemaRoomMenu()
            subOption = input("Digite a opção:")
            if subOption == "1":
                insertCinemaRoom(cinema_rooms)
            if subOption == "2":
                cinemaRoomID = int(input("Digite o ID da sala de cinema:"))
                updateCinemaRoom(cinema_rooms, cinemaRoomID)
                print(cinema_rooms)
            if subOption == "3":
                cinemaRoomID = int(input("Digite o ID da sala de cinema:"))
                deleteCinemaRoom(cinema_rooms, cinemaRoomID)
            if subOption == "4":
                showAllCinemaRoom(cinema_rooms)
            if subOption == "5":
                cinemaRoomID = int(input("Digite o ID da sala de cinema:"))
                showCinemaRoom(cinema_rooms, cinemaRoomID)

    if option == "2":
        subOption = "0"
        while subOption != "6":
            movieMenu()
            subOption = input("Digite a opção:")
            if subOption == "1":
                insertMovie(movies)
            if subOption == "2":
                name = input("Digite o nome do filme:")
                release_year = int(input("Digite o Ano de Lançamento:"))
                updateMovie(movies, (name, release_year))
            if subOption == "3":
                name = input("Digite o nome do filme:")
                release_year = int(input("Digite o Ano de Lançamento:"))
                deleteMovie(movies, (name, release_year))
            if subOption == "4":
                showAllMovie(movies)
            if subOption == "5":
                name = input("Digite o nome do filme:")
                release_year = int(input("Digite o Ano de Lançamento:"))
                showMovie(movies, (name, release_year))
    
    if option == "3":
        subOption = "0"
        while subOption != "6":
            SessionMenu()
            subOption = input("Digite a opção:")
            if subOption == "1":
                insertSession(sessions, movies, cinema_rooms)
                print(sessions)
        
            if subOption == "2":
                movie_name = input("Digite o nome do filme:")
                movie_release_year = int(input("Digite o ano de lançamento:"))
                room_id = int(input("Digite o código da sala:"))
                date = input("Digite a data:")
                time = input("Digite o horário:")
                updateSession(sessions, [movie_name, movie_release_year, room_id, date, time])


            if subOption == "3":
                movie_name = input("Digite o nome do filme:")
                movie_release_year = int(input("Digite o ano de lançamento:"))
                room_id = int(input("Digite o código da sala:"))
                date = input("Digite a data:")
                time = input("Digite o horário:")
                deleteSession(sessions, [movie_name, movie_release_year, room_id, date, time])

            if subOption == "4":
                showAllSession(sessions)
            
            if subOption == "5":
                movie_name = input("Digite o nome do filme:")
                movie_release_year = int(input("Digite o ano de lançamento:"))
                room_id = int(input("Digite o código da sala:"))
                date = input("Digite a data:")
                time = input("Digite o horário:")
                showSession(sessions, [movie_name, movie_release_year, room_id, date, time])
    
    if option == "4":
        subOption = "0"
        while subOption != "4":
            queryMenu()
            subOption = input("Digite a opção:")
            if subOption == "1":
                display_type = input("Digite o tipo de exibição:")
                capacity = int(input("Digite a capacidade para mais que X pessoas:"))
                queryExibitionCapacity(cinema_rooms, display_type, capacity)

            if subOption == "2":
                release_year = int(input("Digite o ano de lançamento:"))
                actor = input("Digite o nome do ator que participou:")
                queryActorReleaseYear(movies, release_year, actor)

            if subOption == "3":
                start_date = input("Data Inicial (DD/MM/YYYY): ")
                end_date = input("Data Final (DD/MM/YYYY): ")
                queryendDateEnd(sessions, start_date, end_date)
            
    if option == "5":
        print("Saindo....")

            

        

            
            

saveCinemaRoomInFile(CINEMA_ROOM_FILE_PATH, cinema_rooms)
saveMovieInFile(MOVIE_FILE_PATH, movies)
saveSessionInFile(SESSION_FILE_PATH, sessions)