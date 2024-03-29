# engine file for Py Game Tell Engine
import sys

import pygame

from configfile import screen, clock


class ScenarioCommands:
    def __init__(self):
        self.sc_file = str()
        self.scenario = str()
        self.musics = dict()
        self.sounds = dict()
        self.pos_x = 0
        self.pos_y = 0
        self.gfont = "consolas"
        self.backgrounds = {"black": pygame.image.load("engine_imgs/black_1366_768.png")}
        self.pfont = pygame.font.SysFont(self.gfont, 32)
        self.tfont = pygame.font.SysFont(self.gfont, 20)
        self.cfont = pygame.font.SysFont(self.gfont, 45)
        self.choice_bg = pygame.image.load("engine_imgs/choice_bg.png")
        self.txt_bg = pygame.image.load("engine_imgs/txt_bg.png")
        self.personages = dict()
        self.bg = "black"
        self.cur_text = ""
        self.pers_is_show = False
        self.cur_perses = []

        # =============================================================================================================
        # Команды в файле сценария:
        #
        # play_music(music) - проигрывание фоновой музыки
        # stop_music() - остановить проигрыванние музыки
        # bg_img(file) - фоновое изображение
        # tell(pers, text) - Отобразить text сказанный персонажем pers
        # play_sound(file) - Проиграть звук
        # pers_init(name, color, cn, sprites) - Создать класс pers и объявить его имя в игре - name
        # Определить цвет имени в игре - color; sprites - список путей к спрайтам игры
        # hide() - спрятать персонажа
        # show(pers, pose, pos_x, pos_y) - показать персонажа pers с позой pose в позиции x: pos_x; y: pos_y
        # pers_pose(pers, file) - выбрать file с позой для персонажа pers
        # init_music(path, music) - путь path к музыке, music ключ для обращения в словарь с музыкой
        # init_sound(path, sound) - путь path к звуку, music ключ для обращения в словарь со звуками
        # init_bg(path, bg) - путь path к фону, bg ключ для обращения в словарь с фонами
        # choice(choices) - создает выбор из choices и возвращает цифру в зависимости от выбора
        #
        # =============================================================================================================
        #
        # !!!ПОКА НЕ РАБОТАЕТ!!!
        # Условные знаки в тексте:
        #
        # ~p~ - пауза в диалоге
        # ~t~Text~t~ - Курсив
        # ~m~Text~m~ - Жирный шрифт

    def play_music(self, music):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.musics[music])
            pygame.mixer.music.play(loops=-1)
        except:
            print(f"A music file named {music} was not found")

    def stop_music(self):
        pygame.mixer.music.stop()

    def init_music(self, path, music):
        self.musics[music] = path

    def init_sound(self, path, sound):
        self.sounds[sound] = path

    def play_sound(self, sound):
        try:
            pygame.mixer.init()
            s = pygame.mixer.Sound(self.sounds[sound])
            s.play()
        except:
            print(f"A sound file named {sound} was not found")

    def bg_img(self, bg="black"):
        screen.blit(self.backgrounds[bg], (0, 0))
        self.bg = bg
        screen.blit(self.txt_bg, (0, 638))

    def init_bg(self, path, bg):
        self.backgrounds[bg] = pygame.image.load(path)

    def tell(self, cn, text):
        self.bg_img(self.bg)
        personage_txt = self.pfont.render(self.personages[cn].name, True, self.personages[cn].color)
        screen.blit(personage_txt, (35, 645))
        pygame.display.flip()
        running = True
        txt_counter = 0
        row_count = 0
        col_count = 0
        screen.blit(self.backgrounds[self.bg], (0, 0))
        if(self.pers_is_show):
            for i in self.cur_perses:
                screen.blit(self.personages[i].sprites[self.personages[i].pose],
                            (self.personages[i].pos_x, self.personages[i].pos_y))
        screen.blit(self.txt_bg, (0, 638))
        screen.blit(personage_txt, (35, 645))

        while running and txt_counter < len(text):
            if pygame.key.get_pressed()[pygame.K_TAB]:
                running = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if(row_count > 122):
                row_count = 0
                col_count += 1

            blit_txt = self.tfont.render(text[txt_counter], True, (201, 201, 201))
            screen.blit(blit_txt, (12 + (row_count * 11), 680 + (col_count * 20)))
            clock.tick(60)
            pygame.display.flip()
            # else:
            #     screen.blit(self.txt_bg, (0, 638))
            #     screen.blit(personage_txt, (35, 645))
            #     screen.blit(blit_txt, (12, 680))
            #     clock.tick(60)
            #     pygame.display.flip()
            # print(clock.get_fps())
            txt_counter += 1
            row_count += 1

        # blit_txt = self.tfont.render(text, True, (201, 201, 201))
        # screen.blit(blit_txt, (12, 680))
        # pygame.display.flip()
        self.cur_text = self.text_printing(text)
        running = True
        while running:
            if pygame.key.get_pressed()[pygame.K_TAB]:
                running = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def show(self, pers, pose, pos_x=0, pos_y=0):
        self.pers_is_show = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        if(pers not in self.cur_perses):
            self.cur_perses.append(pers)
        self.personages[pers].pose = pose
        self.personages[pers].pos_x = pos_x
        self.personages[pers].pos_y = pos_y
        # screen.blit(self.backgrounds[self.bg], (0, 0))
        # screen.blit(self.personages[pers].sprites[pose], (-15, -150))
        # screen.blit(self.txt_bg, (0, 638))
        # screen.blit(self.cur_text, (12, 680))
        pygame.display.flip()

    def text_printing(self, text):
        if(len(text) > 122):
            rows = len(text) // 122 + 1
        else:
            blit_txt = self.tfont.render(text, True, (201, 201, 201))
            screen.blit(blit_txt, (12, 680))
            pygame.display.flip()

            return blit_txt

        for i in range(rows):
            blit_txt = self.tfont.render(text[122*i:122*(i+1)], True, (201, 201, 201))
            screen.blit(blit_txt, (12, 680 + (i * 20)))
        pygame.display.flip()

        blit_txt = self.tfont.render(text, True, (201, 201, 201))
        return blit_txt

    def hide(self, pers):
        self.cur_perses.remove(pers)
        if(len(self.cur_perses) == 0):
            self.pers_is_show = False

        # screen.blit(self.backgrounds[self.bg], (0, 0))
        # screen.blit(self.txt_bg, (0, 638))
        # screen.blit(self.cur_text, (12, 680))
        # pygame.display.flip()

    def pers_init(self, name, color, cn, sprites):
        self.personages[cn] = Personage(name, color, cn, sprites)

    def choice(self, *choices):
        count = 0
        choices_rects = []
        pcenter = (768 - 45 * len(choices) - 5 * (len(choices) - 1)) // 2
        for txt in choices:  # (768 - 17 * len(choices) - 2 * (n - 1)) // 2
            txt = self.cfont.render(txt, True, (185, 185, 185))
            choices_rects.append((pcenter + count, pcenter + count + 35))
            # print(pcenter + count)
            screen.blit(self.choice_bg, (0, pcenter + count + 2))
            screen.blit(txt, (75, pcenter + count))
            count += 50

        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    count = 1
                    for i in choices_rects:
                        if(i[0] <= pygame.mouse.get_pos()[1] <= i[1]):
                            return count
                        count += 1
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


class Personage:
    def __init__(self, name, color, cn, sprites, pose=None, pos_x=0, pos_y=0):
        self.name = name
        self.color = color
        self.sprites = dict()
        # print(sprites)
        for key, value in sprites.items():
            if(key != "none" or value != "none"):
                self.sprites[key] = pygame.image.load(value)
        self.code_name = cn
        self.pose = pose
        self.pos_x = pos_x
        self.pos_y = pos_y

if(__name__ == "__main__"):
    x = ScenarioCommands()
    x.init_music("data/music/quitemusic.mp3", "sample_muse_1")
    # print(x.musics)
    x.play_music("sample_muse_1")
    x.init_sound("data/sounds/dialog_click.mp3", "click_1")
    # print(x.sounds)
    x.play_sound("click_1")
    pygame.init()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
