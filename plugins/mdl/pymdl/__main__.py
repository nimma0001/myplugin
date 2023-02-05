from userge import userge, Message

@userge.on_cmd("test", about="my first command")
async def first_command(message: Message) -> None:
    """ this thing will be used as command doc string """

    test.Dynamic.TIMEOUT = 90

    await call_api()

    await message.edit("first cmd executed")
