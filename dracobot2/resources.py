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

CURRENT_MAINTAINERS = "Raihan and Wonje"
PAST_MAINTAINERS = ["Daniel Lau", "Ji Cheng", "Shao Yi", "Bai Chuan", "Fiz, Youkuan", "Kang Ming", "Zhi Yu"]
TECHNICAL_ASSISTANCE = "@raihahan or @jeonwonje"
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
    "anonymous gifts " + GIFT_EMOJI + " and pranks " + DEVIL_EMOJI + " according to their indicated tolerance levels! " +\
    "Of course, you can look forward to seeing what your own trainer does for you as well! " + WINK_EMOJI + GRIN_EMOJI + SPARKLE_EMOJI + "\n\n" +\
    "<u>Explanation for tolerance levels</u>\n\n" +\
    "1: Gift Exchange, do nice things only!\n" +\
    "2: Pranks are to be minimal, and no / minimal clean up required!\n" +\
    "3: Pranks are fine, but do take care of what your dragon says is <b>OFF LIMITS</b>\n\n" +\
    "<u>Dos</u> " + SMILE_EMOJI + "\n" +\
    "• Observe the Tolerance Levels your dragons have indicated.\n" +\
    f"• Gain consent from your dragon before entering their rooms. (You can ask using the @{BOT_NAME} via the chat function)\n" +\
    "• Do take note of your dragon’s dislikes and OFF LIMITS details and adhere to them (Try to <b>avoid</b> doing anything your dragon dislikes, especially anything they have declared OFF LIMITS)\n" +\
    "• <b>Balance out the pranks with gifts - moderation is key!</b>\n" +\
    "• Try (your best) to <b>keep your identity hidden</b>.\n" +\
    "• Be active in the event! :)\n" +\
    "• " + SPARKLE_EMOJI + "<b>Share your pranks and gifts throughout the event in the Draco group chat!</b>" + SPARKLE_EMOJI + "\n\n" +\
    "<u>Don'ts</u> " + SAD_EMOJI + CROSS_EMOJI + "\n" +\
    "• Cause major damage (e.g. breaking a treasured object) even if they’ve indicated no boundaries.\n" +\
    "• Flout other RC / NUS rules (e.g. theft, possession of alcohol *ahem ahem*).\n" +\
    "• Cause major inconveniences, especially along the common corridor" +\
    "(e.g. blockade the walkway, pranks involving powdered substances like flour or curry powder).\n" +\
    "• Cause fire hazards and hinder evacuation routes.\n" +\
    "• Write, draw or scribble any obscene/vulgar contents on doors / common area.\n" +\
    "• Commit pranks that may put <b>YOURSELF</b> or <b>OTHERS AT RISK</b> " + SWORD_EMOJI + KNIFE_EMOJI + FIRE_EMOJI + " (e.g. placing personal objects at dangerous locations, using flammables)\n\n" +\
    "<b>**IMPORTANT!**</b>\n\n" +\
    "NO LIVE ANIMALS OR INSECTS\n" +\
    "NO MOVING OF FURNITURE OUT OF THE ROOMS and AVOID MOVING of furniture\n" +\
    "And RESTRICT pranks to <b>YOUR OWN DRAGON</b> (avoid performing pranks on others’ dragons as any incidents that arise due to your unannounced pranks would implicate other trainers)\n\n" +\
    "Do adhere to the rules as stated above, as well as the basic housing regulations of RC4.\n\n" +\
    f"If you have any other questions, concerns or doubts, don’t be afraid to reach out to {REACH_OUT_TO}! We hope you have fun and make new friends as well!\n\n" +\
    "Love,\n" +\
    "Draco House Comm" + BLUE_HEART_EMOJI
WELCOME_MESSAGE = "Dear {name},\n\n\n"\
    "You woke up dizzy in the highest floors of a building known as AreSeaFore and you are unsure of how you were transported here. Next to you lies a piece of paper which reads:\n\n\n"\
    "\"Esteemed Trainer, you are tasked to train dragon ‘{dragon_name}’ for the next 2 and a half weeks. Slowly approach the dragon at unit {dragon_room_number} to tame it and teach it new skills.\n\n"\
    "Your dragon likes ‘{dragon_likes}’ but it really dislikes ‘{dragon_dislikes}‘.\n\n"\
    "‘{dragon_requests}' is stated as off limits. Take careful note of these as you venture on your quest to tame your dragon, for there may be consequences.\n\nThe difficulty of training is LEVEL {dragon_level:d}.\n\n\n"\
    f"We, {REACH_OUT_TO}, will watch over all of you trainers throughout the training. Do contact us should you need assistance in taming your dragon.\n\n\n"\
    "Set forth young one and be the best dragon tamer of AreSeaFore Draco.\"\n\n\n"\
    "*Game of Thrones Music Intensifies*"
STATUS = "Trainer Status: {trainer_status}\n"\
    "Dragon Status: {dragon_status}\n"
DRAGON_DETAILS = "Dragon Details " + DRAGON_EMOJI + "\n\n"\
    "Name: {name}\n"\
    "Unit: {room_number}\n"\
    "Level: {level:d}\n\n"\
    "Likes:\n{likes}\n\n"\
    "Dislikes:\n{dislikes}\n\n"\
    "Off Limits:\n{requests}\n\n"
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
