'''
Menucard{
    Breakfast{
        Hot idly:45,
        Pongal:45,
        Appam:85,
        Sambar vadai:45
        poori:60,
        paratta:60,
        chappathi:60,
    Dosai{
        pecial dosai:75,
        Masala dosai:90,
        Onion dosai:105,
        Ghee dosai:160
        }
    Sweets{
        Rava kesari:70,
        Sweet ponkal:70,
        Gulab jamun:40
        }
    Lunch{
        Special limited meals:130,
        Tamilnadu meals:195,
    Rich{
        Curd rice:75,
        Sambar rice:75,
        Leman rice:75
        }
    Evening snacks{
        Veg cutlet:45,
        Bonda:60,
        Samosa:35,
        Sweet kozhukattai:45
        }
    Special{
            Chola poori:90,
            Ghee idly:95,
            Mini tiffin:140
            Quick lunch:140,
            Quick dinner:140
            }
    Hot beverages{
        Special filter coffe:35,
        Special tea:40,
        Special milk:35,
    }
'''
numOfCategories = int(input('Enter the total number of categories : '))
menuCategories=[]        #['Breakfast','Dosai','Sweet','Lunch','Rich','Eveningsnacks','Special','Hotbeverages']
for i in range(1,numOfCategories+1):
    Categories=input(f'\tEnter the category {i} : ')
    menuCategories.append(Categories)
menu={}
for category in menuCategories:
    numOfFood=int(input(f'Enter the total number of food in the category of {category} : '))
    n=menu[category]={}
    for food in range(1, numOfFood + 1):
        foodName = input(f'\tEnter the name of food {food} : ')
        foodCost = int(input(f'\tEnter the cost of {foodName} : '))
        n[foodName]=foodCost
print('\t'*6,'HSB MENU CARD' )
for categoryy,foodd in menu.items():
    print(categoryy)
    for foodN,cost in foodd.items():
        m=(13-((len(foodN)+1)//4))
        print(f'\t{foodN}','\t'*m,f'$.{cost}')
'''
                        HSB MENU CARD                    
Breakfast
    Hot idly                                            $.45
    Pongal                                              $.45

    Appam                                               $.85
    Sambar vadai                                        $.45
    poori                                               $.60
Lunch
    Special limited meals                               $.130
    Tamilnadu meals                                     $.195
Evening snacks
    Veg cutlet                                          $.45
    Bonda                                               $.60
    Samosa                                              $.35
    Sweet kozhukattai                                   $.45
'''