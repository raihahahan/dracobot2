from dracobot2.utils import *
from dracobot2.resources import *
from dracobot2.models import User, Role
from dracobot2.config import SessionLocal
from sqlalchemy.orm import scoped_session
from sqlalchemy import or_
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, PicklePersistence)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext.dispatcher import run_async
import os
import logging
import time
import math
from dotenv import load_dotenv
from setup import createDatabase

from dracobot2.config import SQL_ENGINE
from dracobot2.models import *

load_dotenv()
createDatabase()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

UNREGISTERED, MAIN, CHAT, CHAT_LOGIN, DRAGON_CHAT, TRAINER_CHAT, ADMIN_CHAT = range(
    7)

KEYBOARD_OPTIONS = [[DRAGON_CHAT_KEY], [TRAINER_CHAT_KEY],
                    [HELP_KEY, STATUS_KEY], [RULES_KEY, ABOUT_THE_BOT_KEY]]
DEFAULT_REPLY_MARKUP = {'reply_markup': ReplyKeyboardMarkup(
    KEYBOARD_OPTIONS, one_time_keyboard=True)}
REMOVE_REPLY_MARKUP = {'reply_markup': ReplyKeyboardRemove()}

def get_filter_complete_match(match_string):
    return Filters.regex('^' + match_string + '$')

COMMAND_FILTER_REGEX = get_filter_complete_match(ABOUT_THE_BOT_KEY) | get_filter_complete_match(DRAGON_CHAT_KEY) | get_filter_complete_match(TRAINER_CHAT_KEY) | get_filter_complete_match(STATUS_KEY) | get_filter_complete_match(HELP_KEY) | get_filter_complete_match(RULES_KEY)

END = ConversationHandler.END
TIMEOUT = ConversationHandler.TIMEOUT

Session = scoped_session(SessionLocal)

CHAT_TIMEOUT_SECONDS = 2 * 60


def db_session(method):
    def db_session_decorator(update, context):
        session = Session()
        return_value = method(update, context, session)
        session.close()
        return return_value
    return db_session_decorator


@db_session
def start(update, context, session):
    chat_id = update.message.chat_id
    user = update.message.from_user

    user_db = session.query(User).filter(
        or_(User.tele_handle == user.username, User.chat_id == chat_id)).first()

    if user_db is not None:
        is_new_user = not user_db.registered

        if user_db.chat_id != chat_id:
            user_db.chat_id = chat_id
        if not user_db.registered:
            user_db.registered = True

        user_db.tele_handle = user.username
        user_db.tele_name = user.first_name

        first_name = user.first_name
        if user_db.details:
            first_name = user_db.details.name

        if is_new_user:
            dragon = user_db.dragon
            if dragon and dragon.details and user_db.details:
                welcome_message = WELCOME_MESSAGE.format(**{
                    'name': user_db.details.name,
                    'dragon_name': dragon.details.name,
                    'dragon_room_number': dragon.details.room_number,
                    'dragon_likes': dragon.details.likes,
                    'dragon_dislikes': dragon.details.dislikes,
                    'dragon_requests': dragon.details.requests,
                    'dragon_level': dragon.details.level
                })
                messages = list(filter(lambda x: len(x) > 0, welcome_message.split('\n\n\n')))
                for message in messages:
                    update.message.reply_text(message)
                    time.sleep(math.ceil(len(message) / 40) + 1)

            else:
                update.message.reply_text(USER_NO_DRAGON)

        session.commit()

        update.message.reply_text(HELLO_GREETING.format(
            first_name), **DEFAULT_REPLY_MARKUP)

        return MAIN
    else:
        update.message.reply_text(USER_UNREGISTERED)

        if user.username is None:
            update.message.reply_text(USER_NO_TELE_HANDLE)

        return UNREGISTERED


def about(update, context):
    update.message.reply_text(ABOUT_THE_BOT, **DEFAULT_REPLY_MARKUP)

    return MAIN


