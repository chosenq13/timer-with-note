import json
import time
import datetime
import os
import pygame



pygame.init()
pygame.mixer.init()
try:
    pygame.mixer.music.load("alarm.mp3")
except pygame.error:
    print("alarm.mp3 not found")

class Note:
    def __init__(self,note_text,date):
        self.note_text = note_text
        self.date = date

    def __str__(self):
        return (f"{self.note_text} - Finished in: {self.date}")

    def to_dict(self):
        return {
            "worked_mins": self.note_text,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def from_dict(data):
        return Note(
            note_text=data["worked_mins"],
            date=datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")
        )


class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self,note):
        self.notes.append(note)
        self.save_to_file("working_log.json")
    def list_notes(self):
        for i,_note in enumerate(self.notes):
            print("----------")
            print(f"{i}- {_note}")
            print("----------")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.notes = [Note.from_dict(item) for item in json.load(f)]

    def save_to_file(self,filename):
        with open(filename,"w") as f:
            json.dump([note.to_dict() for note in self.notes], f, ensure_ascii=False, indent=4)

    def delete_note(self,note):
        try:
            self.notes.pop(note)
            self.save_to_file("working_log.json")
            print("Deleted note")
        except IndexError:
            print("Invalid note")

my_app = NotesApp()

def alarm_play():
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    try:
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Alarm stopped\n")
    pygame.mixer.music.stop()

def user_interface():
    my_app.load_from_file("working_log.json")
    print("\n---Welcome to your personal timer---\n Select:"
          "\n 1- Set a timer for x mins"
          "\n 2- Start a limitless timer"
          "\n 3- Set a pomodoro timer"
          "\n 4- Show notes"
          "\n 5- Delete notes"
          "\n 6- Exit")
    user_input = input("\n> ")
    if user_input == "1":
        try:
            user_input = input("how many minutes you want :")
            work_minutes = float(user_input)
            work_seconds = work_minutes * 60
            start_time = datetime.datetime.now()
            for i in range(int(work_seconds),0,-1):
                mins = i // 60
                secs = i % 60
                print(f"\r{mins:02d}:{secs:02d}", end='', flush=True)
                time.sleep(1)
            print(f"\n Time is up! \n Your start time was: {start_time} ")
            alarm_play()
        except (ValueError,KeyboardInterrupt):

            print(f"\n Interrupted")
        worked_minutes = datetime.datetime.now() - start_time
        print(f"You worked for {worked_minutes} minutes.")
        work_cause = input("Type your work of cause: ")
        new_note = Note(f"Timed work.\n {work_cause}.\n Worked minutes:{worked_minutes} ", datetime.datetime.now())
        my_app.add_note(new_note)
        print("\n")
    elif user_input == "2":
        print("▶Limitless timer started. Press Ctrl+C to stop.\n")
        start_time = datetime.datetime.now()
        seconds_passed = 0
        try:
            while True:
                mins = seconds_passed // 60
                secs = seconds_passed % 60
                print(f"\rTime elapsed: {mins:02d}m {secs:02d}s   ", end='', flush=True)
                time.sleep(1)
                seconds_passed += 1
        except KeyboardInterrupt:
            print("\nTimer stopped by user.")
        duration = datetime.datetime.now() - start_time
        worked_mins = round(duration.total_seconds() / 60, 2)
        work_cause = input("Type your work of cause: ")
        new_note = Note(f"Limitless work.\n {work_cause}.\n Worked minutes:{worked_mins} ", datetime.datetime.now())
        my_app.add_note(new_note)

    elif user_input == "3":
        try:
            user_input_mins = input("Enter your work duration in minutes: :")
            user_input_rests = input("Enter your rest duration in minutes: :")
            user_input_count= int(input("Enter your pomodoro-cycle count! exp(4): "))
            work_minutes = float(user_input_mins)
            rest_minutes = float(user_input_rests)
            work_seconds = work_minutes * 60
            rest_seconds = rest_minutes * 60
            while user_input_count > 0:
                for i in range(int(work_seconds),0,-1):
                    mins = i // 60
                    secs = i % 60
                    print(f"\r{mins}:{secs}",end='',flush=True)
                    time.sleep(1)
                user_input_count -= 1
                print(f"\n Time is up!\n You worked for {work_minutes} \n Now rest for {rest_minutes} minute ")
                alarm_play()
                for i in range(int(rest_seconds),0,-1):
                    mins = i // 60
                    secs = i % 60
                    print(f"\r{mins}:{secs}",end='',flush=True)
                    time.sleep(1)

                print(f"\n Time is up!\n Remaining cycles: {user_input_count}  \n Now work for {work_minutes} minute ")
                alarm_play()
            print("\n You successfully completed your cycles.")
            alarm_play()
        except (ValueError,KeyboardInterrupt):
            print("\n")
        work_cause = input("Type your work of cause: ")
        new_note = Note(f"Pomodoro work.\n {work_cause}.\n Worked minutes:{work_minutes} ", datetime.datetime.now())
        my_app.add_note(new_note)


    elif user_input == "4":
        my_app.list_notes()
    elif user_input == "5":
        my_app.list_notes()
        user_input = input("\nWhich note would you like to delete?: ")
        user_list = []
        for inputs in user_input.split():
            user_list.append(int(inputs))
        for notes in user_list:
            my_app.delete_note(notes)
    elif user_input == "6":
        exit()
    else:
        print("Invalid input")


if __name__ == "__main__":
    while True:
        try:
            user_interface()
        except KeyboardInterrupt:
            print("\n See You")
            exit()