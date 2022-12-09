import random
import settings
<<<<<<< HEAD


initial_player_health = settings.INITIAL_PLAYER_HEALTH
heroes = settings.HEROES
choice_heroes = settings.CHOICE_HEROES
result = settings.RESULT
score_for_local = settings.SCORE_FOR_LOCAL
score_for_win = settings.SCORE_FOR_WIN


class Enemy:
    def __init__(self, level):
        self.level = level
        self.health = self.level
        self.score = 0

    def descrease_health(self):
        self.health -= 1
        if self.health == 0:
            print("Ви ПЕРЕМОГЛИ.")
            self.level += 1
            self.score += score_for_win
            self.health = self.level
            print(f"РАУНД {self.level}")

    def select_attack(self):
        return heroes.index(random.choice(heroes))

    def select_defence(self):
        return heroes.index(random.choice(heroes))
=======
import exceptions


class Enemy:
    def __init__(self, level, score=0):
        self.level = level
        self.health = self.level
        self.score = score

    def new_level(self):
        level = self.level + 1
        print("Ви ПЕРЕМОГЛИ!")
        print(f"РАУНД {level}")
        self.score += settings.SCORE_FOR_WIN
        new_enemy = Enemy(level, self.score)
        return new_enemy

    def descrease_health(self):
        self.health -= 1

    def action(self):
        return random.choice(settings.VALID_CHOICES)
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000


class Player:
    def __init__(self, name: str):
        self.name = name
<<<<<<< HEAD
        self.health = initial_player_health
=======
        self.health = settings.INITIAL_PLAYER_HEALTH
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000
        self.score = 0

    def descrease_health(self):
        self.health -= 1
<<<<<<< HEAD

    def select_attack(self):
        attack = 0
        while attack not in choice_heroes:
            attack = input('Виберіть героя для атаки ВОЇН -1, ГРАБІЖНИК -2, ЧАКЛУН -3 : ')
        return heroes.index(heroes[int(attack) - 1])

    def select_defence(self):
        defence = 0
        while defence not in choice_heroes:
            defence = input('Виберіть героя для захисту ВОЇН -1, ГРАБІЖНИК -2, ЧАКЛУН -3 : ')
        return heroes.index(heroes[int(defence) - 1])

    def fight(self, attack, defence):
        if attack == 0 and defence == 1:
            return result[0]
        elif attack == 1 and defence == 2:
            return result[0]
        elif attack == 2 and defence == 0:
            return result[0]
        elif attack == defence:
            return result[2]
        else:
            return result[1]

    def attack(self, enemy):
        print("АТАКУЙ")
        result_fight = self.fight(self.select_attack(), enemy.select_defence())
        if result_fight == result[0]:
            print('Твоя атака УСПІШНА!')
            enemy.descrease_health()
            self.score += score_for_local
            return result_fight
        elif result_fight == result[1]:
            print('Нажаль ПРОВАЛ!')
            return result_fight
        elif result_fight == result[2]:
=======
        try:
            if self.health < 1:
                raise exceptions.GameOver
        except exceptions.GameOver:
            print('GAME OVER.')

    def action(self, side):
        action = 0
        while action not in map(str, settings.VALID_CHOICES):
            action = input(f'Виберіть героя для {side} ВОЇН -1, ГРАБІЖНИК -2, ЧАКЛУН -3 : ')
        return settings.VALID_CHOICES[int(action)]

    def fight(self, attack, defence):
        if attack == settings.WARRIOR and defence == settings.ROBBER:
            return settings.WIN
        elif attack == settings.ROBBER and defence == settings.WIZARD:
            return settings.WIN
        elif attack == settings.WIZARD and defence == settings.WARRIOR:
            return settings.WIN
        elif attack == defence:
            return settings.DRAW
        else:
            return settings.LOSE

    def attack(self, enemy):
        print("АТАКУЙ")
        attack = self.action('атаки')
        defence = enemy.action()
        result_fight = self.fight(attack, defence)
        if result_fight == settings.WIN:
            print('Твоя атака УСПІШНА!')
            enemy.descrease_health()
            self.score += settings.SCORE_FOR_LOCAL_WIN
            return result_fight
        elif result_fight == settings.LOSE:
            print('Нажаль ПРОВАЛ!')
            return result_fight
        elif result_fight == settings.DRAW:
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000
            print('НІЧИЯ!')
            return result_fight

    def defence(self, enemy):
        print("ЗАХИЩАЙСЯ")
<<<<<<< HEAD
        result_fight = self.fight(self.select_defence(), enemy.select_attack())
        if result_fight == result[0]:
            print('Захист УСПІШНИЙ!')
            return result_fight
        elif result_fight == result[1]:
            print('Нажаль ПРОВАЛ!')
            self.descrease_health()
            return result_fight
        elif result_fight == result[2]:
=======
        attack = self.action('захисту')
        defence = enemy.action()
        result_fight = self.fight(attack, defence)
        if result_fight == settings.WIN:
            print('Захист УСПІШНИЙ!')
            return result_fight
        elif result_fight == settings.LOSE:
            print('Нажаль ПРОВАЛ!')
            self.descrease_health()
            return result_fight
        elif result_fight == settings.DRAW:
>>>>>>> c94ddcfe4a6340125cf13fa0510b77193e97e000
            print('НІЧИЯ!')
            return result_fight