@db_session
def helps(update, context, session):
    user = update.message.from_user
    chat_id = update.message.chat_id

    user_db = session.query(User).filter(User.chat_id == chat_id).first()

    first_name = user.first_name
    if user_db.details:
        first_name = user_db.details.name

    update.message.reply_text(HELP_MESSAGE.format(
        first_name), parse_mode=telegram.ParseMode.HTML, **DEFAULT_REPLY_MARKUP)

    return MAIN


def rules(update, context):
    update.message.reply_text(GAME_RULES_MESSAGE, parse_mode=telegram.ParseMode.HTML, **DEFAULT_REPLY_MARKUP)

    return MAIN


@db_session
def status(update, context, session):
    chat_id = update.message.chat_id
    cur_user = session.query(User).filter(User.chat_id == chat_id).first()

    trainer = session.query(User).filter(User.dragon_id == cur_user.id).first()
    dragon = session.query(User).filter(User.id == cur_user.dragon_id).first()

    dragon_details = None
    if dragon and dragon.details:
        dragon_details = {
            'name': dragon.details.name,
            'likes': dragon.details.likes,
            'dislikes': dragon.details.dislikes,
            'room_number': dragon.details.room_number,
            'requests': dragon.details.requests,
            'level': dragon.details.level
        }

    trainer_details = None
    if trainer and trainer.details:
        trainer_details = {
            'name': trainer.details.name,
            'room_number': trainer.details.room_number,
        }

    t_registered = format_registered_message(trainer)
    d_registered = format_registered_message(dragon)

    message = STATUS.format(**{
        'trainer_status': t_registered,
        'dragon_status': d_registered
    })

    # if trainer_details is not None:
    #     message += '\n' + TRAINER_DETAILS.format(**trainer_details)

    if dragon_details is not None:
        message += '\n' + DRAGON_DETAILS.format(**dragon_details)

    update.message.reply_text(message, **DEFAULT_REPLY_MARKUP)

    return MAIN


@db_session
def check_trainer(update, context, session):
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(
        User.chat_id == chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id == cur_user_id).first()

    if trainer is None:
        update.message.reply_text(USER_NO_TRAINER, **DEFAULT_REPLY_MARKUP)
        return END
    elif not trainer.registered:
        update.message.reply_text(
            USER_UNREGISTERED_TRAINER, **DEFAULT_REPLY_MARKUP)
        return END
    else:
        update.message.reply_text(
            CONNECTION_SUCCESS.format(TRAINER_KEY), **REMOVE_REPLY_MARKUP)
        return TRAINER_CHAT


@db_session
def check_dragon(update, context, session):
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(
        User.chat_id == chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id == dragon_id).first()

    if dragon is None:
        update.message.reply_text(USER_NO_DRAGON, **DEFAULT_REPLY_MARKUP)
        return END
    elif not dragon.registered:
        update.message.reply_text(
            USER_UNREGISTERED_DRAGON, **DEFAULT_REPLY_MARKUP)
        return END
    else:
        update.message.reply_text(
            CONNECTION_SUCCESS.format(DRAGON_KEY), **REMOVE_REPLY_MARKUP)
        return DRAGON_CHAT


@db_session
def check_admin(update, context, session):
    chat_id = update.message.chat_id
    user_db = session.query(User).filter(User.chat_id == chat_id).first()

    if user_db and user_db.is_admin:
        update.message.reply_text(ADMIN_GREETING, **REMOVE_REPLY_MARKUP)
        return ADMIN_CHAT

    update.message.reply_text(UNKNOWN_COMMAND)
    return END


def send_message_to_dragon(update, context, session):
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(
        User.chat_id == chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id == dragon_id).first()

    if dragon is not None:
        forward_message(update.message, dragon.chat_id,
                        context.bot, session, message_from=Role.TRAINER)
        return DRAGON_CHAT
    else:
        update.message.reply_text(CONNECTION_ERROR, **REMOVE_REPLY_MARKUP)
        return END


def send_message_to_trainer(update, context, session):
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(
        User.chat_id == chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id == cur_user_id).first()

    if trainer is not None:
        forward_message(update.message, trainer.chat_id,
                        context.bot, session, message_from=Role.DRAGON)
        return TRAINER_CHAT
    else:
        update.message.reply_text(CONNECTION_ERROR, **REMOVE_REPLY_MARKUP)
        return END


