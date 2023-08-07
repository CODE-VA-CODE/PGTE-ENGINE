import pygame

from engine import ScenarioCommands, Personage


# sc_1 = ScenarioCommands()
def scen_1_data_init():
    global sc_1
    sc_1 = ScenarioCommands()

    bs_sprites = {"cl_eye_smile": "data/images/sprites/bs/cl_eye_smile_1.png",
                  "concern": "data/images/sprites/bs/concern_1.png",
                  "norm": "data/images/sprites/bs/norm_1.png",
                  "one_eye_cl_smile": "data/images/sprites/bs/one_eye_cl_smile_1.png",
                  "shout": "data/images/sprites/bs/shout_1.png",
                  "sigh": "data/images/sprites/bs/sigh_1.png",
                  "sm_smile": "data/images/sprites/bs/sm_smile_1.png",
                  "unkindly": "data/images/sprites/bs/unkindly_1.png"}
    sc_1.pers_init("Ceo", (215, 215, 215), "bs", bs_sprites)
    sc_1.pers_init("Ceo", (215, 215, 215), "bs1", bs_sprites)
    sc_1.init_music("data/music/quitemusic.mp3", "sample_music")
    sc_1.init_bg("data/images/bg/office_day.png", "office_1")
    sc_1.pers_init("I", (215, 215, 215), "i", {"none": "none"})
    sc_1.pers_init("", (213, 213, 213), "na", {"none": "none"})  # рассказчик/просто описание происходящего

def scenario_1():
    sc_1.tell("bs", "Hi, this is an example script")
    sc_1.show("bs", "one_eye_cl_smile", 450, 250)
    sc_1.tell("bs", "Just to show the capabilities of the engine")
    sc_1.show("bs", "cl_eye_smile", 450, 250)
    sc_1.tell("bs", "And for that, let's move to a nicer place")
    sc_1.bg_img("office_1")
    sc_1.show("bs", "one_eye_cl_smile", 450, 250)
    sc_1.tell("bs", "Fine, let's turn on the music")
    sc_1.play_music("sample_music")
    sc_1.tell("bs", "...")
    sc_1.tell("bs", "And now I'll show you cloning")
    sc_1.show("bs1", "one_eye_cl_smile", 600, 250)
    sc_1.tell("bs", "...")
    sc_1.tell("bs", "Disappear")
    sc_1.hide("bs1")
    sc_1.tell("bs", "Right now, I control everything here")
