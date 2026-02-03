# Accept an integer amount from the user and tell the minimum number of notes needed:
def min_notes(amount):
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    note_count = {}

    for note in notes:
        if amount >= note:
            note_count[note] = amount // note
            amount = amount % note

            return note_count
        amount = 1783
        note_count = min_notes(amount)
        print(f"Notes needed for {amount}:")
        for note, count in note_count.items():
            print(f"{note} : {count}")
