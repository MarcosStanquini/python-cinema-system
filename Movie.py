from utils import hasFile


def hasMovie(movies, movie_id):
    return movie_id in movies 

def hasActor(actors, actor):
    for i, a in enumerate(actors):
        if a == actor:
            return i
    return -1

def insertMovie(movies):
    name = input("Digite o nome do filme:")
    release_year = int(input("Digite o Ano de Lançamento:"))
    movie_id = (name, release_year)

    if not hasMovie(movies, movie_id):
        production_cost = float(input("Digite o custo de produção:"))
        director = input("Digite o nome do diretor:")
        actors = []
        end = "0"
        while end != "":
            actor = input("Digite o nome do ator:")
            actors.append(actor)
            end = input("Deseja adicionar mais um ator? <Enter> para parar!")

        movies[movie_id] = [production_cost, director, actors]
    else:
        print("Filme ja cadastrado!")


def showMovie(movies, movie_id):
    if hasMovie(movies, movie_id):
        name = movie_id[0]
        release_year = movie_id[1]
        production_cost = movies[movie_id][0]
        director = movies[movie_id][1]
        actors = movies[movie_id][2]
        
        print("----------------------------------")
        print(f"Nome do filme: {name}")
        print(f"Ano de Lançamento {release_year}")
        print(f"Custo de Produção: {production_cost}")
        print(f"Diretor do Filme: {director}")
        for actor in actors:
            print(f"Nome do Ator: {actor} ")
        print("----------------------------------")
    else:
        print("Filme não cadastrado!")


def showAllMovie(movies):
    if len(movies) == 0:
        print("Nenhum filme cadastrado!")
    else:
        for key in movies.keys():
            showMovie(movies, key)


def deleteMovie(movies, movie_id):
    if hasMovie(movies, movie_id):
        confirm = input("Tem certeza que deseja excluir:")
        if confirm.lower() == "sim" or confirm.lower() == "s":
            del movies[movie_id]
            print("Filme deletado!")
        else:
            print("Abortando...")
    else:
        print("Filme não cadastrado!")


def updateSubMenu():
    print("1 - Custo de produção:")
    print("2 - Diretor")
    print("3 - Atores")
    print("4 - Sair")


def updateMovie(movies, movie_id):
    if hasMovie(movies, movie_id):

        production_cost, director, actors = movies[movie_id]

        print("Informações do Filme:")
        showMovie(movies, movie_id)
        option = "0"
        print()
        while option != "4":
            updateSubMenu()
            option = input("Digite a opção para alterar:")
            if option == "1":
                production_cost = float(input("Digite o novo custo de produção:"))
            if option == "2":
                director = input("Digite o novo diretor:")
            if option == "3":
                actor_to_update = input("Digite o nome do ator que deseja alterar:")
                index = hasActor(actors, actor_to_update)
                if index != -1:
                    new_actor = input("Digite o novo ator:")
                    actors[index] = new_actor
                else:
                    print("Ator não cadastrado!")
            if option == "4":
                moviesCopy = [production_cost, director, actors]
                showMovie({movie_id: moviesCopy}, movie_id)
                confirm = input("Tem certeza que deseja alterar:")
                if confirm.lower() == "sim" or confirm.lower() == "s":
                    movies[movie_id] = [production_cost, director, actors]
                else:
                    print("Abortando...")
    else:
        print("Filme não cadastrado!")



def saveMovieInFile(file, movies):
    if len(movies):
        ref_arq = open(file, 'w')
        for key in movies.keys():
            name, release_year = key
            production_cost, director, actors = movies[(name, release_year)]
            line = name + '\t' + str(release_year) + '\t' + str(production_cost) + '\t' + director + '\t'
            for actor in actors:
                line+= actor + "\t"
            line += "\n"
            ref_arq.write(line)
        ref_arq.close()
    print("Movie.txt gerado com sucesso!")



def loadMovieFile(file, movies):
    if hasFile(file):
        ref_arq = open(file, 'r')
        for line in ref_arq:
            line = line[:len(line)-1]
            movie = line.split("\t")
            name = movie[0]
            release_year = int(movie[1])
            production_cost = float(movie[2])
            director = movie[3]
            actors = movie[4:len(movie)-1]
            movies[(name, release_year)] = [production_cost, director, actors]
        ref_arq.close()
        print("Movie.txt carregado com sucesso!")




