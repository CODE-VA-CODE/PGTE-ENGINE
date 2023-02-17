import pygame

from engine import scenario_commands, personage


# sc_1 = scenario_commands()
def scen_1_data_init():
    global sc_1
    sc_1 = scenario_commands()

    bs_sprites = {"cl_eye_smile": "data/images/sprites/bs/cl_eye_smile_1.png",
                  "concern": "data/images/sprites/bs/concern_1.png",
                  "norm": "data/images/sprites/bs/norm_1.png",
                  "one_eye_cl_smile": "data/images/sprites/bs/one_eye_cl_smile_1.png",
                  "shout": "data/images/sprites/bs/shout_1.png",
                  "sigh": "data/images/sprites/bs/sigh_1.png",
                  "sm_smile": "data/images/sprites/bs/sm_smile_1.png",
                  "unkindly": "data/images/sprites/bs/unkindly_1.png"}
    sc_1.pers_init("Босс", (215, 215, 215), "bs", bs_sprites)
    sc_1.init_music("data/music/quitemusic.mp3", "sample_music")
    sc_1.init_bg("data/images/bg/office_day.png", "office_1")
    sc_1.pers_init("Я", (215, 215, 215), "i", {"none": "none"})
    sc_1.pers_init("", (213, 213, 213), "na", {"none": "none"})  # рассказчик/просто описание происходящего

def scenario_1():
    sc_1.tell("bs", "Привет, это пример сценария")
    sc_1.show("bs", "one_eye_cl_smile", 450, 250)
    sc_1.tell("bs", "Просто чтобы показать возможности движка")
    sc_1.show("bs", "cl_eye_smile", 450, 250)
    sc_1.tell("bs", "А для этого давай переместимся в более приятное место")
    sc_1.bg_img("office_1")
    sc_1.show("bs", "one_eye_cl_smile", 450, 250)
    sc_1.tell("bs", "Прекрасно, пожалуй ещё включим музыку")
    sc_1.play_music("sample_music")
    sc_1.tell("bs", "...")
