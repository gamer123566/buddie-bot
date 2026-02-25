"""Buddie Bot"""
# --------- imports
import discord
import asyncio
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context
import sys
from dotenv import load_dotenv
import os
from discord.ext import commands
import random
import json
from mss import mss
from pathlib import Path
import mss
from playsound3 import playsound 
import win32gui
import psutil     #psutil - https://github.com/giampaolo/psutil
import win32process
import time
import ffmpeg
import pyautogui
import keyboard
import webbrowser

# ---- variables cause its annoying to have them clutter my shyt ----
hytale = "https://cdn.discordapp.com/attachments/1461513081459970236/1461762256168550648/image.png?ex=696bbbb0&is=696a6a30&hm=fbb800c1305463a1d18cc85e353cf1eac3e1ce1c3e84dd4b492b16a5c6b7b1fe&"
goonzies = "https://cdn.discordapp.com/attachments/1461493312203526204/1461837475482697840/Powerups.png?ex=696c01bd&is=696ab03d&hm=17db5082e919c1250fbebc30d7938b4cd98d79d0d7bbbc4751aa3ea3dac3e531&"
budimage = [
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166562617426063/argentinian_buddi.png?ex=696d343a&is=696be2ba&hm=c4a36eb7f8697456b2527221a332bdb4c01ffe69909640944466a5cb6be58c30&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166563217084539/attachment_but_gummyt.gif?ex=696d343a&is=696be2ba&hm=9d008ef16a1104a36711706b92440f0aa58375710324993a48f96a992fd3012d&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166563531784305/attachment_but_noob.gif?ex=696d343a&is=696be2ba&hm=7c4bca3caddf251b6528af446d7e22b878899772171d02a332b8492531861913&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166562617426063/argentinian_buddi.png?ex=696d343a&is=696be2ba&hm=c4a36eb7f8697456b2527221a332bdb4c01ffe69909640944466a5cb6be58c30&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166564307603629/budder_pfp_number_Birthday_Special_gajillion.png?ex=696d343a&is=696be2ba&hm=a1da854e45047191e34830f1b22bfaa7f9ac4c3133ab41126956824ebe7c84ee&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166564697801019/budder_pfp_number_one_gajillion.png?ex=696d343a&is=696be2ba&hm=3b494969dfec9413dc2c11386c92f92055a9bfb76d51850f93075d20addba564&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166565297459475/buddie_construct.png?ex=696d343a&is=696be2ba&hm=48ccc176eed13bbcc0f8a6be58f4cb61d5ff2332eb7235d5464af76e6a4a1c3c&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166565653839954/buddie_fumo.png?ex=696d343a&is=696be2ba&hm=a99e4ec92f2fbfce42b7b890c352715603a82a5948d071f6676f89d508753b73&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166565964484742/buddie_pfp_six_gazillion.png?ex=696d343b&is=696be2bb&hm=d1f21da8d04d8586353a954004ea8cb3bc3310f299337aefe120ffdc1dc1205a&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166681915752682/buddie_pfp_five_million.png?ex=696d3456&is=696be2d6&hm=06e6506dcb71d1db0ed605069e72cf17f18f52175995518e49939d81333a4b5a&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166682570195066/buddie_small_pfp.png?ex=696d3456&is=696be2d6&hm=52674f69df8044340f9622e254d0da1481f3997d965ced04698038f56b53f2dc&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166682872320255/buddie_smaller_pfp.png?ex=696d3456&is=696be2d6&hm=b005bf0bc509b5574d7d9f319df5d402ff8f27ded937e35b77bfa17d53a1af67&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166683543142644/chirismas_budlie_double_u.png?ex=696d3457&is=696be2d7&hm=9f78a2af4d3079cb7eb32e1ab4a06695b6f311437fe30cda1ef37fc0b89f15aa&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166684344516911/eb_buddie.png?ex=696d3457&is=696be2d7&hm=8cf51c6a7fcc400840edb06441ba58eab670c5ce2764b57670f56174f5df7dec&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166684050788447/dapper_buddie.png?ex=696d3457&is=696be2d7&hm=b33d8e61e0c20ac789196ede010a0acbbe44e766b0fc9ba2fa2c3fab33b6695e&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166895968125090/builders_club.png?ex=696d3489&is=696be309&hm=2cdeee12403eb251d4df8c91fa429b271702a113f6f3bb5b28acd3d903c59fdc&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166896353869988/eb_pajama_buddie.png?ex=696d3489&is=696be309&hm=50bd8eafb7467da37e4d65a33be9992a53676541d8ac251026d06c1f25e2abc8&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166896714711242/im_gonna_attack_you.png?ex=696d3489&is=696be309&hm=a070cd65656e6b6bb2e678258eb035b018bd61e14c42dd5134d02da8a5ce76d4&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1462166898593628373/soretro_buddie.png?ex=696d348a&is=696be30a&hm=4be2d8662186ea9f9ab6988ffc4418172a14b4965833aed55080fba5269ca761&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1471679296933330986/steamuddie.png?ex=698fcfa6&is=698e7e26&hm=4d909c836e5e9a3c300f3af71e92c5d3585757d64e7a991f934e15fab387603c&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1471679296933330986/steamuddie.png?ex=698fcfa6&is=698e7e26&hm=4d909c836e5e9a3c300f3af71e92c5d3585757d64e7a991f934e15fab387603c&",
        "https://cdn.discordapp.com/attachments/1461513081459970236/1473423927043821812/Buddie_Ultimate_PFP.png?ex=69962877&is=6994d6f7&hm=f1611cec7d0cc3aba0d137371acd6819db4b37e95b3e8ceae0956bc0b85623bc&"
    ]
