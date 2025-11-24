import random

movies = ["Inception", "Shrek", "Harry Potter", "Avengers", "Spirited Away"]

print("Total movies found:", len(movies))
print(movies)

while True:
    print('Random movie suggestion:', random.choice(movies))
    user_input = input('Want another suggestion? (y/n): ')
    if user_input.lower() != 'y':
        break
