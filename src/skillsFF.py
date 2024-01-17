import json
import os
import sys
import csv
import time
import pandas as pd


prodat = pd.read_json("src/output.json")

def foragingLVL():
    with open("src/skillsDAT/Foraginglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_foraging"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 51:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 50"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def miningLVL():
    with open("src/skillsDAT/Mininglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_mining"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 61:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 60"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def farmingLVL():
    with open("src/skillsDAT/Farminglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_farming"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 61:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 60"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def combatLVL():
    with open("src/skillsDAT/Combatlvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_combat"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 61:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 60"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def fishingLVL():
    with open("src/skillsDAT/Fishinglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_fishing"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 51:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 50"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def enchantingLVL():
    with open("src/skillsDAT/Enchantinglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_enchanting"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 61:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 60"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def alchemyLVL():
    with open("src/skillsDAT/Alchemylvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_alchemy"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 51:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 50"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def carpentryLVL():
    with open("src/skillsDAT/Carpentrylvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_carpentry"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 51:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 50"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def runecraftingLVL():
    with open("src/skillsDAT/Runecraftinglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_runecrafting"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 26:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 25"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def socialLVL():
    with open("src/skillsDAT/Sociallvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_social2"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 26:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 25"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }

def tamingLVL():
    with open("src/skillsDAT/Taminglvlreq.json") as file:
        exp_values = json.load(file)
        player_exp = prodat["profile"]["members"]["6c7cd35c6fe14e82b142f1299a3bb759"]["experience_skill_taming"]
        found_level = "Level 0"
        percent_to_next = 0
        exp_to_next = 0
        overflow_exp_v = False
        overflow_exp = 0
        x = 0

        last_iterated_level = ""
        for level, value in exp_values.items():
            if value > player_exp:
                found_level = last_iterated_level
                break;
            last_iterated_level = level
            x = x + 1
        if x == 61:
            overflow_exp_v = True
            overflow_exp = exp_values["Level 60"] - player_exp
            return {
            'level': found_level,
            'xp_current': player_exp,
            'xp_for_next': "0",
            'progress': "100%",
            'overflow_exp': overflow_exp
            }
        else:
            next_level = exp_values[f"Level {x}"]
            next_level_amount = (exp_values[f"Level {x}"] - exp_values[f"Level {x-1}"])
            next_level_player = (player_exp - exp_values[f"Level {x-1}"])
            percent_to_next = (next_level_player/next_level_amount)*100
            amount_to_next = next_level-player_exp
            # print(exp_values[f"Level {x}"])
            # print(percent_to_next)
            # print(next_level_amount)
            # print(next_level_player)
            # print(amount_to_next)
            return {
                'level': found_level,
                'xp_current': next_level_player,
                'xp_for_next': next_level_amount,
                'progress': percent_to_next
            }