kasane = [
    "https://static.wikia.nocookie.net/utau/images/0/01/Teto22.png/revision/latest?cb=20150110230357&path-prefix=es",
    "https://preview.redd.it/kasane-teto-sv-illustrated-by-sakauchi-waka-v0-jeh7180iknra1.jpg?width=640&crop=smart&auto=webp&s=d84c1b655f9b3ff7ce309bdda00975efbbd9b578",
    "https://m.media-amazon.com/images/I/613FwkW60mL._AC_UF894,1000_QL80_.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbvzqgNrFhSbk_wBVskLpnslqeN4fcmjPSLw&s",
    "https://preview.redd.it/teto-birdbrain-v0-p7xz8is56lff1.jpg?width=553&format=pjpg&auto=webp&s=7bf77a4080a49a055633e490b2586b2587845fb5",
    "https://cdn.discordapp.com/attachments/1475675152032465037/1476097716764545126/image.png?ex=699fe2a0&is=699e9120&hm=aeb5f6dddc23dbc33c24f8b578ca67b95d3d5f8dd1f263b4e0cd9579c37fe218&",
    "https://www.japanzon.com/208144-product_hd/good-smile-company-pop-up-parade-kasane-teto-l-size-non-scale-pre-painted-figure.jpg",
    "https://preview.redd.it/art-by-sagami-kasane-teto-attack-form-v0-fs2hvwzkzy7c1.jpeg?width=640&crop=smart&auto=webp&s=c041a5a9779957b321be5f8402804681cdb0f970",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq7s68ARbK7YjbPfFc5NL2AQK8kuk57hEOOg&s",
    
]
friendquotes = [
    "\"Yosh was here\" - Mitsuri",
    "\"erm what the sigma\" - Mell",
    "\"Maybe you know me, maybe you don't.\" - Buddie, probably.",
    "I would've put a racial slur here, 'cause Gummyboiyt said it, but it's kinda against the rules. Sorry.",
    "\"You like kissing boys, don't you?\" -...who??",
    "\"im hooning it\" - Gummyboiyt",
    "\"You know who else had their spine removed?\" - Muscle Man",
    "\"Friend inside me\" - Woody, probably.",
    "\"Hi guys im the mother from the Mother™ series\" - The Mother from the Mother™ series",
    "📞: \" hi guys its me im the father from the Mother 2 game\" - Your father, from Mother™ 2/Earthbound©",
    "\"I HATE EVERYTHING\" - Interesting",
    "\"i loove hooning\" - Bud-, wait, when did I ever say that?!",
    "\"DARK, DARKER, YET DARKER.\" - Gaster, the royal scientist\n.",
    "\"hi guys\" - Goofy Guy",
    "\"Baby horses are juggling Wingstop locations in the middle of San Francisco\" - CUDIX",
    "\"stop fingering me\" - Niko (Not from OneShot",
    "\"Hey, you're not part of my Sprites\nget back to that box of yours   immediately\"\n-Ness"
]
restartin = [
    "Oh well, here goes nothing...!",
    "Hope this code works...",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "You know who else loves troubleshooting! My Buddie!!!",
    "Well, off to hang myself!",
    "Okie dokie. By the way, shoutouts to Spazbot. C:",
    "What the helly",
    "Well, okay. Bye-bye.",
    "What?! NO, DUDE!!!!!!!!!!!",
    "My head's spinning...",
    "What? What do you mean I have to kill myself?",
    "Oh well.",
    "Literally Roblox is too hard!!",
    "https://cdn.discordapp.com/attachments/1471252400999239895/1471253871698645186/roblock_hard.mov?ex=6990e671&is=698f94f1&hm=6ebbe6d2549fcb6e449dfec46f53ffa923528a460444bfbb1c70d26b41efbd53&"
]
# -------essentials
intents = discord.Intents.default()
intents.presences = True # Enable the presence intent
intents.members = True # Often needed for other functions, good practice to include
intents.message_content = True # ok maybe remove this later

