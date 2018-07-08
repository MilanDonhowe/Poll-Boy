#!/usr/bin/python3.5
# PollBoy - Simple text-based yes or no polls in Discord.


import discord
import asyncio

# Get user token for .exe version

#print("To exit press ctrl+c")
#print("Welcome to Poll-Boy!")
#token = input("Please copy and paste your token here: ")

client = discord.Client()





# Global variables

channelsRunning = []
pollYes = 0
pollNo = 0
voted = {}
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
        
    # check channels - Used for testing purposes
    #currentChannels = []
    
    #if message.content.startswith("$debug"):
    #    for server in client.servers:
    #        for channel in server.channels:
    #            if(channel.type == discord.ChannelType.text):
    #                currentChannels.append(channel)
    #                print("Added one!")
    #    print(currentChannels)
    #    print(message.channel in currentChannels)
    
    if message.content.startswith("$poll"):
        if (message.channel not in channelsRunning):
            voted[message.channel] = []
            channelsRunning.append(message.channel)
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
            channelsRunning.remove(message.channel)
            if (pollYes > pollNo):
                await client.send_message(message.channel, "The majority (%s %s) responded 'yes' to the poll titled: %s." % (str((pollYes/(pollYes + pollNo))*100), "%" , str(pollTitle)))
            elif (pollYes < pollNo):
                await client.send_message(message.channel, "The majority (%s %s) responded 'no' to the poll titled: %s." % (str((pollNo/(pollYes + pollNo))*100), "%" , str(pollTitle)))
            else:
                await client.send_message(message.channel, "The poll, " + str(pollTitle) + ", ended in a tie.")
            
        else:
            await client.send_message(message.channel, "{0.author.mention} please wait until the current Poll is finished to start a new one.".format(message))
    # User Vote No
    if (message.content.startswith("$n") or message.content.startswith("$N")):
        if (message.channel in channelsRunning):
            author ="{0.author.mention}".format(message)
            if not author in voted[message.channel]:
                voted[message.channel].append(author)
                pollNo += 1
                await update_poll(realPoll, pollTitle, pollNo, pollYes)
            else:
                await client.send_message(message.channel, "{0.author.mention} You've already voted.".format(message))
    # User Vote Yes        
    if (message.content.startswith("$y") or message.content.startswith("$Y")):
        if (message.channel in channelsRunning):
            author ="{0.author.mention}".format(message)
            if not author in voted[message.channel]:
                voted[message.channel].append(author)
                pollYes += 1
                await update_poll(realPoll, pollTitle, pollNo, pollYes)
            else:
                await client.send_message(message.channel, "{0.author.mention} You've already voted.".format(message))
            
            
client.run("token")    
#client.run(str(token)) for exe file
