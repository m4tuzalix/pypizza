from collections import UserDict
from enum import Enum, auto
from dataclasses import dataclass

class MovieType(Enum):
    HORROR = auto()
    COMEDY = auto()
    DRAMA = auto()

@dataclass
class MovieDetails:
    type: MovieType
    year: int

@dataclass
class Movie:
    title: str
    details: MovieDetails

class Library(UserDict):
    def __init__(self):
        super().__init__()
    
    def __setitem__(self, key: str, item: MovieDetails):
        if self.get(key):
            raise ValueError("This movie already exist in db")
        if type(item) != MovieDetails: raise ValueError("Wrong movie details provided")

        super(Library, self).__setitem__(key, item)
    def add(self, movie: Movie):
        self.__setitem__(movie.title, movie.details)

    def search(self, title: str) -> MovieDetails | None:
        return self.get(title)

def main():
    library = Library()
    titanic = Movie("titanic", MovieDetails(type=MovieType.DRAMA, year=1999))

    library.add(titanic)
    print(library.search("titanic"))

if __name__ == "__main__":
    main()