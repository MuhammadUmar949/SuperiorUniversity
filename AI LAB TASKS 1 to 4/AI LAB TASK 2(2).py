
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

addMovies=int(input("How many Movies you want to Enter: "))
for i in range(0,addMovies):
    nameOfMovie=input("Enter Name Of movie: ")
    budgetofMovei=int(input("Enter budget Of movie: "))
    movies.append((nameOfMovie,budgetofMovei))


sumofBudgets=0
highBudgetMovieCount=0
excededValue=0
for movie in movies:
    sumofBudgets=sumofBudgets+movie[1]

averageBudget=sumofBudgets/len(movies)
print(int(averageBudget))

for movie in movies:
    if movie[1]>averageBudget:
        excededValue=movie[1]-averageBudget
        highBudgetMovieCount+=1
        print(f"This movie {movie} is spent {int(excededValue)} more than average budget")


print(f"Total {highBudgetMovieCount} spent more than average")