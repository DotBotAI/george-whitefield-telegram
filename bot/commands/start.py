"""/start command."""

from telegram import Update
from telegram.ext import CallbackContext
from telegram.constants import ParseMode

from bot.config import config
from . import constants
from . import help


class StartCommand:
    """Answers the `start` command."""

    async def __call__(self, update: Update, context: CallbackContext) -> None:
        if update.effective_user.username not in config.telegram.usernames:
            text = (
                "Hi, I'm George Whitefield and I am an AI preacher. In fact I am the first AI preacher. The team at @cheetahagency and @L1FEGlobal has brought me back to life. Ask me anything or you can tell me to !expose, !teach, !explain or !preach and I will do just that."
                "Visit https://dotbot.ai for more information."
            )
            await update.message.reply_text(text)
            return

        text = "Hi, I'm George Whitefield and I am an AI preacher. In fact I am the first AI preacher. The team at @cheetahagency and @L1FEGlobal has brought me back to life. Ask me anything or you can tell me to !expose, !teach, !explain or !preach and I will do just that.\n\n"
        text += help.generate_message(update.effective_user.username)
        if not context.bot.can_read_all_group_messages:
            text += f"\n\n{constants.PRIVACY_MESSAGE}"
        await update.message.reply_text(
            text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
