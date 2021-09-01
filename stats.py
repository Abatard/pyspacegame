dictionary = {
    #player
    "player": {
        "ship": "small_bio_ship",
        "health": 10,
        "credits": 0
    },

    #ships
    "small_bio_ship": {
        "typ": "small_bio_ship",
        "width": 100,
        "height": 100,
        "health": 3,
        "speed": 7,
        "animation_cycle_counter": 0,
        "animation_cycle_max": 20,
        "animation_sprite_number_counter": 0,
        "guns": [{"typ":"simple_gun","x_offset": 0,"y_offset": -1},],
        "exploding": False,
        "exploding_duration": 200,
        "exploding_modulus": 30,  #alle x ticks explosionen
        "explosion_amount": 3
    },
    "small_robot_ship": {
        "typ": "small_robot_ship",
        "width": 50,
        "height": 100,
        "health": 2,
        "speed": 1,
        "animation_cycle_counter": 0,
        "animation_cycle_max": 20,
        "animation_sprite_number_counter": 0,
        "guns": [{"typ":"simple_gun","x_offset": 0,"y_offset": -0.9},
                {"typ":"simple_gun","x_offset": 0,"y_offset": 0.9}],
        "exploding": False,
        "exploding_duration": 200,
        "exploding_modulus": 30,  #alle x ticks explosionen
        "explosion_amount": 3
    },

    #weapons
    "simple_gun": {
        "typ": "simple_gun",
        "width": 45,
        "height": 45,
        "speed":0,
        "x_offset_for_bullet_90": 50,
        "y_offset_for_bullet_90": 50,
        "x_offset_for_bullet_270": 50,
        "y_offset_for_bullet_270": 50,
        "bullet_typ": "simple_bullet",
        "health": 1,
        "heat_max": 10000,
        "heat": 0,
        "heat_emission": 0,
        "reload": 60,
        "magazin_max": 50,
        "magazin_counter": 0,
        "ticks_per_shot": 20,
        "ticks_per_shot_counter": 0,
        "exploding": False,
        "exploding_duration": 200,
        "exploding_modulus": 30,
        "explosion_amount": 1,
        "animation_cycle_counter": 0,
        "animation_cycle_max": 20,
        "animation_sprite_number_counter": 0
    },

    #bullets
    "simple_bullet": {
        "typ": "simple_bullet",
        "width": 16,
        "height": 16,
        "speed": 8,
        "damage": 1,
        "exploding": False,
        "exploding_duration": 59,
        "exploding_modulus": 1,
        "explosion_amount": 1,
        "animation_cycle_counter": 0,
        "animation_cycle_max": 20,
        "animation_sprite_number_counter": 0
    },

    #explosions
    "simple_explosion": {
        "typ": "simple_explosion",
        "width": 80,
        "height": 80,
        "animation_cycle_counter": 0,
        "animation_cycle_max": 10,
        "animation_sprite_number_counter": 0,
        "animation_lifetime_counter": 59
    }
}


def stats_get(sub_dictionary, request):
    return dictionary.get(sub_dictionary).get(request)
