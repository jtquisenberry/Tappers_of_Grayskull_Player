# Tappers of Grayskull Player

## Introduction

He-Man Tappers of Grayskull is a tapper game for Android and iOS. Completing higher stages requires fortifying characters with artifact upgrades using keys, one of two in-game currencies. 

This Tappers of Grayskull Player application is designed to accumulate keys with minimal human interaction. 

I built the Player after tournaments were discontinued. Thus, cheating at multiplayer has not been possible.

## Strategy

It is assumed that the user has already advanced far enough in the game to upgrade the artifact that provides a gold bonus when time-travelling. The user should have upgraded the artifact that increases the number of keys obtained after time travel. 

The Player plays typically 155-159 stages, upgrades characters, and time travels. With autosave enabled, the game saves progress. The process takes about 23 minutes. With a 200% bonus to time travel keys, I obtain a bit more than 1,000 keys per time travel or 2,600 keys per hour.

Once the user can reach level 2,700, gathering keys is no longer the most efficient way to pass stages. Even pouring hundreds of thousands of keys into artifacts does little to increase the power of characters and enable them to progress to the next stage. At that point, repeated use of the Sacrifice skill, followed by the cooldown reduction skill is recommended. That can be accomplished with the ClickMate macro recorder on Android.

### Table of Formal Names

|                                                | He-Man           | She-Ra                        |
|------------------------------------------------|------------------|-------------------------------|
| Sacrifice Skill                                | Sacrifice        | Sacrifice                     |
| Cooldown Skill                                 | Meditation       | Contemplation                 |
| Artifact granting extra keys from time travel  | Sunstone         | Queen Angella's Crystal Crown |
| Artifact granting extra gold after time travel | Secret Treasure  | Glittering Bangle             |
| Store option to reduce enemies per stage       | Cowardly Enemies | Cowardly Enemies              |

## Technical

The application relies on UIAutomator2, a Python package that wraps ADB (Android Debug Bridge) interfaces. See https://github.com/openatx/uiautomator2#image-match.

The Tappers of Grayskull game is buggy. Using my finger to tap buttons does not always activate them. Consequently, the behavior of the Player may vary from what is expected. Submitting commands through ADB adds to the challenge. Two swipes with the same parameters may scroll the list of characters by different amounts. The Player takes into account the imprecise nature of both the game and UIAutomator2 inputs. The longest uninterrupted run I observed was greater than 24 hours but less than 36 hours. Checking on the game every few hours is wise.

I commented out code that reloads the saved game when a character is injured before time travel becomes available. I once observed that autosave was disabled after a reload. I believe this to be a rare behavior of the game. Until re-enabling autosave, time travel did not save further progress. If you are comfortable with the risk, the most time-efficient strategy is to uncommented the code. 

I have used UIAutomator on both a physical Samsung Galaxy A71 phone and an emulated Pixel 4 phone. I have run the Player only with the emulated device.    

## Notes about the Game

* The final dimensional artifact can be obtained at stage 3001 on the She-Ra side of the game.
* Online functionality, such as tournaments, were discontinued around July 1, 2019.
* The latest version of the game is 3.3.1.
* The highest stage is 3,500. Several players at the top of the leaderboard have reached this stage. There are a few players with higher maximum stage. It is unclear whether it was possible to reach a higher stage in an early version of the game or the entries in the leaderboard are illegitimate. 
