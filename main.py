import pygame

from sc_scripts.example_sc_script import scenario_1, scen_1_data_init


def run():
    scen_1_data_init()
    scenario_1()
    pygame.display.flip()


if(__name__ == "__main__"):
    run()
