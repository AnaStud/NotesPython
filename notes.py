import json
import os
import datetime

notes_file = "notes.json"

def add_note(title, message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(get_notes()) + 1,
        "title": title,
        "message": message,
        "datetime": current_time
    }
    notes = get_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def get_notes():
    if not os.path.exists(notes_file):
        return []
    with open(notes_file, "r") as file:
        notes = json.load(file)
    return notes

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)

def list_notes():
    notes = get_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Message: {note['message']}")
        print(f"Created at: {note['datetime']}\n")

def delete_note(note_id):
    notes = get_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print(f"Заметка с ID {note_id} удалена")

def main():
    print("Доступные команды: add, list, delete")
    command = input("Введите команду: ")

    if command == "add":
        title = input("Введите заголовок заметки: ")
        message = input("Введите текст заметки: ")
        add_note(title, message)
    elif command == "list":
        list_notes()
    elif command == "delete":
        note_id = int(input("Введите ID заметки для удаления: "))
        delete_note(note_id)
    else:
        print("Некорректная команда")

if __name__ == "__main__":
    main()