bot = discord.Bot(intents=intents)

load_dotenv()
DATA_FILE = 'currency.json'
# ids:
# buddie - 547900581692309521
# mell: - 1078788946609324175

# they look the exact same, but take my word for it they arent
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_value(user_id: int, label: str, default=0):
    data = load_data()
    if label == 'dollarys':
        default = 100
    if label == 'admino':
        default = False
    return data.get(str(user_id), {}).get(label, default)

def set_value(user_id: int, label: str, value):
    data = load_data()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}
    data[uid][label] = value
    save_data(data)

def add_value(user_id: int, label: str, amount: int):
    current = get_value(user_id, label, 0)
    set_value(user_id, label, current + amount)
    return current + amount

def admino_only(ctx):
    data = load_data()
    if get_value(ctx.author.id, 'admino') != True:
        return False
    else:
        return True



# command groups
testing = bot.create_group("testing", "testing stuff")

image = bot.create_group("image", "Image-related commands")

currency = bot.create_group("currency", "Currency commands")

buddie = bot.create_group("buddie", "commands to mess with buddie")

admin = bot.create_group("admin","admin tools")


# ------------- event shyt

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):

    error = getattr(error, "original", error)
    
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond("hey hey hey. wait just a minute. this command's on cooldown! go play MineCrap, or whatever you kids play nowadays.", ephemeral=True)
    
    elif isinstance(error, discord.errors.NotFound):
        await ctx.respond("whoops, the command errored. try running it again!")
        raise error

    elif hasattr(ctx.command, 'on_error'):
        playsound('error.wav', block=False)
        await ctx.respond(f"oh, i guess buddie flipped up something. go tell him about this error: `{error}`")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.respond(f"Error: hey, you're missing the argument `{error.param.name}`! please, use the command properly.", ephemeral=true)

    elif isinstance(error, commands.MissingPermissions):
        playsound('error.wav', block=False)
        await ctx.respond("Error: whoops, you don't have enough permissions! i don't know how you got this error, since there's no commands that need permissions, so please ping buddie and tell him to fix his shyt")

    else:
        playsound('error.wav', block=False)
        ctx.command.reset_cooldown(ctx)
        await ctx.respond(f"ohhh shoot i just had an error: \n`{error}` \nbot didn't crash, but i recommend you ping budie double you for this.\n-# don't ping if it's an unknown integration error. i can't fix that. just suck it up and try the command again.")
        raise error # We must raise the error so the Buddie of the Double Us can fix the error.

@tasks.loop(seconds=20) # ts broken for whatever reason
async def status_task(self) -> None:
        statuses = [
            'Now featuring: Screenshots!', 
            'Also try: SpazBot',
            'Also try... wait, what do you mean this status got removed?',
            'What? What do you mean? I didn\'t do that.',
            'straight up budding it',
            'Committing crimes...',
            'Give Me Your Data!',
            'I\'m gonna leak where you live: Earth.',
            'Beep, boop.',
            'That\'s the 50TH ERROR THIS WEEK!',
            'You know who else had a Syntax Error?',
            'whuh',
            'zzz...',
            'F',
            'Buddie-bot would never ask for your face.',
            'Playing Minecrap',
            'Playing Super Mario Bros. Remastered',
            'Playing J*b Simulator',
            'Playing Rob Blox',
            'wega',
            'SMAAAAASH!!!',
        ]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

@status_task.before_loop
async def before_status_task(self) -> None:
        """
        Before starting the status changing task, we make sure the bot is ready
        """
        await self.wait_until_ready()
        

async def setup_hook(self) -> None:
        self.logger.info(f"Logged in as {self.user.name}")
        self.logger.info(f"Python version: {platform.python_version()}")
        self.logger.info(
            f"Running on: {platform.system()} {platform.release()} ({os.name})"
        )
        self.logger.info("-------------------")
        self.status_task.start()
        self.check_server.start()

startin = [
    "Buddie-Bot is up 'n runnin'. Can't wait for it to die instantly.",
    "Buddie-Bot is ready. Please, God, let this code work.",
    "Buddie-Bot is locked 'n loaded!",
    "Buddie-Bot has started up.",
    "Buddie-Bot is here, ready to execute commands!"
]

@bot.event
async def on_ready():
    playsound('start.wav', block=False)
    print(random.choice(startin))


