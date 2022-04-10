import uiautomator2 as u2
from ppadb.client import Client
import time
from datetime import datetime
import logging
import os
import re
import traceback
from collections import OrderedDict
from tappersogp.enemies import enemies_list
from tappersogp.shouts import shouts_list
import pyperclip



command_count = 1


setting = ''

# We are using an OrderedDict so that specific enemy types, such as "Ancient Dragon" are tested before general
# enemy types, such as "Dragon".
enemies = OrderedDict({'Arch Necromancer': 'Shout', 'Adoring Fan': 'Weapon', 'Ancient Dragon': 'Shout',
           'Death Hound': 'Weapon', 'Dragon Priest': 'Weapon',
           'Dremora Markynaz': 'Shout', 'Dremora Valkynaz': 'Shout',
           'Elder Dragon': 'Shout', 'Forsworn Ravager': 'Weapon',
           'Forsworn Warlord': 'Weapon', 'Frost Dragon': 'Shout',
           'Frost Troll': 'Weapon', 'Frostbite Spider': 'Weapon', 'Ghost': 'Shout', 'Giant Mudcrab': 'Weapon',
           'Ice Wolf': 'Weapon',
           'Large Mudcrab': 'Weapon',
           'Master Necromancer': 'Shout', 'Renegade Storm Cloak': 'Weapon', 'Sabre Cat': 'Weapon',
           'Bear': 'Weapon', 'Chaurus': 'Weapon', 'Conjurer': 'Shout', 'Cryomancer': 'Shout',
           'Dragon': 'Shout', 'Draugr': 'Shout',
           'Dremora': 'Shout', 'Electromancer': 'Shout', 'Falmer': 'Shout', 'Forsworn': 'Weapon', 'Giant': 'Shout',
           'Mage': 'Shout', 'Mudcrab': 'Weapon', 'Pyromancer': 'Shout', 'Thalmor': 'Shout', 'Troll': 'Weapon',
           'Vampire': 'Shout', 'Werewolf': 'Weapon', 'Wolf': 'Weapon'})
paths = ['Black Iron Gate', 'Broken Open Gate', 'Cobwebbed Passageway', 'Crumbling Staircase',
         'Decoratively Carved Door', 'Definitley Not Booby Trapped Hallway', 'Dimly-Lit Hallway',
         'Foul Smelling Hallway', 'Half-Collapsed Archway', 'Heavy Wooden Door', 'Hidden Staircase',
         'Metal Banded Door', 'Musty Passageway', 'Peaked Archway', 'Portcullis Gate',
         'Sagging Wooden Archway', 'Scarred Iron Door', 'Secret Passageway', 'Simple Wooden Gate',
         'Spiral Staircase', 'Stone Archway', 'Stone Staircase', 'Suspiciously Ordinary Door',
         'Tall Ancient Archway', 'Tapestry-Lined Hallway', 'Torchlit Passageway', 'Unlocked Gate',
         'Well-Worn Passageway', 'Winding Hallway', 'Wooden Staircase', 'shady grove', 'blossoming grove',
         'flooded evergreen grove',
         'trail', 'bridge', 'door', 'gate', 'hill', 'scramble', 'ridge', 'mineshaft', 'tunnel', 'footpath',
         'plateau', 'ladder', 'corridor',
         'ancestral grove', 'foggy deadwood grove',
         'glade', 'path']

locations = ['Abandoned Tower', 'Ancient Standing Stone', 'Bustling Tavern', 'Busy Trading Post',
             'Daedric Shrine', 'Dusty Old Wood Mill', 'Fishing Camp', 'Foggy Dock', 'Fortified Town',
             'Isolated Shack', 'Nordh Village', 'Quaint Farm', 'Small Hamlet', 'Spooky Lighthouse']

objectives = ['will you avenge', 'will you lend', 'will you help']
confirmations = ['face the peril ahead', 'charge into danger', 'wish to proceed',
                 'forward on your quest', 'venture in']


class SkyrimVSEPlayer():
    def __init__(self, outfile='tappers.txt'):
        self.outfile = outfile
        self.serial = 'emulator-5554'
        self.host = '127.0.0.1'
        self.port = 5037
        self.d = u2.connect('emulator-5554')

        outfile_exists = True
        if not os.path.exists(self.outfile):
            outfile_exists = False

    def _reboot_phone(self):
        print("REBOOTING")
        logging.error("REBOOTING")
        adb = Client(host=self.host, port=self.port)
        adb_device = adb.device(self.serial)
        adb_device.reboot()
        time.sleep(240.0)

    def _setup_files(self):
        if os.path.exists(self.outfile):
            with open(self.outfile, "r", encoding="utf-8") as f2:
                for line in f2:
                    line_chunks = re.split("\t", line)
        else:
            self.my_outfile.write("Timestamp\tSetting\tRequest\tShout\tSpell\tWeapon\tResponse\n")
            self.my_outfile.flush()
        return True

    def start(self):
        print("STARTING")
        self._setup_files()

        hierarchy = self.d.dump_hierarchy()
        pyperclip.copy(hierarchy)
        print(hierarchy)



        self.my_outfile.close()

        end_time = datetime.now()
        print(end_time - self.start_time)
        print("Done")

        return True


if __name__ == '__main__':
    svsep = SkyrimVSEPlayer()
    ret_val = svsep.start()
    print(str(ret_val))
