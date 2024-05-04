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
            Special dosai:75,
            Masala dosai:90,
            Onion dosai:105,
            Ghee dosai:160
            }
    Sweets{
        Raba kesari:70,
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

        spice

    }
'''
numOfCategories = int(input('Enter the total number of categories : '))
menuCategories=[]
for i in range(1,numOfCategories+1):
    Categories=input(f'Enter the category {i} : ')         #['Breakfast','Sweet','Lunch','Eveningsnacks','Special','Hotbeverages']
    menuCategories.append(Categories)
menuSubCategories=[input(f'Enter the subcategory {i} : ') for i in range(1,int(input('Enter the total number of subcategories : '))+1)]    #['Dosai','Rich']
menu={}
for category in menuCategories:
    numOfFood=int(input(f'Enter the total number of food in the category of {category} : '))
    n=menu[category]={}
    for food in range(1,numOfFood+1):
        foodName = input(f'Enter the food name {food} : ')
        if(foodName in menuSubCategories):
            numOffood=int(input(f'Enter the total number of food in the category of {foodName} :'))
            m=menu[category][foodName]={}
            for food in range(1, numOffood + 1):
                foodname = input(f'Enter the food name {food} : ')
                foodCost = input(f'Enter the cost name {foodname} : ')
                m[foodname]=foodCost
        else:
            foodCost = input(f'Enter the food cost {foodName} : ')
            n[foodName]=foodCost
print(menu)