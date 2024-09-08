import csv
from dracobot2.config import SessionLocal
from dracobot2.models import User, UserDetails

session = SessionLocal()

f = open("import.csv")
f_reader = csv.reader(f)

header = next(f_reader)


def get_row_info(cur_row):
    index = int(cur_row[0])
    name = cur_row[1]
    handle = cur_row[2]
    likes = cur_row[6]
    dislikes = cur_row[7]
    room_number = cur_row[8]
    requests = cur_row[9]
    level = int(cur_row[3][-1])
    dragon_no = int(cur_row[4])
    return {
        'index': index,
        'name': name,
        'handle': handle,
        'likes': likes,
        'dislikes': dislikes,
        'room_number': room_number,
        'requests': requests,
        'level': level,
        'dragon_no': dragon_no,
    }


users_list = {}
for row in f_reader:
    user_obj = get_row_info(row)
    user_db = User(id=user_obj['index'], tele_handle=user_obj['handle'])
    user_details_db = UserDetails(user=user_db,
                                  name=user_obj['name'],
                                  likes=user_obj['likes'],
                                  dislikes=user_obj['dislikes'],
                                  room_number=user_obj['room_number'],
                                  requests=user_obj['requests'],
                                  level=user_obj['level'])
    users_list[user_obj['index']] = (user_db, user_obj['dragon_no'])
    session.add(user_details_db)

session.commit()

for user_id in users_list:
    user_db, dragon_id = users_list[user_id]
    user_db.dragon = users_list[dragon_id][0]

session.commit()
