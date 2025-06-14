from Movie import hasMovie
from CinemaRoom import hasCinemaRoom
from utils import hasFile

def hasSession(sessions, session):
    for i in range(len(sessions)):
        if (
            sessions[i][2] == session[2] and
            sessions[i][3] == session[3] and
            sessions[i][4] == session[4]):
            return True
    return False


def findSessionIndex(sessions, session):
    for i in range(len(sessions)):
        if (
            sessions[i][2] == session[2] and
            sessions[i][3] == session[3] and
            sessions[i][4] == session[4]):
            return i
    return -1
            


def insertSession(sessions, movies, cinema_rooms):
    movie_name = input("Digite o nome do filme:")
    movie_release_year = int(input("Digite o ano de lançamento:"))
    if hasMovie(movies, (movie_name, movie_release_year)):
        room_id = int(input("Digite o código da sala:"))
        if hasCinemaRoom(cinema_rooms, room_id):
            date = input("Digite a data:")
            time = input("Digite o horário:")
            ticket_price = float(input("Digite o value do ingresso:"))
            if not hasSession(sessions, [movie_name, movie_release_year, room_id, date, time, ticket_price]):
                sessions.append([movie_name, movie_release_year, room_id, date, time, ticket_price])
            else:
                print("Sessão ja existente nesses parametros!")
        else:
            print("Sala não cadastrada!")
    else:
        print("Filme não cadastrado!")


def deleteSession(sessions, session):
    if hasSession(sessions, session):
        del sessions[findSessionIndex(sessions, session)]
    else:
        print("Não existe sessão cadastrada")

def updateSession(sessions, session):
    if hasSession(sessions, session):
        index = findSessionIndex(sessions, session)
        sessionsList = sessions[index]
        new_ticket_price = float(input("Digite o novo value do ingresso:"))
        confirm = input("Tem certeza que deseja alterar:")
        if confirm.lower() == "sim" or confirm.lower() == "s":
            sessionsList[5] = new_ticket_price
        else:
            print("Abortando...")
    else:
        print("Sessão não cadastrada!")
    
        
def showSession(sessions, session):
    if hasSession(sessions, session):
        index = findSessionIndex(sessions, session)
        print("----------------------------------")
        print("Informações da sessão:")
        sessionList = sessions[index]
        print(f"Nome do Filme: {sessionList[0]}")
        print(f"Ano de Lançamento: {sessionList[1]}")
        print(f"Código da Sala: {sessionList[2]}")
        print(f"Data: {sessionList[3]}")
        print(f"Horário: {sessionList[4]}")
        print(f"Preço do Ingresso: {sessionList[5]}")
        print("----------------------------------")
    else:
        print("Sessão não cadastrada!")

    

def showAllSession(sessions):
    if len(sessions) > 0:
        for i in range(len(sessions)):
            showSession(sessions, sessions[i])
    else:
        print("Nenhuma sessão cadastrada!")



def saveSessionInFile(file, sessions):
    if len(sessions) > 0:
        ref_arq = open(file, 'w')
        for value in sessions:
                movie_name = value[0]
                release_year = value[1]
                room_id = value[2]
                date = value[3]
                time = value[4]
                ticket_price = value[5]
                line = movie_name + '\t' + str(release_year) + '\t' + str(room_id) + '\t' + date + '\t' + time + '\t' + str(ticket_price) + '\n'
                ref_arq.write(line)
        ref_arq.close()
                
def loadSessionFile(file, sessions):
    if hasFile(file):
        ref_arq = open(file, 'r')
        for line in ref_arq:
            line = line[:len(line)-1]
            session_values = line.split("\t")
            movie_name = session_values[0]
            movie_release_year = int(session_values[1])
            room_id = int(session_values[2])
            date = session_values[3]
            time = session_values[4]
            ticket_price = float(session_values[5])
            sessions.append([movie_name, movie_release_year, room_id, date, time, ticket_price])
        ref_arq.close()
    print("Session.txt carregado com sucesso!")



def is_date_between(xdate, start_date, end_date):
    day_x, month_x, year_x = int(xdate[0:2]), int(xdate[3:5]), int(xdate[6:])
    day_start, month_start, year_start = int(start_date[0:2]), int(start_date[3:5]), int(start_date[6:])
    day_end, month_end, year_end = int(end_date[0:2]), int(end_date[3:5]), int(end_date[6:])

    data_x = (year_x, month_x, day_x)
    data_start = (year_start, month_start, day_start)
    data_end = (year_end, month_end, day_end)

    return data_start < data_x < data_end





    

    







