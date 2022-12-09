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
    while gamer.health > 0:
        gamer.attack(boss)
        try:
            if boss.health < 1:
                raise exceptions.EnemyDown
        except exceptions.EnemyDown:
            boss = boss.new_level()
            gamer.attack(boss)
        gamer.defence(boss)
    print(f'{gamer.name}, ти набрав {boss.score + gamer.score} балів.')
    print('До зустрічі!')


try:
    play()
except KeyboardInterrupt:
    print('\n До зустрічі!')
