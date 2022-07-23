import discord
import random


class MyClient(discord.Client): # The entire script of what the bot does goes in this class
    async def on_ready(self):
        print(f' {self.user} On !')

    async def on_message(self, message):
        yes ="yes"
        no = "no"
        
        yes_responses = [
        'Of Fucking course!',
        'No way! I was gunna ask you!',
        'Yes! I would love to date someone from this planet. Ive never done that before.',
        'SMASH',
        'Everyone Ive ever dated mysteriously died, but I could try again for you!',
        'Definitely not no',
        'Im interested, as long as I get to live.',
        'Thought youd never ask',
        'Sounds good, shell have her people call your people.',
        'Lucky you its a yes ! '
        ]

        no_responses = [
        'Youre cute, but not her type',
        'The LADY said NO!',
        'Dont even try. ',
        'Sorry not interested…',
        'Sorry shes actually moving to countries',
        'She rather drop dead',
        'Pass.',
        'Of course I would love too! SIKE',
        'Ew no',
        'Sorry, you have small dick energy',
        'The answer would probably be yes, but No'
        ]

        if message.content.startswith(yes):
            await message.channel.send(random.choice(yes_responses))

        if message.content.startswith(no):
            await message.channel.send(random.choice(no_responses))

client = MyClient()
client.run('MTAwMDEyNjg2NjUzNzA1ODMwNA.GS6ZW8.yKEHwRRmswMrnIAk85wZdB0WFAyIZ40oWuGbH4')