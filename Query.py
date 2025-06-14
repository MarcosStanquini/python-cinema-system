from CinemaRoom import showCinemaRoom
from Movie import showMovie, hasActor
from Session import is_date_between, showSession

def queryExibitionCapacity(cinema_rooms, display_type, capacity):
    for keys in cinema_rooms.keys():
        if cinema_rooms[keys][2] == display_type:
            if cinema_rooms[keys][1] > capacity:
                showCinemaRoom(cinema_rooms, keys)

def queryActorReleaseYear(movies, release_year, actor):
    for key in movies.keys():
        dict_release_year = key[1]
        actors = movies[key][2]
        if dict_release_year >= release_year:
            if hasActor(actors, actor) != -1:
                showMovie(movies, key)


def queryendDateEnd(sessions, start_date, end_date):
    for session in sessions:
        if is_date_between(session[3], start_date, end_date):
            showSession(sessions, session)

            
        
    
   

