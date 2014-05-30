======
Django Simple FAQ
======

FAQ is Django app for managing Frequently Asked Questions. 
FAQ provides two models: Category and Question.
Question objects contain question and answer text fields and a display order
field to control sorting. 

Category objects allow questions to be organized into groups.

APP_SETTINGS:
- SIMPLE_FAQ_PAGINATE_BY - number of questions to paginate by (set to None to
  disable pagination)