# ---------- ai generated commands
# error right there on the console twin
# Command to check balance
@currency.command(name="balance", description="see how many dollary doos you have in yo walet")
@discord.option("user", description="Who's balance should you see?")
async def balance(ctx, user: discord.Member):
    if ctx.user.bot:
        await ctx.respond("hey, that's a bot. those don't get to have money.", ephemeral=True)
    elif user == bot.user:
        await ctx.respond("sorry, dude. i got no dollary doos on me. just trust me.", ephemeral=True)
    else:
        await ctx.respond(f"{user.mention} has {get_value(user.id, 'dollarys')} dollary doos.")

workign = [
    "worked at a macgongals and got 500 dollary doos <:bluecap_cool:1461469457661694045> new balance:",
    "worked with erm what the sigma and got 500 dollary doos <:bluecap_cool:1461469457661694045> new balance:",
    "you did something and got 500 dollary doos <:bluecap_cool:1461469457661694045> new balance:",
    "did a kickflip and someone gave you 500 dollary doos <:bluecap_cool:1461469457661694045> new balance:",
    "typed random numbers on a screen and got paid 500 dollary doos... somehow. <:goofy_guy:1461469461784563898> new balance:"
]
gambalose = [
    "well, shucks. you lost the lottery.",
    "aw dangit!",
    "oof. you lost.",
    "brozalawg lost the lottery smh,",
    "erm. you lost. what a loser."
]
gambawin = [
    "YOU WON!",
    "hooray! you won the lotery!!",
    "YIPPEEE!!! you won!!",
    "yayzers you win,,",
    "ummm, okay. you win. whatever."
]

# get a JOB and earn monies
@currency.command(name="workin", description="get a JOB!!!!! (Scariest gameplay imaginable)")
async def work(ctx):
    add_value(ctx.user.id, 'dollarys', 500)
    await ctx.respond(f'{random.choice(workign)} {get_value(ctx.user.id, 'dollarys')}')

@admin.command(name="give", description="assign a stat to a user")
@discord.option("stat", description="What stat? [STATS: dollarys, admino]")
@discord.option("user", description="Who should recieve it?")
@discord.option("value", description="How much, or what?")
@discord.option("hidden", description="Should it be hidden?", required=False, default=True, input_type=bool)
async def hooneringit(ctx, user: discord.Member, stat, value, hidden: bool):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        if hidden == True:
            if user.id == ctx.bot.user.id:
                await ctx.respond("yeah right. in your dreams.", ephemeral=True)
            elif user.bot:
                await ctx.respond("that's a bot you bum. go away", ephemeral=True)
            else:
                print(f"{ctx.user} gave {user} {value} {stat}")
                set_value(user.id, stat, value)
                await ctx.respond(f'gave {user} {value} {stat}, their current balance is: {get_value(user.id, 'dollarys')}', ephemeral=True)
        else:
            if user.id == ctx.bot.user.id:
                await ctx.respond("yeah right. in your dreams.")
            elif user.bot:
                await ctx.respond("that's a bot you bum. go away")
            else:
                print(f"{ctx.user} gave {user} {value} {stat}")
                set_value(user.id, stat, value)
                await ctx.respond(f'gave {user} {value} {stat}, their current balance is: {get_value(user.id, 'dollarys')}')

@admin.command(name="reset_stats", description="Reset someone's stats. Feeling good yet?")
@discord.option("user", description="Who?")
async def take(ctx, user: discord.Member):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        if user.id == ctx.bot.user.id:
            await ctx.respond("yeah right. in your dreams.", ephemeral=True)
        elif user.bot:
            await ctx.respond("that's a bot you bum. go away", ephemeral=True)
        else:
            set_value(user.id, 'dollarys', 100)
            await ctx.respond(f'reset {user}\'s dollary doos, their current balance is: {get_value(user.id, 'dollarys')}', ephemeral=True)

# don't work (and maybe like die)
@currency.command(name="evilwork", description="remain unemployed (most boring gameplay imaginable)")
async def evilwork(ctx):
    playermonies = get_value(ctx.user.id, 'dollarys')
    if playermonies >= 24:
        add_value(ctx.user.id, 'dollarys', -25) # negative because EVIL
        playermonies = get_value(ctx.user.id, 'dollarys')
        await ctx.respond(f'You spent 25 dollary doos buying instant noodles. Because youre unemployed. Balance: {playermonies} (By the way, this economy SUCKS! What do you mean a cup of noodles is 25 DOLLARY DOOS???)')
    else:
        add_value(ctx.user.id, 'dollarys', -9000) # even more evil
        playermonies = get_value(ctx.user.id, 'dollarys')
        await ctx.respond(f"You went to the grocery store, but couldn't afford anything to eat. You then starved to death. -9000 dollary doos, current balance: {playermonies}")


