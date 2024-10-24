import os, time, json

class Connect_4(object):
    def __init__(self) -> None:
        self.col_codex = 'abcdefghi'
        self.ln_codex = range(1, 10)

        self.place = ''

        if 'memory.json' in os.listdir():
            self.memory, self.turn = self.autoload()
        else:
            self.memory, self.turn = {col + str(ln): ' ' for col in self.col_codex for ln in self.ln_codex}, 'X'

    def ui(func):
        def wrapper(*args, **kwargs):
            logo = """
       ______                            __     ______                
      / ____/___  ____  ____  ___  _____/ /_   / ____/___  __  _______
     / /   / __ \/ __ \/ __ \/ _ \/ ___/ __/  / /_  / __ \/ / / / ___/
    / /___/ /_/ / / / / / / /  __/ /__/ /_   / __/ / /_/ / /_/ / /    
    \____/\____/_/ /_/_/ /_/\___/\___/\__/  /_/    \____/\__,_/_/     



"""
            foo = func(*args, **kwargs)
            new = ''
            for i in foo.split('\n'):
                new += '\t\t\t\t{}\n'.format(i)

            return logo + new
        return wrapper
    
    @ui
    def playground(self) -> str:
        sidewalls = 'Π'
        for key, value in self.memory.items():
            sidewalls += value

            if key[1] == '9':
                if key[0] == 'i':
                    sidewalls += 'Π\n'
                elif key[0] == 'd':
                    sidewalls += "Π\t{} sırası\nΠ".format(self.turn)
                else:
                    sidewalls += 'Π\nΠ'
        ground = 'Ξ' * 11

        return sidewalls + ground
    
    @ui
    def celebration(self, winner: str):
        fireworks_df = """               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '"""
        fireworks = """               *    *
   *         '       *       .  *   '     .           * *
                                                               '
   *                     *'          *          *        '
   .         *                 |               /
               '.         |    |        '     |    '      *
                 \*        \   \             / 
       '          \    '*  |    |    *      |*                  *  *
            *      `.       \   |      *     /      *      '
  .                  \      |   \          /                *
     *'  *     '      \      \   '.       |
        -._            `                  /            *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='          *
             .  '      *       *    *   .       _.:--'
    *               . Oyun BİTTİ, {} kazandı!-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
            *           _.'  .'       `.        '   *              *
    *            *  _.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                    *                    `
               *        '             '                          .
     .                         *          .           *  *
         *          .                                    '""".format(winner)
        
        os.remove("memory.json")
        os.remove("moves.txt")
        self.memory, self.turn = {col + str(ln): ' ' for col in self.col_codex for ln in self.ln_codex}, 'X'

        for i in range(5):
            os.system("cls")
            print(fireworks_df)
            time.sleep(1)
            os.system("cls")
            print(fireworks)
            time.sleep(1)

        return ""

    def autoload(self):
        with open("memory.json", "r") as file:
            load = json.loads(file.read())
            return load["memory"], load["turn"]

    def autosave(self):
        with open("memory.json", "w") as file:
            json.dump({'memory': self.memory, 'turn': self.turn}, file)
        with open("moves.txt", "a") as file:
            file.write("{}>>> {} kullanıcısı, {} satıra oynadı.\n".format(time.strftime("%H: %M: %S"), self.turn, self.place))

    def input(self) -> None:
        while True:
            move = str(input("Sayı? (1-9) = "))

            if int(move) in range(1, 10):
                break

        self.brain(move)

    def brain(self, input):
        def check(place: str) -> bool:
            col, ln = place

            col_ = self.col_codex.find(col)
            ln_ = int(ln)
            horizontal_check = ''
            vertical_check = ''
            cross_check_1 = ''
            cross_check_2 = ''
            for h, v, nh in zip(range(ln_ - 3, ln_ + 4), range(col_ - 3, col_ + 4), range(ln_ + 4, ln_ - 3, -1)):
                try:
                    horizontal_check += self.memory[col + str(h)] #Horizontal
                except:
                    pass
                try:
                    vertical_check += self.memory[self.col_codex[v] + ln] #Vertical
                except:
                    pass
                try:
                    cross_check_1 += self.memory[self.col_codex[v] + str(h)] #Left to right cross
                except:
                    pass
                try:
                    cross_check_2 += self.memory[self.col_codex[v] + str(nh)] #Right to left cross
                except:
                    pass

            con = self.turn * 4
            if horizontal_check.find(con) != -1 or vertical_check.find(con) != -1 or cross_check_1.find(con) != -1 or cross_check_2.find(con) != -1:
                return True

            return False
        
        queue = -1
        while True:
            try:
                self.col_codex[queue]
            except IndexError:
                break
            else:
                if self.memory[self.col_codex[queue] + input] == ' ':
                    self.memory[self.col_codex[queue] + input] = self.turn
                    self.place = self.col_codex[queue] + input

                    if check(self.col_codex[queue] + input):
                        self.celebration(self.turn)
                    
                    self.turn = 'O' if self.turn == 'X' else 'X'

                    self.autosave()
                    break
                else:
                    queue -= 1

foo = Connect_4()

while True:
    os.system('cls')
    print(foo.playground())
    foo.input()
