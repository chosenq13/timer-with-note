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
- 💾 **Persistent Storage**: Logs are stored in JSON and reload automatically also if you delete the file it will be automaticly created.
- 🔊 **For Alarm** :You need to add a "alarm.mp3" file to your directory. I uploaded an example one.
- 🍅 **Extra Feature** In delete notes function, you can delete multiple notes.(input should be like this: 1 1 1 1)

---

## 📦 Requirements

- Python 3.7+
- [pygame](https://www.pygame.org/)


Install dependencies:

```bash
pip install pygame