@currency.command(name="gamba", description="because every currency bot needs one")
async def gamba(ctx):
    gamba = random.randint(-2000,2000)
    playermonies = get_value(ctx.user.id, 'dollarys')
    if playermonies <= 0:
        await ctx.respond(f'whoops, sorry buddy, but you have {playermonies} dollary doos. cant gamble in debt.')
        return
    add_value(ctx.user.id, 'dollarys', gamba)
    playermonies = get_value(ctx.user.id, 'dollarys')
    if gamba <= 0:
        await ctx.respond(f'{random.choice(gambalose)} wallet emptied by {gamba} dollary doos, current balance: {playermonies}')
    else:
        await ctx.respond(f'{random.choice(gambawin)} got {gamba} dollary doos, current balance: {playermonies}')
        

@currency.command(name="supergamba", description="instead of min and max being 2k, it's 10k. High risk, high reward! [40s cooldown]")
@commands.cooldown(1, 40, commands.BucketType.user)
async def supergamba(ctx):
    gamba = random.randint(-10000,10000)
    playermonies = get_value(ctx.user.id, 'dollarys')
    print(playermonies)
    if playermonies <= 0:
        await ctx.respond(f'whoops, sorry buddy, but you have {playermonies} dollary doos. cant supergamble in debt.')
        return
    add_value(ctx.user.id, 'dollarys', gamba)
    playermonies = get_value(ctx.user.id, 'dollarys')
    if gamba <= 0:
        await ctx.respond(f'{random.choice(gambalose)} wallet emptied by {gamba} dollary doos, current balance: {playermonies}')
    else:
        await ctx.respond(f'{random.choice(gambawin)} got {gamba} dollary doos, current balance: {playermonies}')

@currency.command(name="american_roulette", description="It's like Russian Roulette, but every chamber except one is loaded! Gyulp. [60s cooldown]")
@commands.cooldown(1, 60, commands.BucketType.user)
async def deathlmfao(ctx):
    winnings = random.randint(0,9999999)
    bullet = random.randint(1,6)
    playermonies = get_value(ctx.user.id, 'dollarys')
    if playermonies <= 0:
        await ctx.respond(f'whoops, sorry buddy, but you have {playermonies} dollary doos. cant play russian roulette in debt.')
        return
    if bullet == 1:
        add_value(ctx.user.id, 'dollarys', winnings)
        newmoniez = playermonies + winnings
        await ctx.respond(f"Hooray! You survived! Got {winnings}, current balance: {newmoniez}")
    else:
        add_value(ctx.user.id, 'dollarys', -999999999)
        newmoniez = playermonies -999999999
        await ctx.respond(f"Ouchie mama! You died. Thankfully, the Medic from TF2 was right there to revive you! The medical bill is 999,999,999 dollary doos, though. Balance: {newmoniez}")
# If this fails, add 'async' to it
def get_hwnds_by_exe_name(exe_name: str):
    """
    Finds window handles (HWNDs) for a given executable name or path.
    Attributes:
        exe_name: The name of the executable we should search.
    """
    hwnd_list = []
    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            # Get the process ID for the window
            _, process_id = win32process.GetWindowThreadProcessId(hwnd)
            try:
                # Get the process name or path using psutil
                process = psutil.Process(process_id)
                process_name = process.name()
                
                # Check if the process name matches the target
                if process_name.lower() == exe_name.lower():
                    hwnd_list.append(hwnd)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle potential errors if the process is gone or access is denied
                pass
        return True # Continue enumeration
    # Enumerate all top-level windows
    win32gui.EnumWindows(win_enum_handler, None)
    return hwnd_list
    
# function to run it
@buddie.command(name="music", description="What's Buddie listening to?")
async def get_music(ctx):   
    target_exe_name = "foobar2000.exe" 
    found_windows = get_hwnds_by_exe_name(target_exe_name)

    if found_windows:
        for hwnd in found_windows:
            window_title = win32gui.GetWindowText(hwnd)
            respounse = f"{window_title}"
            respounsetwo = respounse.replace('[foobar2000]',' ')
            await ctx.respond(respounsetwo)
    else:
        await ctx.respond(f"Hey, {target_exe_name}, Buddie's preffered music app, isn't open. Either he's on YouTube or he isn't listening to anything.")

#---------- human commands (i made them!! buddie boule you!!! or just got them from a template)

@bot.command(description="Say hi to Buddie-bot")
async def hello(ctx):
  await ctx.respond(f"Hello, {ctx.author}! <:bluecap_cool:1461469457661694045>")

@bot.command(name="whatareyoudoing", description="Ask the bot what he's doing")
async def wyd(ctx: discord.ApplicationContext):
    gaming = [
        ":video_game: Playing [**DELTARUNE**](https://www.deltarune.com/) <:bluecap_boyfriend:1461469456399073332>",
        ":video_game: Playing [**BombSquda**](https://github.com/MellBoii1/bombsquda) <:bluecap_boyfriend:1461469456399073332>",
        "lowk doing something that i cannot say rn",
        "Being tested on. Help me",
        "william afton screaming in hell.ogg",
        "Having some drinks with my Friends and Fellas Buds and Bluds",
        "your mother <:bluecap_cool:1461469457661694045>",
        "Being developed on!",
        "listening to homeroLoop.ogg on repeat"
    ]
    await ctx.respond(random.choice (gaming))

