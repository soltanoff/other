# Yandex translate client

ABOUT
---------

Project build on MSVS 2012

.NET Framework 4.5.1

Simple client Yandex.Translator. This program allows you to communicate with an Internet 
service providing online software tools for automatic translation of words, phrases and 
sentences from one language to another.

The client is written in C# using an API Translator.

About API Translator - https://tech.yandex.ru/translate/

- Hotkeys:

      1) Ctrl+F1 - to perform the translation
 
      2)* Ctrl+F2 - to perform the translation of the text from the clipboard and places the result there

      3)* Ctrl+F3 - to change the direction of translation (Ru <-> Eng)

      (*) - may be executed when an inactive application window

VERSION HISTORY
---------

- ver 1.0

      1) Start to dev

- ver 1.1

      1) Added file (Open/save file dialog)

      2) Fix bugs with translate

      3) Added context strip menu on textBoxes

- ver 1.2

      1) Added new background

      2) Fix bugs with web exceptions

- ver 1.3

      1) Added "About" form

      2) Fixed output of special characters

      3) Add new background

- ver 1.4

      1) Fixed output of special and arithmetic characters

      2) Include globalKeyboardHook class

- ver 1.4.1

      1) Added double buffering for background picture

      2) Added HotKey hook (with WinAPI)

      3) Exclude globalKeyboardHook class

      4) Added #region's

- ver 1.4.2

      1) Added Hotkey info form

      2) Replace and remodel #region's

- ver 1.5

      1) Added checkbox to configure access to a global catching of keyboard shortcuts.

      2) Renamed some classes, namespaces and functions

      3) Fixed a bug associated with long handling Web exceptions

      4) Added or auto-detection of font sizes depending on the number of lines of text.
