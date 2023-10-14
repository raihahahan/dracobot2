import os
from dotenv import load_dotenv
load_dotenv()

env = os.environ["ENV"]
BOT_NAME = os.environ["TELEGRAM_BOT_NAME_DEV"] if env == "DEV" else os.environ["TELEGRAM_BOT_NAME_PROD"]

# EMOJI UNICODE
CAKE_EMOJI = u"\U0001F382"
ROBOT_EMOJI = u"\U0001F916"
SKULL_EMOJI = u"\U0001F480"
SMILEY_EMOJI = u"\U0001F642"
HELP_EMOJI = u"\U0001F64F"
MONKEY_EMOJI = u"\U0001F64A"
DRAGON_EMOJI = u"\U0001F432"  # In use for Dragon Trainer Bot
TRAINER_EMOJI = u"\U0001F3CB"
BLUE_HEART_EMOJI = u"\U0001F499"
GREEN_STATUS_EMOJI = u"\U0001F7E2"
RED_STATUS_EMOJI = u"\U0001F534"
CROSS_EMOJI = u"\U0000274C"
GIFT_EMOJI = u"\U0001F381"
DEVIL_EMOJI = u"\U0001F608"
WINK_EMOJI = u"\U0001F609"
GRIN_EMOJI = u"\U0001F601"
SMILE_EMOJI = u"\U0001F642"
SAD_EMOJI = u"\U00002639"
SPARKLE_EMOJI = u"\U00002728"
SWORD_EMOJI = u"\U0001F5E1"
KNIFE_EMOJI = u"\U0001F52A"
FIRE_EMOJI = u"\U0001F525"


WHALE_EMOJI = u"\U0001F40B"
SPOUTING_WHALE_EMOJI = u"\U0001F433"
SPEECH_BUBBLE_EMOJI = u"\U0001F4AC"
THINKING_FACE_EMOJI = u"\U0001F914"

# TELEGRAM KEYBOARD KEYS
ABOUT_THE_BOT_KEY = u"About the Bot" + " " + DRAGON_EMOJI
ADMIN_KEY = u"admin"
DRAGON_CHAT_KEY = u"Chat with Dragon" + " " + DRAGON_EMOJI
TRAINER_CHAT_KEY = u"Chat with Trainer" + " " + TRAINER_EMOJI
STATUS_KEY = u"Status" + " " + GREEN_STATUS_EMOJI
HELP_KEY = u"Help" + " " + HELP_EMOJI
RULES_KEY = u"Rules" + " " + MONKEY_EMOJI
MENU_KEY = u"menu"
TRAINER_KEY = u"trainer"
DRAGON_KEY = u"dragon"
START_KEY = u"start"
DELETE_KEY = u"delete"
CANCEL_KEY = u"cancel"
DONE_KEY = u"done"

def comma_separate(str_list: list):
    return ", ".join(str_list)

CURRENT_MAINTAINERS = "Raihan & Wonje"
PAST_MAINTAINERS = ["Ji Cheng", "Shao Yi", "Bai Chuan", "Fiz, Youkuan", "Kang Ming", "Zhi Yu", "Javier", "Raihan", "Wonje"]
TECHNICAL_ASSISTANCE = "@xavierchia"
REACH_OUT_TO = "@notbingsu, @yukuleles, @xavierchia, @vitchun"


# GREETINGS
ABOUT_THE_BOT = DRAGON_EMOJI + " *About DracoBot* " + DRAGON_EMOJI + "\n\n" + CAKE_EMOJI + " Birthday: June 2017\n\n" +\
    ROBOT_EMOJI + f" Currently maintained by {CURRENT_MAINTAINERS}\n\n" + SKULL_EMOJI +\
    f" Past Bot Developers: {comma_separate(PAST_MAINTAINERS)}\n\n"

ADMIN_GREETING = "Hello there, Administrator! What do you want to say to everyone?\n" +\
    "Whatever you submit from now on will be broadcasted to all users, be CAREFUL!\n" +\
    "Type /" + DONE_KEY + " to exit, once you have made your announcement."

HELLO_GREETING = "Hello there, {}! DracoBot at your service! Press /" + \
    MENU_KEY + " to bring up keyboard! " + DRAGON_EMOJI