@bot.command(name="buddieinfo", description="Tell me about Buddie.")
async def brodie(ctx: discord.ApplicationContext):
    await ctx.respond("<:goofy_guy:1461469461784563898> Alright, if you say so! Here's his bio:\nspanish / english\nNow remastered!\nhttps://web-buddie.neocities.org/\nyou should keep reply ping on when talking to me unless you're just saying \"ok\"\n\n\nshoutouts to kevin eleven")

@bot.command(name="ping", description="how ass is my wifi rn")
async def ping(ctx: discord.ApplicationContext):
   await ctx.respond(f"<:bluecap_boyfriend:1461469456399073332> Ring! `{round(bot.latency*1000)}ms`")

@bot.command(name="gyatt", description="Buddie-bot, how big was the gyatt?")
async def gyat(ctx: discord.ApplicationContext):
   await ctx.respond("https://tenor.com/view/bonnie-fnaf-fnafmovie-gif-5124708767506072283 it was thiis big")

@admin.command(name="resetto", description="Resetto! I love troubleshooting.")
async def secret(ctx: discord.ApplicationContext):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        print("Restarting...")
        await ctx.respond(random.choice (restartin))
        os.execv(sys.executable, ['python'] + sys.argv)

@admin.command(name="shutup", description="Instead of shutting DOWN, it shuts UP!")
async def shutdown(ctx):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        print("Bot is shutting down... Death to all bugs!")
        await ctx.respond("Oh god. I see it. I see the light. Please. I don't wanna die. I don't wanna die. I DON'T WANNA DIE I DON'T WANNA DIE **I DON'T WANN**")
        await bot.close() # Gracefully closes the connection to Discord

@image.command(name="goony", description="Displays a picture of Goonin' Gummy. Viewer discretion is adviced.")
async def goony(ctx: discord.ApplicationContext):
    await ctx.respond(goonzies)

@image.command(name="hytaleherobrine", description="hytale herobrine")
async def heroin(ctx: discord.ApplicationContext):
    await ctx.respond(hytale)

@bot.command(name="69finder", description="Keeps rolling between -100 and 100 until it finds 69, then posts the progress. Nice.")
async def sixtynine(ctx: discord.ApplicationContext):
    sixer = random.randint(-100,100)
    result = "Number #" + str(sixer)
    await ctx.defer()
    while sixer != 69:
        sixer = random.randint(-100,100)
        result = result + " Number #" + str(sixer)
    
    check = len(result)

    if check >= 1999:
        await ctx.respond("I took more than 2000 characters to check for 69. Sorry!")
    else:   
        await ctx.respond(result)

@testing.command(name="refresh", description="Refreshes commands, because Discord is stupid.") #change the description every update
async def ref(ctx: discord.ApplicationContext):                                                #to make the command say its outdated and make it
    await ctx.respond("Your commands were already refreshed, or couldn't refresh. Sorry!!")    #force refresh your commands list

@testing.command(name="math", description="First+Second. Used for testing multiple fields.")
# pycord will figure out the types for you
async def add(ctx, first: discord.Option(int), second: discord.Option(int)): # type: ignore
  # you can use them as they were actual integers
  sum = first + second
  await ctx.respond(f"The sum of {first} and {second} is {sum}.")

@bot.command(name="getip", description="Returns your totally real IP Address. Don't use this in a public space!")
async def dox(ctx: discord.ApplicationContext):
    num1 = random.randint(1,255)
    num2 = random.randint(1,255)
    num3 = random.randint(1,255)
    num4 = random.randint(1,255)
    num5 = random.randint(1,255)
    await ctx.respond(str(num1) + "." + str(num2) + "." + str(num3) + "." + str(num4) + "." + str(num5) + "...Have fun!!")

@bot.command(name="speak", description="says the things that you put in")
async def speak(ctx, texter): # type: ignore
  # you can use them as they were actual integers
  if "@everyone" in texter:
    await ctx.respond("Hey, uh, don't fucking do that.")
  elif "@here" in texter:
    await ctx.respond("Don't ever touch a keyboard ever again")
  else:
    check = len(texter)

    if check >= 1999:
        await ctx.respond("Text is too long. Couldn't send.", ephemeral=True)
    else:
        await ctx.respond(texter)

@image.command(name="buddie", description="Fetch a random image of Buddie. :]")
async def budzo(ctx: discord.ApplicationContext):
    await ctx.respond(random.choice (budimage))

