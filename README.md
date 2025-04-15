# timer-with-note
# ⏳ Personal Timer App

A minimalist command-line timer to help you stay productive, focused, and organized. It includes classic countdown timers, Pomodoro cycles, limitless focus mode, and auto-logging of your work sessions with notes.

> Built in Python. Plays alarm sounds. Saves your work logs. 100% offline. Fully open source.

---

## 🧠 Features

- ⏱ **Countdown Timer**: Set custom time and get notified when it ends
- ♾️ **Limitless Timer**: A timer that runs until you stop it
- 🍅 **Pomodoro Mode**: Work in cycles with break intervals
- 📓 **Work Log**: Save notes about what you worked on and when
- 🔊 **Sound Alarm**: Plays an alarm sound at the end of each timer
- 💾 **Persistent Storage**: Logs are stored in JSON and reload automatically

---

## 📦 Requirements

- Python 3.7+
- [pygame](https://www.pygame.org/)
- For alarm you need to add a "alarm.mp3" file to your directory. I uploaded an example one.
- Json file will be automaticly generated.
- In delete notes function, if you want to delete multiple notes you can just type :1 2 3 4. 

Install dependencies:

```bash
pip install pygame

