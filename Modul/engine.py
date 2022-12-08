import models
import settings

boss_level = settings.BOSS_LEVEL


def get_player_name():
    gamer_name = ''
    while len(gamer_name) == 0:
        gamer_name = input("Введіть ім'я:").strip()
    print(f'Вітаю, {gamer_name}!')
    return gamer_name


def end_game(score, gamer_name):
    print('GAME OVER.')
    print(f'{gamer_name}, ти набрав {score} балів.')
    print('До зустрічі!')


def play():
    gamer_name = get_player_name()
    gamer = models.Player(gamer_name)
    level = boss_level
    boss = models.Enemy(level)
    while gamer.health > 0:
        temp_boss_health = boss.health
        gamer.attack(boss)
        if boss.health > temp_boss_health:
            gamer.attack(boss)
        gamer.defence(boss)
    score = gamer.score + boss.score
    end_game(score, gamer_name)


try:
    play()
except KeyboardInterrupt:
    print('\n До зустрічі!')
