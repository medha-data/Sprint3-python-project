ame_name=video_game_sales[4][NAME]
pokemon=game_name[:7]
print(pokemon)

for name in messy_names:
    clean_name=name.strip().lower()
    print(clean_name)

best_game=video_game_sales[0]
print(
    f"#{best_game[RANK]} Best Seller: {best_game[NAME]} "
    f"({best_game[YEAR]}) - ${best_game[GLOBAL_SALES]}M global sales"
)
