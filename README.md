# BetterQuesting-L10nKeyGen

Tool that generates a copy of `DefaultQuests.json` with all desc replaced by localization keys, and then creates the lang file.


# Environment Requirement

Your computer should have Python 3.x installed.

(This script is developed and tested under Python 3.11)


# How to Use:

1. Put the script `main.py`, and your modpack's `DefaultQuests.json`, in whatever folder you like.
2. Run `main.py` in your favorite way. For myself, I right-click in the folder's window, choose "Open Terminal Here" then execute:
    ```batch
   python -m main.py
   ```
3. Wait the two files to be output:
   1. `xx_xx.lang`: It contains all the Descriptions (value of all "desc:8" keys) and Names (value of all "name:8" keys). They are re-arranged into this form:
      ```text
      #Descs
   
      keys.betterquesting.desc.000000.name=
      keys.betterquesting.desc.000001.name=
      keys.betterquesting.desc.000002.name=
      ...
      
      #Names
   
      keys.betterquesting.name.000000.name=
      keys.betterquesting.name.000001.name=
      keys.betterquesting.name.000002.name=
      ...
      ``` 
      
      Then you may load this language file by any way you like, such as resource packs, OpenLoader or ResourceLoader mod, or `resource` folder in the config folder of BetterQuesting itself.
      
      It should be loaded, and work correctly, as I have tested.

      After that you may do the translation yourself or wait pull requests from other translators.
   2. `output_quest_json.json`: It will be your new `DefaultQuests.json`. It's **HIGHLY recommended** to back up your original `DefaultQuests.json` before you do the replacement!

# Credits

Some codes are from GitHub repo [qc5111/BetterQuestingAutoTranslate](https://github.com/qc5111/BetterQuestingAutoTranslate) which is licensed under MIT License.

Thanks to the original author.
