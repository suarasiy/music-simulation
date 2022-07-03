# import os
# import sys
from custom.music import Music
from colorama import init, Fore, Back, Style

init()


class Menu(Music):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"""\n
  {Back.LIGHTBLUE_EX} {Fore.BLACK} Music Player [♪] {Style.RESET_ALL}\n
  {Fore.GREEN}[1]{Fore.RESET} : tambah musik
  {Fore.GREEN}[2]{Fore.RESET} : hapus musik
  {Fore.GREEN}[3]{Fore.RESET} : pindah musik (swap)
  {Fore.GREEN}[4]{Fore.RESET} : play (queue)
  {Fore.GREEN}[5]{Fore.RESET} : shuffle (status: {f"{Fore.GREEN}on{Fore.RESET}" if Music.get_shuffle(self) else f"{Fore.RED}off{Fore.RESET}"})
  {Fore.GREEN}[6]{Fore.RESET} : index musik
  {Fore.GREEN}[7]{Fore.RESET} : list musik
  {Fore.GREEN}[8]{Fore.RESET} : tambah musik (dummy)
  {Fore.GREEN}[9]{Fore.RESET} : sort (by number registered or A-Z)
  {Fore.GREEN}[0]{Fore.RESET} : exit
    """
    # """.format("on" if Music.get_shuffle(self) else "off")

    def __errnokey(self):
        print(
            f'\n {Fore.RED}Keyword tidak tepat. Pointer kembali ke menu... {Fore.RESET}\n')

    def __cm(self):
        try:
            return int(input("[command] >> "))
        except ValueError:
            self.__errnokey()
            return self.__cm()

    def start_init(self):
        cm = self.__cm()
        while cm:
            if cm == 1:
                input_title = str(input('\n[input] Judul musik : '))
                print(self.__str__())
                Music.add_music(self, input_title)
                cm = self.__cm()
                continue
            if cm == 2:
                try:
                    _ = int(input('\n[input reg] Pilih musik untuk dihapus : '))
                except ValueError:
                    self.__errnokey()
                    cm = self.__cm()
                    continue
                print(self.__str__())
                Music.remove_music(self, _)
                cm = self.__cm()
                continue
            if cm == 3:
                try:
                    _ = str(
                        input('\n[<dari_urutan> <ke_urutan>] pilih musik : ')).split(" ")
                    assert len(_) == 2
                except AssertionError:
                    self.__errnokey()
                    cm = self.__cm()
                    continue
                _from, _to = int(_[0]), int(_[1])
                print(self.__str__())
                Music.order_swap(self, _from, _to)
                print(Music.__str__(self))
                cm = self.__cm()
                continue
            if cm == 4:
                print('\nMusik sedang di play berdasarkan queue.\n')
                Music.play(self)
                cm = self.__cm()
                continue
            if cm == 5:
                Music.set_shuffle(self)
                print(
                    '\nShuffle di-{}kan.'.format("aktif" if Music.get_shuffle(self) else "Nonaktif"))
                print(self.__str__())
                cm = self.__cm()
                continue
            elif cm == 6:
                input_index = int(input('\n[input] Index musik : '))
                music = Music.get_music(self, input_index)
                print("[{}] {} 【{} seconds.】\n".format(
                    input_index, music['title'], music['duration']))
                cm = self.__cm()
                continue
            elif cm == 7:
                print(Music.__str__(self))
                cm = self.__cm()
                continue
            elif cm == 8:
                Music.add_dummy_music(self)
                cm = self.__cm()
                continue
            elif cm == 9:
                print(f"""\n
                {Fore.GREEN}[1]{Fore.RESET} Urut dari nomor registrasi (init {Fore.RESET}queue{Fore.RESET})
                {Fore.GREEN}[2]{Fore.RESET} Urut dari abjad ({Fore.CYAN}A-Z{Fore.RESET})
                """)
                _ = int(input("\n[input] Index sortir : "))
                if _ == 1:
                    Music.sort_by_reg(self)
                    cm = self.__cm()
                    continue
                elif _ == 2:
                    Music.sort_by_az(self)
                    cm = self.__cm()
                    continue
                else:
                    self.__errnokey()
                    cm = self.__cm()
                    continue
            elif cm == 0:
                break
            else:
                self.__errnokey()
                cm = self.__cm()
                continue


def main():
    menu = Menu()
    print(menu)
    menu.start_init()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n\n{Back.RED}Program dihentikan.{Back.RESET}')
        # try:
        #     sys.exit(0)
        # except SystemExit:
        #     os._exit(0)
