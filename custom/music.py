# program music queue

from pythonds.basic.queue import Queue as Q
from custom.interface import Order
from time import sleep
import random
from colorama import Fore


class Music(Order, Q):

    def __init__(self):
        self.shuffle = False
        super().__init__()

    def get_shuffle(self):
        return self.shuffle

    def set_shuffle(self):
        self.shuffle = not self.shuffle
        return self.shuffle

    def play(self):
        if len(self.items) == 0:
            print(f'{Fore.GREEN}All music successfully played.{Fore.RESET}\n')
            return
        try:
            if len(self.items) > 0:
                current = self.items[len(self.items)-1]
                current['current'] = True
                self.items[len(self.items)-1] = current
                print('{}'.format(Order.__str__(self)))
                print(
                    f"\n{Fore.BLUE}:: Playing music {current['title']} 【{current['duration']} seconds.】 ::{Fore.RESET}\n")
                sleep(current['duration'])
                if self.shuffle:
                    _ = self.dequeue()
                    del _['current']
                    self.enqueue(_)
                else:
                    self.dequeue()
                print(f'\n{Fore.YELLOW}Success.{Fore.RESET} {Fore.CYAN}Playing next...{Fore.RESET}\n') if len(
                    self.items) > 0 else None
                self.play()
            else:
                print(f'{Fore.GREEN}All music successfully played.{Fore.RESET}\n')
                return
        except KeyboardInterrupt:
            print(f'\n{Fore.RED}Player dihentikan.{Fore.RESET}\n')

    class RandomDuration():
        def __init__(self):
            # O(n)
            self.DEMO_DURATION = [1, 2, 3, 4, 5]

        def __str__(self):
            return f"{self.DEMO_DURATION}"

        def __call__(self):
            return random.choice(self.DEMO_DURATION)

    def __bubbleSortWKey(self, alist, _key):
        for passnum in range(len(alist) - 1, 0, -1):
            for i in range(passnum):
                if alist[i][_key] < alist[i+1][_key]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp

    def sort_by_reg(self):
        self.__bubbleSortWKey(self.items, 'number registered')
        print(Order.__str__(self))

    def sort_by_az(self):
        self.items = sorted(
            self.items, key=lambda d: d['title'], reverse=True)
        print(Order.__str__(self))

    def __str__(self):
        return "{}".format(Order.__str__(self))

    def get_music(self, index):
        if index <= 0:
            raise IndexError('Nomor track tidak ditemukan.')
        return self.items[self.size() - index]

    def add_music(self, playlists):
        random_duration = self.RandomDuration()
        if type(playlists) == str:
            Order.add_order(self, playlists, random_duration())
            print(Order.__str__(self))
            return

        if type(playlists) == list:
            pls = self.flatten(playlists)
            for pl in pls:
                Order.add_order(self, pl, random_duration())
            return

    def add_dummy_music(self):
        playlist = [
            "Sakuzyo - Apathy",
            "Sakuzyo - l'aventale",
            "Himmel - 心彩",
            "Sakuzyo - endrole",
            ['Sakuzyo - trinity', 'Sakuzyo - hoodie', 'Sakuzyo - axion'],
            [
                ['xi - world fragment', 'xi - niflheimr'],
                'あるか - Bye-Bye Ainsel',
                [
                    'Yuki Kajiura - Quiet Romance', 'Masaru Yokoyama - La Pucelle',
                    [
                        'Noah - Revolt from the abyss',
                        'Shinra-Bansho - Mischievous Sensation'
                    ]
                ]
            ]
        ]

        self.add_music(playlist)

        print(Order.__str__(self))

    def remove_music(self, n):
        if n <= 0:
            print('Nomor track tidak ditemukan')
        if len(self.items) >= n:
            # filtered shallow copy
            distinct_playlist = [
                x for x in self.items if not x['index'] == n-1]
            self.items = distinct_playlist
            print('Track berhasil dihapus.')
            print(Order.__str__(self))
        return

    def flatten(self, lists):
        flatlist = []
        # ['', '', ''] // [['', ''], '', '']
        if type(lists) == list:
            for elem in lists:
                if type(elem) == list:
                    flatlist += self.flatten(elem)
                else:
                    flatlist.append(elem)
            return flatlist

        if type(lists) == str:
            return lists


# test
# player = Music()
# player.add_music("Sakuzyo - Pathethic")
# playlist = [
#     "sakuzyo - Apathy",
#     "sakuzyo - l'aventale",
#     "himmel - 心彩",
#     ['sakuzyo - trinity', 'sakuzyo - hoodie', 'sakuzyo - axion'],
#     [['xi - world fragment', 'xi - niflheimr'], 'あるか - Bye-Bye Ainsel', ['Yuki Kajiura - Quiet Romance', 'Masaru Yokoyama - La Pucelle']]
# ]
# player.add_music(playlist)
# print('\n', player)
# print('pindah 6 ke 1')
# player.order_swap(6, 1)
# print('\n', player)
# player.dequeue()
# print('\n', player)
# music = player.get_music(2)
# print("[{}] {} 【{} seconds.】\n".format(2, music['title'], music['duration']))