@db_session
def send_trainer(update, context, session):
    return send_message_to_trainer(update, context, session)


@db_session
def send_dragon(update, context, session):
    return send_message_to_dragon(update, context, session)


@db_session
def send_admin(update, context, session):
    chat_id = update.message.chat_id
    user_db = session.query(User).filter(User.chat_id == chat_id).first()

    if not user_db.is_admin:
        return END

    all_users = session.query(User).filter(User.registered == True).all()

    for to_send_user in all_users:
        if to_send_user.id != user_db.id:
            forward_message(update.message, to_send_user.chat_id,
                            context.bot, session, message_from=Role.ADMIN)

    return ADMIN_CHAT


def handle_reply_message(current_mode):
    @db_session
    def inner_reply_message(update, context, session):
        new_mode = check_reply_mapping(update.message, session)
        ret_value = END

        if new_mode == Role.TRAINER or (new_mode is None and current_mode == Role.TRAINER):
            ret_value = send_message_to_trainer(update, context, session)
        elif new_mode == Role.DRAGON or (new_mode is None and current_mode == Role.DRAGON):
            ret_value = send_message_to_dragon(update, context, session)

        if new_mode is not None:
            if current_mode is None:
                update.message.reply_text(USER_REPLY_SHORTCUT.format(
                    TRAINER_KEY if new_mode == Role.TRAINER else DRAGON_KEY), **REMOVE_REPLY_MARKUP),
            elif current_mode != new_mode:
                update.message.reply_text(USER_REPLY_CHANGE_MODE.format(
                    TRAINER_KEY if new_mode == Role.TRAINER else DRAGON_KEY), **REMOVE_REPLY_MARKUP)

        return ret_value
    return inner_reply_message


@db_session
def handle_edited_message(update, context, session):
    edit_message(update, context, session)


@db_session
def handle_delete_message(update, context, session):
    delete_message_reply(update.message, context.bot, session)


def unknown_message(update, context):
    update.message.reply_text(UNKNOWN_COMMAND)


def handle_unknown_message_chat(target):
    def unknown_message_chat(update, context):
        update.message.reply_text(UNKNOWN_CHAT_COMMAND.format(target))
    return unknown_message_chat


@db_session
def handle_delete_admin(update, context, session):
    if len(context.args) == 2:
        chat_id, message_id = context.args
        delete_message(update.message, message_id,
                       chat_id, None, context.bot, session)
    else:
        delete_message_reply(update.message, context.bot, session)
    return ADMIN_CHAT


def unsupported_media(update, context):
    update.message.reply_text(
        UNSUPPORTED_MEDIA, reply_to_message_id=update.message.message_id, **REMOVE_REPLY_MARKUP)