@bot.command(name="help", description="Help")
async def help(ctx: discord.ApplicationContext):
    await ctx.respond("look at this menu dummy https://cdn.discordapp.com/attachments/1126856123119575081/1462173271213740244/image.png?ex=696d3a79&is=696be8f9&hm=c378f41412030d300e4253ff97417564e588fcecfb76917111626f308b46241a&")

@bot.command(name="friendquote", description="A quote from one of Buddie's friends")
async def friend(ctx:discord.ApplicationContext):
    await ctx.respond(random.choice (friendquotes))

@buddie.command(name="screenie", description="See Buddie's screen (He will be alerted) (I am not liable for anything that you see) [15s cooldown]")
@commands.cooldown(1, 15, commands.BucketType.user) 
async def scren(ctx:discord.ApplicationContext):
    # python allows for defs inside defs, so just put it her
    def on_exists(fname: str) -> None:
        """Callback example when we try to overwrite an existing screenshot."""
        file = Path(fname)
        if file.is_file():
            file.unlink()
    # run it ONCE the command is called
    with mss.mss() as sct:
        playsound('screenshot.wav', block=False)
        filename = sct.shot(output="LatestScreenshot.png", callback=on_exists)
        print("Took a screenshot at:")
        print(f'{ctx.channel.name}, at server {ctx.guild.name}')
    await ctx.respond(file=discord.File(f'{filename}'))
    # print()

@bot.command(name="rizzmeter", description="How much rizz do you have, according to randint?")
async def rizzy(ctx: discord.ApplicationContext):
    riz = random.randint(0,100)
    await ctx.respond(f"you have {riz}% rizz twin")

@image.command(name="kaido", description="what did he sayyyy????")
async def kaidoling(ctx: discord.ApplicationContext):
    await ctx.respond("https://cdn.discordapp.com/attachments/1126856123119575081/1472349747149930678/image.png?ex=6992400e&is=6990ee8e&hm=9b9799c5d8c4abf7a246fda76c52ee9e0b649fe2942b9b7a1c6c1a8c23bd10e8&")

@image.command(name="lamarjackson", description="Per the suggestion of CUDIX")
async def lamar(ctx:discord.ApplicationContext):
    await ctx.respond("https://cdn.discordapp.com/attachments/1390156735830032567/1473006828609867907/IMG_5268.jpg?ex=6994a403&is=69935283&hm=07739d6685611044a7531523ba3477b4a527767d880c5df07f9ebdd0e29cf5e7&")

@bot.command(name="ai", description="Talk to Buddie-bot, powered by Merl AI")
async def merl(ctx:discord.ApplicationContext, message):
    await ctx.respond(f"-# {ctx.author} said: {message}\nI don't know.")

@bot.command(name="scary_countdown", description="The countdown of doom! Gyulp. [20s cooldown]")
@commands.cooldown(1, 20, commands.BucketType.user) 
async def coutning(ctx:discord.ApplicationContext):
    await ctx.respond("10...")
    await asyncio.sleep(2)
    await ctx.send("9...")
    await asyncio.sleep(2)
    await ctx.send("8...")
    await asyncio.sleep(2)
    await ctx.send("7...")
    await asyncio.sleep(2)
    await ctx.send("6...")
    await asyncio.sleep(2)
    await ctx.send("5...")
    await asyncio.sleep(2)
    await ctx.send("4...")
    await asyncio.sleep(2)
    await ctx.send("3....")
    await asyncio.sleep(4)
    await ctx.send("2.....")
    await asyncio.sleep(6)
    await ctx.send("1......")
    await asyncio.sleep(10)
    await ctx.send("https://img.freepik.com/free-psd/single-yellow-potato-closeup-studio-shot_191095-85935.jpg?semt=ais_user_personalization&w=740&q=80")

@bot.command(name="cudix_facts", description="CUDIX's seemingly random facts.")
async def cudih(ctx:discord.ApplicationContext):
    await ctx.respond("Detroit Lions own the Chicago Bears and Caleb Williams is not iceman\n\n\n\n\n\n... what? \"what does this mean\"...? i don't know either.")


@bot.command(name="ytmp3_download", description="Download and send a YouTube video as an MP3! Provided by yt-dlp. [120s cooldown]")
@commands.cooldown(1, 120, commands.BucketType.user) 
@discord.option("link", description="Link of the video you wish to download")
async def yt(ctx:discord.ApplicationContext, link):
    audiooutput = "output.mp3"
    youretube = ['https://www.youtube.com/watch?v=', 'https://youtu.be/']
    if any(keyword in link for keyword in youretube):
        await ctx.respond("Alright, hold on... This might take a bit, so just relax, and be patient.")
        file = Path(audiooutput)
        if file.is_file():
            file.unlink()
        os.system(f'yt-dlp.exe -o "output.%(ext)s" -t mp3 "{link}"')
        if os.stat('output.mp3').st_size >= 10000000:
            await ctx.respond("File output was too big to upload to Discord. What kinda audio were you trying to download, anyways?!")
            return
        else:
            await ctx.respond(f"Original link: {link}", file=discord.File(f'{audiooutput}'))
    else:
        await ctx.respond("Not a valid link.")

