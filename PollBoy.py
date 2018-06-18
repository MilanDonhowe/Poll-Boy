#!/usr/bin/python3.5
# PollBoy - Simple text-based yes or no polls in Discord.


import discord
import asyncio

# Global variables

pollRunning = False;
pollYes = 0
pollNo = 0
voted = []
client = discord.Client()
realPoll = None
pollTitle = ''

async def update_poll(realPoll, pollTitle, pollNo, pollYes):
    await client.edit_message(realPoll, """
                ```css
                [POLL] %s
                [YES : %s ]  [NO : %s ]
                To vote yes type $y, to vote no type $n.
                ```""" % (str(pollTitle), str(pollYes), str(pollNo)))


@client.event
async def on_ready():
    print("User: " + client.user.name + client.user.id)
    await client.change_presence(game=discord.Game(name='Solitaire | $help'))

@client.event
async def on_message(message):
    global pollRunning, pollNo, pollYes, realPoll, pollTitle, voted
    
    if message.content.startswith("$help"):
        helpInfo = """I see {0.author.mention} requested help.  Here are my commands:
        '$help' - Lists this screen.
        '$poll' - Starts a in-chat poll.  Format: ```$poll [name of poll here]``` By default a poll lasts 40 seconds.""".format(message)
        await client.send_message(message.channel, helpInfo)
        
    if message.content.startswith("$poll"):
        if (pollRunning == False):
            voted = []
            pollRunning = True
            pollTitle = message.content[5:]
            pollYes = 0
            pollNo = 0
            realPoll = await client.send_message(message.channel, """
            ```css
            [POLL] %s
            [YES : %s ]  [NO : %s ]
            To vote yes type $y, to vote no type $n.
            ```
            """ % (str(pollTitle), str(pollYes), str(pollNo)))       
            await asyncio.sleep(40.0)
            pollRunning = False;
            if (pollYes > pollNo):
                await client.send_message(message.channel, "The majority (%s %s) responded 'yes' to the poll titled: %s." % (str((pollYes/(pollYes + pollNo))*100), "%" , str(pollTitle)))
            elif (pollYes < pollNo):
                await client.send_message(message.channel, "The majority (%s %s) responded 'no' to the poll titled: %s." % (str((pollNo/(pollYes + pollNo))*100), "%" , str(pollTitle)))
            else:
                await client.send_message(message.channel, "The poll, " + str(pollTitle) + ", ended in a tie.")
            
        else:
            await client.send_message(message.channel, "{0.author.mention} please wait until the current Poll is finished to start a new one.".format(message))

    if (message.content.startswith("$n") or message.content.startswith("$N")):
        if (pollRunning == True):
            author ="{0.author.mention}".format(message)
            if not author in voted:
                voted.append(author)
                print(voted)
                pollNo += 1
                await update_poll(realPoll, pollTitle, pollNo, pollYes)
            else:
                await client.send_message(message.channel, "{0.author.mention} You've already voted.".format(message))
            
    if (message.content.startswith("$y") or message.content.startswith("$Y")):
        if (pollRunning == True):
            author ="{0.author.mention}".format(message)
            if not author in voted:
                voted.append(author)
                print(voted)
                pollYes += 1
                await update_poll(realPoll, pollTitle, pollNo, pollYes)
            else:
                await client.send_message(message.channel, "{0.author.mention} You've already voted.".format(message))
            
            
        
client.run(token) # replace "token" with your own bot token.