HELP_MESSAGE = "Hello there, {}!\n\n" +\
    "<u>Main Menu</u>\n" +\
    DRAGON_CHAT_KEY + ": To chat with your Dragon \n" +\
    TRAINER_CHAT_KEY + ": To chat with your Trainer\n" +\
    HELP_KEY + ": To explore this bot's functionality\n" +\
    STATUS_KEY + ": To view status of Dragon and Trainer\n" +\
    RULES_KEY + ": To view the game rules\n" +\
    ABOUT_THE_BOT_KEY + ": To view information about the bot\n\n" +\
    "Type /" + DONE_KEY + " at any point in time to exit the chat\n" +\
    "Type /" + MENU_KEY + " to show the Main Menu\n\n" +\
    "<u>Features</u>\n" +\
    "1. <b>Reply message</b>: You can reply to a message to automatically chat with your dragon / trainer.\n" +\
    "2. <b>Delete message</b>: You can select a message and type /delete\n" +\
    "3. <b>Edit message</b>: You can edit your message to your dragon / trainer\n" +\
    "4. <b>Media files</b>: Supported files are <i>audio</i>, <i>document</i>, <i><b>photo</b></i>, <i><b>sticker</b></i>, <i>videos</i>, <i>video note</i> and <i>voice</i>\n\n" +\
    f"Please message {TECHNICAL_ASSISTANCE} if you need technical assistance!\n" +\
    "Thank you and we hope you'll have fun throughout this game! :)"

GAME_RULES_MESSAGE = "Rules of Dragon and Trainer " + DRAGON_EMOJI + "\n\n" +\
    "Each of you who participated will be assigned a Trainer and a Dragon. " +\
    "Of course, you will know the identity of your Dragon while your Trainer’s identity will be kept " +\
    "from you. Throughout the course of the event, feel free to chat with both your Dragon and Trainer " +\
    "through this telegram bot where your identity will be kept secret, and take care of your dragon with " +\
    "anonymous gifts " + GIFT_EMOJI + " and pranks " + DEVIL_EMOJI + " according to their indicated commitment levels! " +\
    "Of course, you can look forward to seeing what your own trainer does for you as well! " + WINK_EMOJI + GRIN_EMOJI + SPARKLE_EMOJI + "\n\n" +\
    "<u>Explanation for commitment levels</u>\n\n" +\
    "Level 1: No pranks, No entering participant’s rooms, Light gift giving\n" +\
    "Level 2: Light pranks, Entering participants room upon strict consent with restrictions, Gift Giving proportionate to Prank\n" +\
    "Level 3: Highest Level of Tolerance, Room Entering is allowed (subject to personal preference), Gift Giving proportionate to Prank\n\n" +\
    "Throughout the course of the event, ensure your actions are within the Housing Services Code of Conduct and Rules. Participants will be held accountable for any damages caused and will face the appropriate disciplinary action. As part of our efforts to create a safe but fun environment for everyone, please read the following rules beforehand:\n\n" +\
    f"1) <b>DO NOT ENTER</b> your dragon’s room <b>UNTIL CONSENT IS Given</b> {GREEN_STATUS_EMOJI}\nPlease note the consent details, and clarify with your dragon if you are ever in doubt.\n\n" +\
    f"2) <b>TAKE NOTE OF FOOD ALLERGIES</b> {CAKE_EMOJI}. Please check with your dragon on his/her allergies before giving any food/gifts. Please tell your trainer your allergies if you have any.\n\n" +\
    f"3) <b>ADHERE</b> to what your dragon dislikes. Please avoid doing anything your dragon dislikes, especially the things they have declared <b>OFF Limits</b> {CROSS_EMOJI}\n\n" +\
    f"4) <b>RESTRICT</b> surprises to your <b>OWN DRAGON</b>. Avoid performing surprises onto other people apart from your dragon as any incidents that happen due to your unannounced surprises could implicate other trainers.\n\n" +\
    f"5) <b>ADHERE TO THE INDICATED</b> Commitment Level {SPARKLE_EMOJI}. Do not do anything outside the indicated commitment level. If you and your dragon are at level 1, please restrict to gift giving only. The same is true for level 2 and 3.\n\n" +\
    f"6) <b>BALANCE</b> out the surprises with gifts - <b>MODERATION IS KEY</b>!\n\n" +\
    f"7) <b>AVOID REMOVAL or MOVING OF ITEMS/FURNITURE</b> {SKULL_EMOJI}. Any missing items reported from your dragon's room could implicate you. DAMAGED furniture could subject you to disciplinary action. <b>FURNITURE IS NOT TO BE MOVED OUT OF ROOMS and DO NOT REMOVE ANY DOORS</b>.\n\n" +\
    f"8) NO ANIMALS OR INSECTS {WHALE_EMOJI} (Dead or alive). Housing Services does not tolerate the use of live animals or insects as it contravenes housing regulations and could put other residents at risk of Injury. <b>FAILURE TO COMPLY COULD RESULT IN DEMERIT POINTS</b>.\n\n" +\
    "9) <b>DO NOT</b> commit surprises that <b>MAY PUT YOURSELF OR OTHERS AT RISK</b>. This includes but is not restricted to:\n" +\
    "> Placing personal objects at dangerous locations\n" +\
    "> Entering toilets of the opposite gender\n" +\
    "> Using flammables/creating an open flame\n" +\
    "> Entering rooms using the windows\n" +\
    "> Placing heavy objects in high places\n" +\
    "> Blocking fire exits and common corridors\n\n" +\
    "10) Non-Exhaustive List of Banned surprises:\n" +\
    "> Powder-related surprises\n" +\
    "> Surprises that extend past Draco floors\n" +\
    "> Spoilage of food or surprises relating to smell\n" +\
    "> Surprises involving different gendered toilets \n\n" +\
    f"If you have any other questions, concerns or doubts, don’t be afraid to reach out to {REACH_OUT_TO}!\n\n We hope you have fun and make new friends as well!\n\n" +\
    "Love,\n" +\
    "Dragon & Trainer Organising Committee" + BLUE_HEART_EMOJI + DRAGON_EMOJI