@bot.command(name="webcam", description="See Buddie's... webcam...? I'm not too sure about this one.")
async def trolo(ctx:discord.ApplicationContext):
    await ctx.respond("https://cdn.discordapp.com/attachments/1461513081459970236/1474201797450272808/trolfeis_mirror_selfie_lmaooo.jpg?ex=6998fce9&is=6997ab69&hm=a802139e38b7ea34cba0878715310bd54149b2be236588b6b88b31b9a51b7ecb&")

# the following commands are admin only because god knows what people would do if they weren't :fearful:
@admin.command(name="buddie_cursor", description="Move the cursor on Buddie's screen to mess with him (X and Y values)")
async def cursoring(ctx:discord.ApplicationContext, why: int, ex: int):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.")
    else:
        playsound('cursor.wav', block=False)
        print("look at you. lookin at the console to see if it really happened. yes, buddie. your cursor did move. you're not insane. now go back to playing minecraft. fucking shit for brains.")
        pyautogui.moveRel(ex, why)
        await ctx.respond("done") 

@admin.command(name="buddie_type", description="It does what it says on the tin. Types on Buddie's end. gyulp")
@discord.option("text", description="tyope on budie keybor lol")
async def WhatTheFuckAreYouDoingToMyPCBro(ctx:discord.ApplicationContext, text):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        if len(text) >= 60:
            await ctx.respond("go away loser", ephemeral=True)
        else:
            playsound('cursor.wav', block=False)
            keyboard.write(text,delay=0)
            await ctx.respond("done")

@admin.command(name="buddie_key", description="It does what it says on the tin. Presses a key on Buddie's end. gyulp")
@discord.option("key", description="Important keys: 'f11','esc','space','backspace'")
async def WhatTheFuckAreYouDoingToMyPCBro(ctx:discord.ApplicationContext, key):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        playsound('cursor.wav', block=False)
        keyboard.press_and_release(key)
        await ctx.respond("done")

@admin.command(name="buddie_website", description="Opens Chrome and forces Buddie to enter a specific website")
@discord.option("site", description="Website URL (must have https:// at the beginning)")
async def webbingsyte(ctx:discord.ApplicationContext, site: str):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
        return
    if not site.startswith( ('https://', 'http://') ):
        await ctx.respond("website doesn't begin with https:// (likely not a website)", ephemeral=True)
        return
    if site.startswith('http://'):
        await ctx.respond("website is insecure (uses http and not https)", ephemeral=True)
        return
    print(f"{ctx.user} opened the website {site} on yo pc")
    playsound('cursor.wav', block=False)
    webbrowser.open(site)  # Source - https://stackoverflow.com/a/4302041
    await ctx.respond("done")

# ok no more admino comands
@bot.command(name="github_info", description="Link to the Github page for this bot")
async def leenk(ctx:discord.ApplicationContext):
    await ctx.respond("[Here!](https://github.com/gamer123566/buddie-bot)")

@testing.command(name="intentional_error", description="lol errorz")
async def errorerleing(ctx:discord.ApplicationContext, erorname):
    raise NameError(erorname)

@image.command(name="tetokasane", description="Various images of Kasane Teto. Very cool. :) (Yes, I did get these from Google Images.)")
async def tetoling(ctx:discord.ApplicationContext):
    await ctx.respond(random.choice (kasane))

@bot.command(name="mastick_coin", description="Mastick's coin of approval. Basically just a cooler coinflip")
async def imhooneringit(ctx:discord.ApplicationContext):
    coin = random.randint(0,1)
    if coin == 0:
        await ctx.respond("https://cdn.discordapp.com/attachments/1473404984581296168/1474488991742038149/ezgif-2677d3af0aa0112f.gif?ex=699ff722&is=699ea5a2&hm=9fc8bb15b176632adb569af22f8eefbf0cfe2741a1c3dd59ab5994269d7dc62c&")
    else:
        await ctx.respond("https://cdn.discordapp.com/attachments/1473404984581296168/1474488992148754700/ezgif-3275af723423c6a9.gif?ex=699ff722&is=699ea5a2&hm=88e3915c539e299e822126382f2ae93be077e63db295b19db6650ef883c0822c&")


bot.run(os.getenv('TOKEN')) # type: ignore
