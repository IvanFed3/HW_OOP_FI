import random
import settings
import exceptions


class Enemy:
    def __init__(self, level, score=0):
        self.level = level
        self.health = self.level
        self.score = score

    def descrease_health(self):
        self.health -= 1
        if self.health < 1:
            raise exceptions.EnemyDown

    @staticmethod
    def action():
        return random.choice(settings.VALID_CHOICES)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = settings.INITIAL_PLAYER_HEALTH
        self.score = 0

    def descrease_health(self):
        self.health -= 1
        if self.health < 1:
            raise exceptions.GameOver

    @staticmethod
    def action(side):
        action = 0
        while action not in map(str, settings.VALID_CHOICES):
            action = input(f'Виберіть героя для {side} ВОЇН -1, ГРАБІЖНИК -2, ЧАКЛУН -3 : ')
        return settings.VALID_CHOICES[int(action)]

    @staticmethod
    def fight(attack, defence):
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
            print('НІЧИЯ!')
            return result_fight

    def defence(self, enemy):
        print("ЗАХИЩАЙСЯ")
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
            print('НІЧИЯ!')
            return result_fight
