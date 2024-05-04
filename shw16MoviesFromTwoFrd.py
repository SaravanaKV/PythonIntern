############## Problem  1 ####################
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list,
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like


firstFriendMovies=input('Enter the movies that you like: ').upper().split(' ')
print(f'First Friend Movies {firstFriendMovies}')
anotherFriendMovies=[]
commonMovies=0
while True:
    anotherFriendMovie=input('Enter the movie that you like: ').upper().strip()
    anotherFriendMovies.append(anotherFriendMovie)
    if anotherFriendMovie in firstFriendMovies:
        print(f'You both like {anotherFriendMovie}')
        commonMovies+=1
    if commonMovies>=3:
        break
print(f'Another Friend Movies {anotherFriendMovies}')


