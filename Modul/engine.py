import models
import settings
<<<<<<< HEAD

boss_level = settings.BOSS_LEVEL
=======
import exceptions
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000


def get_player_name():
    gamer_name = ''
<<<<<<< HEAD
    while len(gamer_name) == 0:
=======
    while not gamer_name:
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000
        gamer_name = input("Введіть ім'я:").strip()
    print(f'Вітаю, {gamer_name}!')
    return gamer_name


<<<<<<< HEAD
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
=======
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
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000


try:
    play()
except KeyboardInterrupt:
    print('\n До зустрічі!')
