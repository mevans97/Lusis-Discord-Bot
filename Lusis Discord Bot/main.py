import discord #discord.py package
import random #random package


class MyClient(discord.Client): # The entire script of what the bot does goes in this class
    async def on_ready(self):
        print(f' {self.user} On !')

    async def on_message(self, message):
        yes =str.lower("yes")
        no = "no"
        
        yes_responses = [
        'Of Fucking course!',
        'No way! she was gunna ask you!',
        'Yes! she would love to date someone from this planet. she has never done that before.',
        'SMASH',
        'Everyone she has ever dated mysteriously died, but she could try again for you!',
        'Definitely not no',
        'She is interested, as long as she get to live.',
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
        'Of course she would love too! SIKE',
        'Ew no',
        'Sorry, you have small dick energy',
        'The answer would probably be yes, but No'
        ]

        if message.content.startswith(yes):
            admin = "theRATking#5670"
            message_username = message.author.name + "#" + message.author.discriminator
            if message_username == admin:
                await message.channel.send(random.choice(yes_responses))
            else:
                await message.channel.send("You are not " + admin)

        if message.content.startswith(no):
            admin = "theRATking#5670"
            message_username = message.author.name + "#" + message.author.discriminator
            if message_username == admin:
                await message.channel.send(random.choice(no_responses))
            else:
                await message.channel.send("You are not " + admin)


client = MyClient()
client.run('MTAwMDEyNjg2NjUzNzA1ODMwNA.GI--FN.magwWqvJztBZ96vAMxGD0o2clRHo3vCt5mWpss')