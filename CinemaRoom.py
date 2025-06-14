from utils import hasFile

def hasCinemaRoom(cinema_rooms, room_id):
    return room_id in cinema_rooms

def insertCinemaRoom(cinema_rooms):
    room_id = int(input("Digite o código da Sala:"))
    if hasCinemaRoom(cinema_rooms, room_id):
        print("Sala de cinema já cadastrada!")
    else:
        name = input("Digite o nome da sala de cinema:")
        capacity = int(input("Digite a capacidade da sala:"))
        display_type = input("Qual o tipo de exibição:")
        is_acessible = int(input("1 - Acessivel, 0 - Sem Suporte:"))
        cinema_rooms[room_id] = (name, capacity, display_type, bool(is_acessible))


def showCinemaRoom(cinema_rooms, room_id):
    if not hasCinemaRoom(cinema_rooms, room_id):
        print("Sala de cinema não cadastrada!")
    else:
        name, capacity, display_type, is_acessible = cinema_rooms[room_id]

        print('-------------------------------')
        print("Informações da Sala de Cinema:")
        print(f"Código da Sala: {room_id}")
        print(f"Nome da Sala: {name}")
        print(f"Capacidade da Sala: {capacity}")
        print(f"Tipo de exibição: {display_type}")
        if is_acessible:
            print(f"É acessível: Sim")
        else:
            print(F"É acessível: Não")
        print('-------------------------------')

def showAllCinemaRoom(cinema_rooms):
    if len(cinema_rooms) == 0:
        print("Nenhuma Sala Cadastrada!")
    else:
        for val in cinema_rooms.keys():
            showCinemaRoom(cinema_rooms, val)
        
def updateSubMenu():
    print("1 - Nome da Sala:")
    print("2 - Capacidade da Sala:")
    print("3 - Tipo de Exibição: ")
    print("4 - Acessibilidade")
    print("5 - Sair")

def updateCinemaRoom(cinema_rooms, room_id):
    if hasCinemaRoom(cinema_rooms, room_id):
        showCinemaRoom(cinema_rooms, room_id)
        name, capacity, display_type, is_acessible = cinema_rooms[room_id]
        option = "0"
        while option != '5':
            updateSubMenu()
            option = input("Digite a escolha:")
            if option == "1":
                name = input("Digite o novo nome da sala:")
            if option == "2":
                capacity = int(input("Digite a nova capacidade da sala:"))
            if option == "3":
                display_type = input("Digite o novo tipo de exibição:")
            if option == "4":
                is_acessible = int(input("1 - Acessivel, 0 - Sem Suporte:"))
            if option == "5":
                cinema_roomsCopy = (name, capacity, display_type, bool(is_acessible))
                showCinemaRoom({ room_id: cinema_roomsCopy }, room_id)
                confirm = input("Tem certeza que deseja alterar:")
                if confirm.lower() == "sim" or confirm.lower() == "s":
                    cinema_rooms[room_id] = (name, capacity, display_type, bool(is_acessible))
                else:
                    print("Abortando...")
    else:
        print("Sala de cinema não cadastrado!")
   

def deleteCinemaRoom(cinema_rooms, room_id):
    if not hasCinemaRoom(cinema_rooms, room_id):
        print("Sala de cinema não cadastrada!")
    else:
        confirm = input("Tem certeza que deseja excluir:")
        if confirm.lower() == "sim" or confirm.lower() == "s":
            del cinema_rooms[room_id]
            print("Sala de Cinema Deletada!")
        else:
            print("Abortando...")
        

def saveCinemaRoomInFile(file, cinema_rooms):
    if len(cinema_rooms):
        ref_file = open(file, 'w')
        for room in cinema_rooms.keys():
            room_id = room
            name, capacity, display_type, is_acessible = cinema_rooms[room_id]
            line = str(room_id) + '\t' + name + '\t' + str(capacity) + '\t' + display_type + '\t' + str(is_acessible) + '\n'
            ref_file.write(line)
        ref_file.close()
    print("CinemaRoom.txt gerado com sucesso!")



def loadCinemaRoomFile(file, cinema_rooms):
    if hasFile(file):
        ref_file = open(file, 'r')
        for line in ref_file:
            line = line[:len(line)-1]
            room = line.split("\t")
            room_id = int(room[0])
            name = room[1]
            capacity = int(room[2])
            display_type = room[3]
            is_acessible = True if room[4] == "True" else False
            cinema_rooms[room_id] = (name, capacity, display_type, is_acessible)
        ref_file.close()
    print("CinemaRoom.txt carregado com sucesso!")









    
