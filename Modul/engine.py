import models
import settings
import exceptions


def get_player_name():
    gamer_name = ''
    while not gamer_name:
        gamer_name = input("Введіть ім'я:").strip()
    print(f'Вітаю, {gamer_name}!')
    return gamer_name


def play():
    gamer_name = get_player_name()
    gamer = models.Player(gamer_name)
    boss = models.Enemy(settings.BOSS_LEVEL)
    while True:
        try:
            gamer.attack(boss)
            gamer.defence(boss)
        except exceptions.EnemyDown:
            boss = models.Enemy(boss.level + 1)
            print("Ви ПЕРЕМОГЛИ!")
            print(f"РАУНД {boss.level}")
            gamer.score += settings.SCORE_FOR_WIN
        except exceptions.GameOver:
            print('GAME OVER.')
            print(f'{gamer.name}, ти набрав {gamer.score} балів.')
            print('До зустрічі!')
            break


try:
    play()
except KeyboardInterrupt:
    print('\n До зустрічі!')
