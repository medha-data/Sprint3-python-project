sales_by_genre={}

for game in video_game_sales:
    genre=game[GENRE]
    sales=game[GLOBAL_SALES]

    if genre in sales_by_genre:
          sales_by_genre[genre]+= sales
    else:
        sales_by_genre[genre]= sales

print(sales_by_genre)

games_per_publisher={}

for game in video_game_sales:
    publisher=game[PUBLISHER]

    if publisher in games_per_publisher:
        games_per_publisher[publisher]+=1
    else :
        games_per_publisher[publisher]=1

print(games_per_publisher)

for game in video_game_sales:
    if game[RANK]==1:
        top_game={
            'name':game[NAME],
            'year':game[YEAR],
            'genre':game[GENRE],
            'publisher':game[PUBLISHER],
            'global_sales':game[GLOBAL_SALES]
        }

    for key,value in top_game.items():
        print(key,value)
