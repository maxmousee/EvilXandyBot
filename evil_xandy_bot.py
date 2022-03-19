from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater("YOUR_TOKEN_HERE", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Olá, cidadão. Tô de olho nas mensagens, viu? Não vá espalhar fake news aqui")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Quer ajuda? Pede pra alguém do governo!""")


def fake(update: Update, context: CallbackContext):
    update.message.reply_text("""Tô de olho nas mensagens, viu? Não vá espalhar fake news aqui!""")


def mentira(update: Update, context: CallbackContext):
    update.message.reply_text("""Isso é fake news! Vou dar ordem de prisão para todos envolvidos nessa conversa!""")


def verdade(update: Update, context: CallbackContext):
    update.message.reply_text("""Isso é verdade! Já verifiquei com os fact checkers aqui!""")


def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Não sei como fazer isso, vou te processar!")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Isso é fake news, vou mandar a multa pode fazer o PIX")


updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('fake', fake))
updater.dispatcher.add_handler(CommandHandler('verdade', verdade))
updater.dispatcher.add_handler(CommandHandler('mentira', mentira))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_command))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown_command))  # Unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()