from userge import userge, Message

@userge.on_cmd("mdl", about="get movie from mdl")
async def first_command(message: Message) -> None:
    """ this thing will be used as command doc string """

    await message.edit("first cmd executed")
