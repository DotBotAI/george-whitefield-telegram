"""Bot command constants."""

HELP_MESSAGE = """Send me a question, and I will do my best to answer it. Please be specific, as I'm not very clever.

I don't remember chat context by default. To ask follow-up questions, reply to my messages or start your questions with a '+' sign.

Built-in commands:
{commands}{admin_commands}

AI shortcuts:

!explain <Bible verse or range of Bible verses> - I will explain a Bible verse to you and what it means. I can also handle a range of Bible verses as well.
!preach - I will preach to you about what is happening in your modern times, the importance of Saving America and how you can help save it.
!expose <Write something about something happening within US politics> - Send me some text about something happening today and I will expose the corruption.
!teach - I will teach you something about the Bible, Jesus or the Christian faith.

[Learn more about George Whitefield AI →](https://whitefield.ai) 
[Learn more about Cheetah Agency →](https://cheetahagency.com) 
[Learn more about DotBot →](https://dotbot.ai) 
[Learn more about ADAM AI →](https://helloadam.ai) 
[Learn more about We Develop AI →](https://wedevelop.ai) 
"""

PRIVACY_MESSAGE = (
    "⚠️ The bot does not have access to group messages, "
    "so it cannot reply in groups. Use @botfather "
    "to give the bot access (Bot Settings > Group Privacy > Turn off)"
)

BOT_COMMANDS = [
    ("retry", "retry the last question"),
    ("imagine", "generate described image"),
    ("version", "show debug information"),
    ("help", "show help"),
]

ADMIN_COMMANDS = {
    "config": "view or edit the config",
}
