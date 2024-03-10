def save_word(word, file):
    with open(file, 'a') as f:
        f.write(word + '\n')


def game_word(file):
    print("start game! enter word:")
    last_word = input().lower()
    save_word(last_word, file)

    while True:
        new_word = input(
            "enter word starting with the last letter of the previous one (or 'stop' to end the game)").lower()

        if new_word == 'stop':
            break

        if not new_word.startswith(last_word[-1]):
            print("word must begin with the last letter of the previous one!")
            break

        save_word(new_word, file)
        last_word = new_word


game_file = "word.txt"
game_word(game_file)