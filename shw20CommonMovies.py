'''
Test this scenario:
The first three friends did not have any common movie and the fourth friend have common movies. Debug and check the value of every variable
'''
firstFriendMovies=input('Enter the movies that you like (Friend 1): ').upper().split(' ')
print(f'First Friend Movies {firstFriendMovies}')
secondFriendMovies=input('Enter the movies that you like (Friend 2): ').upper().split(' ')
print(f'First Friend Movies {secondFriendMovies}')
thirdFriendMovies=input('Enter the movies that you like (Friend 3): ').upper().split(' ')
print(f'First Friend Movies {thirdFriendMovies}')
fourthFriendMovies=[]
commonMovies=0
while True:
    fourthFriendMovie=input('Enter the movie that you like (Friend 4): ').upper().strip()
    fourthFriendMovies.append(fourthFriendMovie)
    if fourthFriendMovie in firstFriendMovies:
        print(f'You and your first friend like {fourthFriendMovie}')
        commonMovies+=1
    elif fourthFriendMovie in secondFriendMovies:
        print(f'You and your second friend like {fourthFriendMovie}')
        commonMovies += 1
    elif fourthFriendMovie in thirdFriendMovies:
        print(f'You and your third friend like {fourthFriendMovie}')
        commonMovies += 1
    if commonMovies>=3:
        break
print(f'Another Friend Movies {fourthFriendMovies}')