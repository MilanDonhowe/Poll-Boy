# Poll-Boy - A discord bot for better decision making.
A discord bot which allows simple in-chat yes-or-no polls.

Created on: 12/31/17

## Installation
To setup your own Poll-Boy bot you'll need to:  


 ***1**. Download the .py file.*  
 ***2**. Go to [the Discord Developer Page](https://discordapp.com/developers/applications/me) and create a New App.*  
 ***3**. Add a bot user*  
 ***4**. Go to this url with your own client id added https://discordapp.com/api/oauth2/authorize?client_id=YOUR-CLIENT-ID-HERE&permissions=537078784&scope=bot*  
 ***5**. Add bot to server which you select.*  
 ***6**. Add your bot token (you can get the bot token from your discord app page) to the .py file one the last line (as a string! "")*  
 ***7**. Put the .py script running on a server or your computer.*    
 
 
***Experiencing troubles?  Bring up an issue over on the issues tab!***

## Usage
* ```$poll [yes or no question]``` - Creates poll.  
* ```$y``` - Votes yes for current poll.  
* ```$n``` - Votes no for current poll.  
* ```$help``` - Displays help screen.  
### Example  

![Gif example here](https://github.com/MilanDonhowe/ReadmeImages/blob/master/PollBoyExample.gif)

## Built With
 * [Discord.py](https://github.com/Rapptz/discord.py) - A python wrapper for the discord API.
 * [Asyncio](https://docs.python.org/3/library/asyncio.html#module-asyncio) - The standard library used for asynchronous programming in Python.
 * [Python 3.5.4](https://www.python.org/downloads/release/python-354/) - The programming language used.
