import json


def add_to_db(name, number, helper=False):
    """
    Adds a new entry to the database.
    """
    with open("db/db.json", "r") as f:
        db = json.load(f)

    if not helper:
        for entry in db["guests"]:
            if entry["number"] == number:
                return False
    if helper:
        db["helpers"].append({"name": name, "number": number+"helf"})
    else:
        db["guests"].append({"name": name, "number": number})
    with open("db/db.json", "w") as f:
        json.dump(db, f)
    f.close()
    return True


def does_exist(number):
    """
    Checks if a ticket with the given number and name exists.
    """
    with open("db/db.json", "r") as f:
        db = json.load(f)

    # if the string ends with "helf", set helper to true
    helper = False
    if number.endswith("helf"):
        helper = True

    if not helper:
        for entry in db["guests"]:
            if entry["number"] == number:
                db["guests"].remove(entry)
                save_db(db)
                f.close()
                return True
    if helper:
        for entry in db["helpers"]:
            if entry["number"] == number:
                db["helpers"].remove(entry)
                save_db(db)
                f.close()
                return True
    f.close()
    return False


def save_db(db):
    """
    Saves the database to a file.
    """
    with open("db/db.json", "w") as f:
        json.dump(db, f)
    f.close()
