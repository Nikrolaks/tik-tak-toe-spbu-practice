import random


class TikTakToeManager:
    def __init__(self, name_1='Looser-Иван_Пупкин', name_2='Looser-Семён_Семёныч'):
        useless_mas = [name_1, name_2]
        first = random.randint(0, 1)
        self.first_gamer = useless_mas[first]
        self.second_gamer = useless_mas[1 - first]
        self.move = 0
        self.is_end = False
        self.frame = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]
        print('Первым ходит: {0}\n'
              'Ходит знаком X\n'
              'Вражила - знаком O'.format(self.first_gamer))

    def whose_move(self):
        whose = self.second_gamer if self.move else self.first_gamer
        print('Ход делает {0}'.format(whose))
        return tuple([self.move*1, whose])

    def do_move(self, wherewith_x_or_o, where_to_go_outer_scope_urod):
        if 'X' != wherewith_x_or_o and 'O' != wherewith_x_or_o:
            print('Нет таких фишек в игре')
            return -1
        whose_sign = (wherewith_x_or_o == 'X') * 1 + (wherewith_x_or_o == 'O') * 2
        if whose_sign-1 != self.move*1:
            whose_sign = self.first_gamer if self.move else self.second_gamer
            print('Это не твой ход, {0} :/'.format(whose_sign))
            return -2
        if \
                where_to_go_outer_scope_urod[0] > 2\
                or where_to_go_outer_scope_urod[1] > 2\
                or where_to_go_outer_scope_urod[0] < 0\
                or where_to_go_outer_scope_urod[1] < 0:
            print('Поле не настолько большое')
            return -3
        if self.is_end:
            print('Игра окончена')
            return -4
        if self.frame[where_to_go_outer_scope_urod[0] + where_to_go_outer_scope_urod[1] * 3]:
            print('Сюда уже кто-то ходил до тебя')
            return -5
        self.frame[where_to_go_outer_scope_urod[0] + where_to_go_outer_scope_urod[1] * 3] = whose_sign
        var = \
            ((self.frame[0] == whose_sign)
             and (self.frame[1] == whose_sign)
             and (self.frame[2] == whose_sign))

        var = \
            ((self.frame[3] == whose_sign)
             and (self.frame[4] == whose_sign)
             and (self.frame[5] == whose_sign))\
            or var
        var = \
            ((self.frame[6] == whose_sign)
             and (self.frame[7] == whose_sign)
             and (self.frame[8] == whose_sign))\
            or var
        var = \
            ((self.frame[0] == whose_sign)
             and (self.frame[3] == whose_sign)
             and (self.frame[6] == whose_sign))\
            or var
        var = \
            ((self.frame[1] == whose_sign)
             and (self.frame[4] == whose_sign)
             and (self.frame[7] == whose_sign))\
            or var
        var = \
            ((self.frame[2] == whose_sign)
             and (self.frame[5] == whose_sign)
             and (self.frame[8] == whose_sign))\
            or var
        var = \
            ((self.frame[0] == whose_sign)
             and (self.frame[4] == whose_sign)
             and (self.frame[8] == whose_sign))\
            or var
        var = \
            ((self.frame[2] == whose_sign)
             and (self.frame[4] == whose_sign)
             and (self.frame[6] == whose_sign))\
            or var
        self.is_end = var
        self.move = not self.move
        return self

    def is_this_the_end(self):
        if self.is_end:
            print('Игра завершена')
        else:
            print('Игра в процессе')
        return not self.is_end

    def who_is_winner(self):
        if not self.is_end:
            print('Все проиграли. Шучу\nИгра в процессе')
            return -1
        whose_win = self.first_gamer if self.move else self.second_gamer
        print('ПОБЕДА И ОВАЦИИ ДОСТАЮТСЯ.............{0}'.format(whose_win))
        return whose_win

    def draw_frame(self):
        useless_mas = ['¤', 'X', 'O']
        for i in range(3):
            print('{0}\t{1}\t{2}\t'.format(useless_mas[self.frame[i*3 + 0]],
                                           useless_mas[self.frame[i*3 + 1]],
                                           useless_mas[self.frame[i*3 + 2]]))
        return self


game = TikTakToeManager()
while game.is_this_the_end():
    whose_move = game.whose_move()[0]
    game.draw_frame()
    where_to_go = [0, 0]
    is_o_or_x = input()
    where_to_go[0] = int(input())
    where_to_go[1] = int(input())
    game.do_move(is_o_or_x, where_to_go)
game.who_is_winner()
