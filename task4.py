for game in video_game_sales:
    if game[GLOBAL_SALES]>25:
       print(game[NAME],game[GLOBAL_SALES])
        
pre_2000_count=0
for game in video_game_sales:
    if game[YEAR]<2000:
        pre_2000_count=pre_2000_count+1

print(pre_2000_count)

na_total=0
jp_total=0

for game in video_game_sales:
  na_total += game[NA_SALES]
  jp_total += game[JP_SALES]

print(na_total)
print(jp_total)

if na_total>jp_total:
    print("North America had higher sales")
else :
    print("Japan has higher sales")

nintendo_games=[]
for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(nintendo_games)
print(len(nintendo_games))

