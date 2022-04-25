#https://github.com/openatx/uiautomator2#image-match
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
import cv2

#command_count = 1
#setting = ''


class TappersOGPlayer():
    def __init__(self, outfile='tappers.txt'):
        self.outfile = outfile
        self.serial = 'emulator-5554'
        self.host = '127.0.0.1'
        self.port = 5037
        self.d = u2.connect('emulator-5554')

        self.start_time = datetime.now()

        self.image = None

        # outfile_exists = True
        # if not os.path.exists(self.outfile):
        #    outfile_exists = False

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

    def _click_skill(self):
        # (117, 1596)
        # (117, 1758)
        # (117, 1908)
        # (117, 2058)
        # (117, 2208)

        self.d.click(117, 1596)

    def _click_shera(self):
        self.d.click(117, 1758)

    def _click_master(self):
        self.d.click(117, 1908)

    def _click_artifact(self):
        self.d.click(117, 2058)

    def _click_store(self):
        self.d.click(117, 2208)

    def _scroll_to_top(self):
        for i in range(9):
            self.d.swipe(600, 1600, 600, 1900, .1)
            #self.d.swipe(600, 1455, 600, 1900, duration=.25)
            time.sleep(.05)

    def _scroll_to_bottom(self):
        for i in range(9):
            self.d.swipe(600, 1900, 600, 1600, .1)
            time.sleep(.05)

    def _click_master_1(self):
        self.d.click(950, 1680)

    def _click_master_2(self):
        self.d.click(950, 1920)

    def _click_master_3(self):
        self.d.click(950, 2150)

    def _click_boss(self):
        self.d.click(950, 220)

    def _upgrade_master_1(self):
        self.d.long_click(950, 1680, .5)
        time.sleep(.1)
        self.d.click(600, 1680)

    def _upgrade_master_2(self):
        self.d.long_click(950, 1920, .5)
        time.sleep(.1)
        self.d.click(600, 1900)

    def _upgrade_master_3(self):
        self.d.long_click(950, 2150, .5)
        time.sleep(.1)
        self.d.click(600, 2150)

    def _get_hierarchy(self):
        hierarchy = self.d.dump_hierarchy()
        pyperclip.copy(hierarchy)
        print(hierarchy)

    def _write_screenshot(self):
        #hierarchy = self.d.dump_hierarchy()
        #pyperclip.copy(hierarchy)
        #print(hierarchy)

        #date_time_string = self.start_time.strftime("%Y%m%d_%H%M%S")
        date_time_string = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.image = self.d.screenshot()  # default format="pillow"
        self.image.save(r"D:\Projects\tappers\screen_{}.png".format(date_time_string))

    def _do_move(self):
        self.d.touch.down(600, 1900)  # Simulate press down
        self.d.touch.sleep(seconds=.1)
        # time.sleep(.01)  # The delay between down and move, you control it yourself
        self.d.touch.move(0, 200)  # simulate movement
        self.d.touch.sleep(seconds=.1)
        self.d.touch.up(600, 1600)  # Simulate lift

        # self.d.touch.down(400, 700).sleep(1).move(400, 1000).sleep(1).move(800,1000).sleep(1).move(800, 700).sleep(1).move(400, 700).sleep(1).up(400, 700)

        # Square
        self.d.touch.down(400, 700).sleep(1).move(400, 1000).sleep(.1).move(800, 1000).sleep(.1).move(800, 700).sleep(
            .1).move(400, 700).sleep(.1).up(400, 700)

        # Swipe
        # self.d.touch.down(500, 1900).sleep(1).move(500, 1600).sleep(.1).up(500, 1600)

    def _check_for_character_status(self):
        pixel = self.d.screenshot(format="opencv")
        r = pixel[430, 930][2]
        g = pixel[430, 930][1]
        b = pixel[430, 930][0]

        if r in range(153, 173) and g in range(37, 57) and b in range(17, 37):
            return True
        else:
            return False

    def _check_for_injury(self):
        pixel = self.d.screenshot(format="opencv")
        r = pixel[730, 930][2]
        g = pixel[730, 930][1]
        b = pixel[730, 930][0]

        if r in range(153, 173) and g in range(37, 57) and b in range(17, 37):
            return True
        else:
            return False

    def _time_travel(self):
        time.sleep(1)
        self._click_skill()
        time.sleep(1)
        self.d.click(700, 2100)
        time.sleep(1)
        self.d.click(550, 1100)
        time.sleep(7)

    def _reload_game(self):
        time.sleep(1)
        self.d.click(165, 225)
        time.sleep(2)
        self.d.click(550, 1300)
        time.sleep(3)
        self.d.click(550, 1600)
        time.sleep(3)
        self.d.click(850, 1090)
        time.sleep(5)
        self.d.click(705, 1555)
        time.sleep(2)
        self._time_travel()


    def _run_round_01(self):

        # New swipe
        #self.d.swipe(600, 1900, 600, 1455, duration=.25)

        cows = 0

        while True:

            time.sleep(2)
            self.d.click(300, 1000)
            time.sleep(1.5)
            self.d.click(300, 1000)
            time.sleep(1.5)
            self.d.click(300, 1000)
            time.sleep(1.5)
            self.d.click(300, 1000)
            time.sleep(1.5)
            self.d.click(300, 1000)
            time.sleep(15)
            print("At first boss")



            self._click_skill()
            time.sleep(.5)
            self._click_master()
            time.sleep(.5)
            self._scroll_to_top()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._upgrade_master_1()
            time.sleep(1)
            self._click_master_2()
            self._upgrade_master_2()
            time.sleep(1)
            self._click_master_3()
            self._upgrade_master_3()
            time.sleep(1)

            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue


            # self.image.getpixel((950, 1680))
            # (9, 102, 170)

            # self.image.getpixel((933, 1674))
            # (231, 231, 231)

            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            #self.d.swipe(600, 1900, 600, 1600, .1)
            time.sleep(3)

            #self.image = self.d.screenshot()  # default format="pillow"
            #pixel = self.image.getpixel((850, 1680))


            print("Scroll to second set.")
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                self._click_master()
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2)
                pixel = self.d.screenshot(format="opencv")

                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]
                xxx = 1

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue




            self._click_master_1()
            time.sleep(1)
            self._upgrade_master_1()
            time.sleep(1)
            self._click_master_2()
            time.sleep(1)
            self._upgrade_master_2()
            time.sleep(1)
            self._click_master_3()
            time.sleep(1)
            self._upgrade_master_3()
            time.sleep(1)

            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)
            self._click_master_3()
            time.sleep(.5)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue

            time.sleep(3)
            print("Third set")
            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            time.sleep(3)
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                    not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                self._click_master()
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2)
                pixel = self.d.screenshot(format="opencv")

                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]
                xxx = 1

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue

            self._click_master_1()
            time.sleep(1)
            self._upgrade_master_1()
            time.sleep(1)
            self._click_master_2()

            time.sleep(1)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_1()
            time.sleep(.5)
            self._click_master_2()
            time.sleep(.5)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue


            start_tap_time = datetime.now()

            time.sleep(1)


            # Click Fight Boss
            self.d.click(920, 230)

            print("Swipe Attack 1")
            while True:
                # Squareish
                #self.d.touch.down(400, 700).sleep(1).move(400, 1000).sleep(.1).move(800, 1000).sleep(.1).move(800, 700).sleep(
                #    .1).sleep(.1).up(800, 700)
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 420:
                    break


            #self._write_screenshot()



            # SNAPSHOT

            print("Sleep 1")
            time.sleep(1)
            print("Activate Zodac")
            self._click_master_3()
            print("Sleep 60")
            time.sleep(60)

            if self._check_for_character_status():
                q = 1
            if self._check_for_injury():
                q = 1

            print("Click Boss")
            # Click Fight Boss
            self.d.click(920, 230)

            self._write_screenshot()
            start_tap_time = datetime.now()
            print("Tap Attack 2")
            time.sleep(1)
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 120:
                    break
            print("Activate Rio Blast")
            time.sleep(1)

            if self._check_for_character_status():
                q = 1
            if self._check_for_injury():
                q = 1

            print("Fourth set")
            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                    not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                self._click_master()
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                pixel = self.d.screenshot(format="opencv")

                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]
                xxx = 1
            time.sleep(3)
            self._click_master_1()

            if self._check_for_character_status():
                q = 1
            if self._check_for_injury():
                q = 1

            print("Click Boss")
            # Click Fight Boss
            self.d.click(920, 230)


            time.sleep(1)
            start_tap_time = datetime.now()
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 90:
                    break

            time.sleep(2)
            self._click_master_2()
            time.sleep(2)

            print("Click Mekaneck")
            self.d.click(920, 230)

            start_tap_time = datetime.now()
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 210:
                    break

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            time.sleep(2)
            self._click_master_3()
            time.sleep(2)

            print("Click He-man")
            self.d.click(920, 230)

            start_tap_time = datetime.now()
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 110:
                    break

            time.sleep(1)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            print("Upgrade Rio Blast, Mekaneck, He-Man")
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)

            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)

            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue


            print("Upgrade Teela")

            self._scroll_to_top()
            time.sleep(1)

            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)

            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)

            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(3)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            print("Fourth set")
            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                    not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                self._click_master()
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                pixel = self.d.screenshot(format="opencv")

                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]
                xxx = 1
            time.sleep(3)

            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)
            self._click_master_1()
            time.sleep(3)
            self._upgrade_master_1()
            time.sleep(3)


            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._click_master_2()
            time.sleep(3)
            self._upgrade_master_2()
            time.sleep(3)


            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(3)
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(2)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                print("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            print("Back to the past")

            self._click_skill()
            time.sleep(1)
            self.d.click(700, 2100)
            time.sleep(1)
            self.d.click(550, 1100)
            time.sleep(7)

            #self._run_round_01()


            a = 1


    def start(self):
        print("STARTING")
        #self._setup_files()

        self._run_round_01()





        a = 1

        #(117, 1596)
        #(117, 1758)
        #(117, 1908)
        #(117, 2058)
        #(117, 2208)

        #d(scrollable=True).scroll(steps=10)

        # self.d.swipe(900, 1900, 900, 1600, .5)
        self.d.drag(600, 1900, 600, 1600, .2)
        self.d.swipe(600, 1900, 600, 1600, .2)
        self.d.click(117, 1758)

        # self.my_outfile.close()
        end_time = datetime.now()
        print(end_time - self.start_time)
        print("Done")

        return True


if __name__ == '__main__':
    svsep = TappersOGPlayer()
    ret_val = svsep.start()
    print(str(ret_val))
