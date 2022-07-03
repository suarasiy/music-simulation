from pythonds.basic.queue import Queue as Q
from json import dumps
from colorama import Fore, Back, Style


# test
# DO_EXPECT = {'title': '__some_title', 'order': '__number_order'}


class Order(Q):

    def __init__(self):
        super().__init__()

    def __repr__(self):
        dumps_order = dumps(self.items, indent=3)
        return f"{dumps_order}"

    def __str__(self):
        """
        ♫ Music playlist ♪
        [1] <first_order_music> || <- CURRENT
        [2] <first_order_music> || <- NEXT
        [3] <first_order_music>
        [4] <first_order_music>
        [5] <first_order_music> || <- LAST
        """
        mp = f"\n{Fore.YELLOW}♫ Music{Fore.RESET} {Fore.CYAN}playlist ♪{Fore.RESET}\n"
        if self.size() == 0:
            mp += f'\n{Back.RED}Playlist Kosong.{Back.RESET}\n'
        else:
            for idx, playlist in enumerate(self.items):
                if 'current' in playlist:
                    # default pattern using format manipulation
                    # mp += "{}[{}] {} 【{} seconds.】(reg: {}) || <- CURRENT\n".format(
                    #     self.size() - idx, playlist['title'], playlist['duration'], playlist['number registered'])
                    mp += f"{Fore.GREEN}[{self.size() - idx}]{Fore.RESET} {Fore.LIGHTBLUE_EX}{playlist['title']}{Fore.RESET} 【{playlist['duration']} seconds.】(reg: {Fore.BLUE}{playlist['number registered']}{Fore.RESET}) || <- {Back.LIGHTBLUE_EX}{Fore.BLACK} CURRENT {Style.RESET_ALL}\n"
                else:
                    mp += f"{Fore.GREEN}[{self.size() - idx}]{Fore.RESET} {playlist['title']} 【{playlist['duration']} seconds.】(reg: {Fore.BLUE}{playlist['number registered']}{Fore.RESET})\n"

        return mp

    def __interface(self, _title, _duration, _index, _number_registered):
        return {
            'title': _title,
            'duration': _duration,
            'index': _index,
            'number registered': _number_registered
        }

    def add_order(self, items, duration):
        item = self.__interface(
            items,
            duration,
            self.size(),
            self.size() + 1,
        )

        Q.enqueue(self, item)

    def value_error(self, message):
        raise ValueError(message)

    def type_error(self, message):
        raise TypeError(message)

    def index_error(self, message):
        raise IndexError(message)

    def order_swap(self, from_number, to_number):
        if from_number <= 0 or to_number <= 0 or from_number > self.size() or to_number > self.size():
            raise IndexError('Nomor track tidak ditemukan.')

        index_from_number = Q.size(self) - from_number
        index_to_number = Q.size(self) - to_number

        previous = self.items[index_from_number] if len(self.items) > index_from_number else self.index_error(
            f'Playlist urutan ke-{index_from_number+1} tidak ditemukan.')
        next = self.items[index_to_number] if len(self.items) > index_to_number else self.index_error(
            f'Playlist urutan ke-{index_to_number+1} tidak ditemukan.')

        self.items[index_from_number] = next
        self.items[index_to_number] = previous

        self.items[index_from_number]['index'] = self.items.index(previous)
        self.items[index_to_number]['index'] = self.items.index(next)

        print(
            '\n{} dipindah ke posisi-{}\n'.format(previous['title'], self.size() - self.items.index(previous)))
        return self.__str__()


# test
# order = Order()
# order.add_order(
#     'Mischievous Sensation [Shinra-bansho official]')
# order.add_order('Sakuzyo - pathetic')
# order.add_order('Sakuzyo - apathy')


# print(order)
# print('===')
# order.order_swap(1, 2)
# print('====')
# print(order)
