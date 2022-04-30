#https://github.com/openatx/uiautomator2#image-match
import uiautomator2 as u2
from ppadb.client import Client
import time
from datetime import datetime
import logging
import os
import re
import traceback
import pyperclip
import cv2
import sys


class TappersOGPlayer():
    def __init__(self, outfile='tappers.txt'):
        self.outfile = outfile
        self.serial = 'emulator-5554'
        self.host = '127.0.0.1'
        self.port = 5037
        self.d = u2.connect('emulator-5554')

        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                            level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                            handlers=[
                                logging.FileHandler("tappers.log"),
                                logging.StreamHandler(sys.stdout)])

        self.start_time = datetime.now()
        self.image = None

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
            self.my_outfile.write("\n")
            self.my_outfile.flush()
        return True

    def _click_skill(self):
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
        for i in range(12):
            self.d.swipe(600, 1600, 600, 1900, .1)
            time.sleep(.2)

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
        date_time_string = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.image = self.d.screenshot()  # default format="pillow"
        self.image.save(r"D:\Projects\tappers\screen_{}.png".format(date_time_string))

    def _do_move(self):
        # Square
        self.d.touch.down(400, 700).sleep(1).move(400, 1000).sleep(.1).move(800, 1000).sleep(.1).move(800, 700).sleep(
            .1).move(400, 700).sleep(.1).up(400, 700)

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
        start_breakpoint = 0

        while True:
            logging.info("START")
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
            logging.info("Click Boss 1")

            self._click_skill()
            time.sleep(1)
            self._click_master()
            time.sleep(1)
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
                logging.info("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Reload Game")
                self._reload_game()
                time.sleep(1)
                continue

            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            time.sleep(3)

            logging.info("Scroll to Second Set - Gwildor, Stratos, Clamp Champ")
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                time.sleep(1)
                self._click_skill()
                time.sleep(1)
                self._click_master()
                time.sleep(1)
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2)
                pixel = self.d.screenshot(format="opencv")
                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                logging.info("Reload Game - Character Status")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game - Injury")
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
                logging.info("Reload Game - Character Status")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game - Injury")
                self._reload_game()
                time.sleep(1)
                continue

            time.sleep(3)

            logging.info("Scroll to Third Set: MossMan, Sy-Klone, Zodac")
            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            time.sleep(3)
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                    not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                time.sleep(1)
                self._click_master()
                time.sleep(1)
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

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                logging.info("Reload Game - Character Status")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game - Injury")
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
                logging.info("Reload Game - Character Status")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game - Injury")
                self._reload_game()
                time.sleep(1)
                continue

            start_tap_time = datetime.now()
            time.sleep(1)

            # Click Fight Boss
            logging.info("Click Boss 2")
            self.d.click(920, 230)

            logging.info("Tap Attack 1 (360 seconds)")
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 360:
                    break

            time.sleep(1)
            logging.info("Click Zodac")
            self._click_master_3()
            logging.info("Sleep 60 seconds")
            time.sleep(60)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                logging.info("Reload Game - Character Status")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game - Injury")
                self._reload_game()
                time.sleep(1)
                continue

            logging.info("Click Boss 2")
            self.d.click(920, 230)

            self._write_screenshot()
            start_tap_time = datetime.now()
            logging.info("Tap Attack 2 (120 seconds)")
            time.sleep(1)
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 120:
                    break


            time.sleep(1)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                logging.info("Reload Game - Character Status")
                self._reload_game()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                print("Reload Game - Injury")
                self._reload_game()
                time.sleep(1)
                continue

            logging.info("Scroll to Fourth Set: Rio Blast, Mekaneck, He-Man")
            self.d.swipe(600, 1900, 600, 1440, duration=.25)
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                    not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                time.sleep(1)
                self._click_master()
                time.sleep(1)
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                self.d.swipe(600, 1900, 600, 1440, duration=.25)
                time.sleep(2.5)
                pixel = self.d.screenshot(format="opencv")

                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]

            logging.info("Click Rio Blast")
            time.sleep(3)
            self._click_master_1()
            time.sleep(1)
            self._click_master_1()
            time.sleep(1)

            if self._check_for_character_status():
                time.sleep(1)
                self.d.click(930, 430)
                time.sleep(1)
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            logging.info("Click Boss")
            self.d.click(920, 230)

            logging.info("Tap Attack 3")
            time.sleep(1)
            start_tap_time = datetime.now()
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 120:
                    break

            time.sleep(1)
            logging.info("Click Mekaneck")
            self._click_master_2()
            time.sleep(1)
            self._click_master_2()
            time.sleep(1)

            logging.info("Click Boss")
            self.d.click(920, 230)

            start_tap_time = datetime.now()
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 210:
                    break

            if self._check_for_character_status():
                time.sleep(1)
                self.d.click(930, 430)
                time.sleep(1)
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            time.sleep(2)
            logging.info("Click He-Man")
            self._click_master_3()
            time.sleep(30)
            self._click_master_3()
            time.sleep(1)

            logging.info("Click Boss")
            self.d.click(920, 230)

            logging.info("Tap Attack 4 (110 seconds)")
            start_tap_time = datetime.now()
            while True:
                self.d.swipe(500, 500, 500, 1200, .05)
                time.sleep(.05)
                total_seconds = (datetime.now() - start_tap_time).total_seconds()
                if total_seconds > 110:
                    break

            time.sleep(1)

            if self._check_for_character_status():
                time.sleep(1)
                self.d.click(930, 430)
                time.sleep(1)
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            logging.info("Upgrade Rio Blast, Mekaneck, He-Man")
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)

            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)

            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)

            if self._check_for_character_status():
                time.sleep(1)
                self.d.click(930, 430)
                time.sleep(1)
                #logging.info("Character Status Time Travel")
                #print("Character Status Time Travel")
                #self._time_travel()
                #time.sleep(1)
                #continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Injury Time Travel")
                #print("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue


            logging.info("Upgrade Teela")
            #print("Upgrade Teela")
            time.sleep(1)
            self._scroll_to_top()
            time.sleep(2)

            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)
            self._upgrade_master_1()
            time.sleep(2)
            self._click_master_1()
            time.sleep(2)

            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._click_master_2()
            time.sleep(2)
            self._upgrade_master_2()
            time.sleep(2)
            self._click_master_2()
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
            self._click_master_3()
            time.sleep(2)
            self._upgrade_master_3()
            time.sleep(2)
            self._click_master_3()
            time.sleep(2)

            if self._check_for_character_status():
                self.d.click(930, 430)
                time.sleep(1)
                logging.info("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            logging.info("Fourth Set")
            self.d.swipe(600, 1900, 600, 1455, duration=.25)
            pixel = self.d.screenshot(format="opencv")
            r = pixel[1680, 850][2]
            g = pixel[1680, 850][1]
            b = pixel[1680, 850][0]

            while not (r in range(5, 15) and g in range(95, 110) and b in range(165, 185)) and \
                    not (r in range(225, 255) and g in range(225, 255) and b in range(225, 255)):
                self._click_skill()
                time.sleep(1)
                self._click_master()
                time.sleep(1)
                self._scroll_to_top()
                time.sleep(2)
                self.d.swipe(600, 1900, 600, 1455, duration=.25)
                time.sleep(2.5)
                pixel = self.d.screenshot(format="opencv")
                r = pixel[1680, 850][2]
                g = pixel[1680, 850][1]
                b = pixel[1680, 850][0]

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
                logging.info("Character Status Time Travel")
                self._time_travel()
                time.sleep(1)
                continue
            if self._check_for_injury():
                self.d.click(930, 730)
                time.sleep(1)
                logging.info("Injury Time Travel")
                self._time_travel()
                time.sleep(1)
                continue

            logging.info("Back to the Past")

            self._click_skill()
            time.sleep(1)
            self.d.click(700, 2100)
            time.sleep(1)
            self.d.click(550, 1100)
            time.sleep(7)

            end_breakpoint = 1

    def start(self):
        self._run_round_01()
        return True


if __name__ == '__main__':
    svsep = TappersOGPlayer()
    ret_val = svsep.start()
    print(str(ret_val))