WELCOME_MESSAGE = "Dear {name},\n\n\n"\
    "Welcome to the Land Above All, where our spirits intertwine and legends come to life. You have been sent on a mission atop RC4, tasked with training your dragon companion, ‘{dragon_name}‘. Over the next two weeks, forge a bond, tame the wild, and explore the depths of companionship. Embrace this extraordinary journey and uncover the hidden potentials within both you and your dragon.\n\n\n"\
    "You slowly approach your Dragon's lair at {dragon_room_number}. At the entrance of the lair is a signage which reads: \n\n"\
    "{dragon_name} is a Commitment Level {dragon_level:d} dragon.\n"\
    "{dragon_name}'s likes include \"{dragon_likes}\".\n"\
    "{dragon_name}'s dislikes and no-gos include \"{dragon_dislikes}\".\n"\
    "{dragon_name}'s consent details: {dragon_requests}\n\n"\
    "Take careful note of these as you venture on your quest to tame your dragon, for there may be consequences.\n\n"\
    f"We, {REACH_OUT_TO}, will watch over all of you trainers throughout the training. Do contact us should you need assistance in taming your dragon.\n\n\n"\
    "Set forth young one and be the best dragon tamer in the Land Above All.\n\n\n"

STATUS = "Trainer Status: {trainer_status}\n"\
    "Dragon Status: {dragon_status}\n"

DRAGON_DETAILS = "Dragon Details " + DRAGON_EMOJI + "\n\n"\
    "Name: {name}\n"\
    "Unit: {room_number}\n"\
    "Commitment Level: {level:d}\n\n"\
    "Likes:\n{likes}\n\n"\
    "Dislikes:\n{dislikes}\n\n"\
    "Consent Details:\n{requests}\n\n"

TRAINER_DETAILS = "Trainer Details " + TRAINER_EMOJI + SPARKLE_EMOJI + "\n\n"\
    "Name: {name}\n"\
    "Unit: {room_number}\n"
CHAT_COMPLETE = "You have finish chatting with your {}."
CONNECTION_SUCCESS = "You have been connected with your {}." +\
    " Anything you type here will be sent anonymously to him/her.\n" +\
    "To exit, type /" + DONE_KEY
DELETE_MESSAGE_SUCCESS = "Message deleted."
USER_REPLY_SHORTCUT = "This message has been sent. You are currently connected with your {}. Send /" + DONE_KEY + " when you are done."
USER_REPLY_CHANGE_MODE = "You are currently connected with your {}. Send /" + DONE_KEY + " when you are done."

# Error Messages
USER_UNREGISTERED = "You have not been registered. Press /start once you have registered."
USER_NO_TELE_HANDLE = "Please register with your telegram handle."
USER_NO_TRAINER = "You have no trainer. Please ask the admin to assign a trainer to you."
USER_UNREGISTERED_TRAINER = "Your trainer has not register. Please try again later."
USER_NO_DRAGON = "You have no dragon. Please ask the admin to assign a dragon to you."
USER_UNREGISTERED_DRAGON = "Your dragon has not register. Please try again later."
UNSUPPORTED_MEDIA = "Media not supported."
CONNECTION_ERROR = "Connection error. Please be patient and try again soon!" + SMILEY_EMOJI
CANNOT_DELETE_ERROR = "Cannot delete message."
DELETE_MESSAGE_ERROR = "Message has been deleted."
DELETE_MESSAGE_REPLY_ERROR = "Please reply a message to delete."
UNKNOWN_COMMAND = "Unknown command. Press /" + \
    MENU_KEY + " to bring up keyboard."
UNKNOWN_CHAT_COMMAND = "You are still chatting with your {}. Press /" + \
    DONE_KEY + " if you are done chatting."
TIMEOUT_MESSAGE = "You have been inactive for more than {}. You will be disconnected from the chat."