def handle_timeout_chat(update, context):
    timeout_message = ""
    if CHAT_TIMEOUT_SECONDS < 60:
        timeout_message = str(CHAT_TIMEOUT_SECONDS) + " second(s)"
    else:
        timeout_message = str(CHAT_TIMEOUT_SECONDS // 60) + " minutes(s)"

    update.message.reply_text(TIMEOUT_MESSAGE.format(timeout_message), **DEFAULT_REPLY_MARKUP)

    return END


def done_chat(target):
    def inner_done_chat(update, context):
        update.message.reply_text(
            CHAT_COMPLETE.format(target), **DEFAULT_REPLY_MARKUP)

        return END
    return inner_done_chat


def _error(update, context):
    logger.error(context)
    logger.error(context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    pp = PicklePersistence(filename='conversationbot')
    updater = Updater(TOKEN, persistence=pp, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    chat_handler = ConversationHandler(
        entry_points=[MessageHandler(get_filter_complete_match(DRAGON_CHAT_KEY), check_dragon),
                      CommandHandler(DRAGON_KEY, check_dragon),
                      MessageHandler(get_filter_complete_match(
                          TRAINER_CHAT_KEY), check_trainer),
                      CommandHandler(TRAINER_KEY, check_trainer),
                      MessageHandler(Filters.reply, handle_reply_message(None)), ],

        states={
            # Chat with dragon
            DRAGON_CHAT: [MessageHandler(Filters.update.edited_message,
                                         handle_edited_message),
                          CommandHandler(DONE_KEY, done_chat(DRAGON_KEY)),
                          CommandHandler(DELETE_KEY, handle_delete_message),
                          MessageHandler(
                              Filters.command | COMMAND_FILTER_REGEX, handle_unknown_message_chat(DRAGON_KEY)),
                          MessageHandler(
                              Filters.reply, handle_reply_message(Role.DRAGON)),
                          MessageHandler(
                              SUPPORTED_MESSAGE_FILTERS, send_dragon),
                          MessageHandler(UNSUPPORTED_MESSAGE_FILTERS, unsupported_media)],

            # Chat with trainer
            TRAINER_CHAT: [MessageHandler(Filters.update.edited_message,
                                          handle_edited_message),
                           CommandHandler(DONE_KEY, done_chat(TRAINER_KEY)),
                           CommandHandler(DELETE_KEY, handle_delete_message),
                           MessageHandler(
                               Filters.command | COMMAND_FILTER_REGEX, handle_unknown_message_chat(TRAINER_KEY)),
                           MessageHandler(
                               Filters.reply, handle_reply_message(Role.TRAINER)),
                           MessageHandler(
                               SUPPORTED_MESSAGE_FILTERS, send_trainer),
                           MessageHandler(UNSUPPORTED_MESSAGE_FILTERS, unsupported_media)],

            TIMEOUT: [MessageHandler(
                Filters.text | Filters.command, handle_timeout_chat)]
        },

        fallbacks=[],
        conversation_timeout=CHAT_TIMEOUT_SECONDS,
        map_to_parent={
            END: MAIN,
        },

        name="dt_conversation",
        persistent=True,
    )

    admin_handler = ConversationHandler(
        entry_points=[CommandHandler(ADMIN_KEY, check_admin)],

        states={
            ADMIN_CHAT: [MessageHandler(Filters.update.edited_message,
                                        handle_edited_message),
                         CommandHandler(DONE_KEY, done_chat(ADMIN_KEY)),
                         CommandHandler(DELETE_KEY, handle_delete_admin, run_async=True),
                         MessageHandler(
                             Filters.command | COMMAND_FILTER_REGEX, handle_unknown_message_chat(ADMIN_KEY)),
                         MessageHandler(SUPPORTED_MESSAGE_FILTERS, send_admin, run_async=True),
                         MessageHandler(UNSUPPORTED_MESSAGE_FILTERS, unsupported_media)],

            TIMEOUT: [MessageHandler(
                Filters.text | Filters.command, handle_timeout_chat)]
        },

        fallbacks=[],
        conversation_timeout=CHAT_TIMEOUT_SECONDS,
        map_to_parent={
            END: MAIN,
        },

        name="admin_conversation",
        persistent=True,
    )

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.update.edited_message, handle_edited_message),
                      MessageHandler(Filters.all, start, run_async=True), ],

        states={
            UNREGISTERED: [MessageHandler(Filters.all, start, run_async=True)],

            MAIN: [MessageHandler(Filters.update.edited_message, handle_edited_message),
                   chat_handler,
                   admin_handler,
                   CommandHandler(MENU_KEY, start),
                   CommandHandler(DELETE_KEY, handle_delete_message),
                   MessageHandler(get_filter_complete_match(ABOUT_THE_BOT_KEY), about),
                   MessageHandler(get_filter_complete_match(HELP_KEY), helps),
                   MessageHandler(get_filter_complete_match(RULES_KEY), rules),
                   MessageHandler(get_filter_complete_match(STATUS_KEY), status)],
        },

        fallbacks=[MessageHandler(Filters.all, unknown_message)],

        name="main_conversation",
        persistent=True,
    )

    dp.add_error_handler(_error, run_async=True)
    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info("Initialised....")
    logger.info("Starting main()...")
    main()
