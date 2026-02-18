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
    "\"stop fingering me\" - Niko (Not from OneShot"
]
restartin = [
    "Oh well, here goes nothing...!",
    "Hope this code works...",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "You know who else loves troubleshooting! My Buddie!!!",
    "Well, off to hang myself!",
    "Okie dokie. By the way, shoutouts to Spazbot. C:",
    "Okie dokie. By the way, shoutouts to Gummy's Bank Inc. C:",
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

client = discord.Client(intents=intents)

load_dotenv()
DATA_FILE = 'currency.json'
# buddie: 547900581692309521
# mell: 1078788946609324175
bot = discord.Bot(owner_id=547900581692309521)

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
testing = bot.create_group("testing", "admin tools 4 bruddie")

image = bot.create_group("image", "Image-related commands")

currency = bot.create_group("currency", "Currency commands")

buddie = bot.create_group("buddie", "commands to mess with buddie")


# ------------- event shyt

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    error = getattr(error, "original", error)
    if hasattr(ctx.command, 'on_error'):
        playsound('error.wav', block=False)
        await ctx.send(f"oh, i guess buddie flipped up something. go tell him about this error: `{error}`")

    if isinstance(error, commands.MissingRequiredArgument):
        playsound('error.wav', block=False)
        await ctx.send(f"Error: hey, you're missing the argument `{error.param.name}`! please, use the command properly.")
    elif isinstance(error, commands.MissingPermissions):
        playsound('error.wav', block=False)
        await ctx.send("Error: whoops, you don't have enough permissions! go get /op'd, right about now.")
    else:
        playsound('error.wav', block=False)
        await ctx.send(f"ohhh shoot i just had an error: `{error}`. bot didn't crash, but i recommend you ping me, budie double you, for this.")

@tasks.loop(seconds=20) # ts broken for whatever reason
async def status_task(self) -> None:
        statuses = [
            'Now featuring: Screenshots!', 
            'Also try: SpazBot',
            'Also try: Gummy\'s Bank INC.',
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

@testing.command(name="give", description="assign a stat to a user")
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
                set_value(user.id, stat, value)
                await ctx.respond(f'gave {user} {value} {stat}, their current balance is: {get_value(user.id, 'dollarys')}', ephemeral=True)
        else:
            if user.id == ctx.bot.user.id:
                await ctx.respond("yeah right. in your dreams.")
            elif user.bot:
                await ctx.respond("that's a bot you bum. go away")
            else:
                set_value(user.id, stat, value)
                await ctx.respond(f'gave {user} {value} {stat}, their current balance is: {get_value(user.id, 'dollarys')}')

@testing.command(name="reset_stats", description="Reset someone's stats. Feeling good yet?")
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
        

@currency.command(name="supergamba", description="instead of min and max being 2k, it's 10k. High risk, high reward!")
async def supergamba(ctx):
    gamba = random.randint(-10000,10000)
    playermonies = get_value(ctx.user.id, 'dollarys')
    if playermonies <= 0:
        await ctx.respond(f'whoops, sorry buddy, but you have {playermonies} dollary doos. cant supergamble in debt.')
        return
    add_value(ctx.user.id, 'dollarys', gamba)
    playermonies = get_value(ctx.user.id, 'dollarys')
    if gamba <= 0:
        await ctx.respond(f'{random.choice(gambalose)} wallet emptied by {gamba} dollary doos, current balance: {playermonies}')
    else:
        await ctx.respond(f'{random.choice(gambawin)} got {gamba} dollary doos, current balance: {playermonies}')

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
        ":video_game: Playing [**BombSquad: Gummy's Overhaul**](https://gamejolt.com/games/gummysoverhaul/923618) <:bluecap_boyfriend:1461469456399073332>",
        ":video_game: Playing [**Bombsquda**](https://github.com/MellBoii1/bombsquda) <:bluecap_boyfriend:1461469456399073332>",
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
    await ctx.respond("<:goofy_guy:1461469461784563898> Alright, if you say so! Here's his bio:\nspanish / english\num, no thank you!\nhttps://web-buddie.neocities.org/\nyou should keep reply ping on when talking to me unless you're just saying \"ok\"\n\n\nshoutouts to kevin eleven")

@bot.command(name="ping", description="how ass is my wifi rn")
async def ping(ctx: discord.ApplicationContext):
   await ctx.respond(f"<:bluecap_boyfriend:1461469456399073332> Ring! `{round(bot.latency*1000)}ms`")

@bot.command(name="gyatt", description="Buddie-bot, how big was the gyatt?")
async def gyat(ctx: discord.ApplicationContext):
   await ctx.respond("https://tenor.com/view/bonnie-fnaf-fnafmovie-gif-5124708767506072283 it was thiis big")

@testing.command(name="resetto", description="Resetto! I love troubleshooting.")
async def secret(ctx: discord.ApplicationContext):
    if admino_only(ctx) == False:
        await ctx.respond("what do you think you're doing. huh. non-admin. go away. freakin loser.", ephemeral=True)
    else:
        print("Restarting...")
        await ctx.respond(random.choice (restartin))
        os.execv(sys.executable, ['python'] + sys.argv)

@testing.command(name="shutup", description="Instead of shutting DOWN, it shuts UP!")
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

    while sixer != 69:
        sixer = random.randint(-100,100)
        result = result + " Number #" + str(sixer)
    
    check = len(result)

    if check >= 1999:
        await ctx.respond("I took more than 2000 characters to check for 69. Sorry!")
    else:   
        await ctx.respond(result)

@testing.command(name="refresh", description="Refreshes commands, because Discord is stupid.")
async def ref(ctx: discord.ApplicationContext):
    await ctx.respond("Your commands were already refreshed, or couldn't refresh. Sorry!!")

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
async def add(ctx, text: discord.Option(str)): # type: ignore
  # you can use them as they were actual integers
  if text == "@everyone":
    await ctx.respond("Are we deadass")
  elif text == "@here":
    await ctx.respond("Hey, uh, don't fucking do that.")
  else:
    await ctx.respond(f"{text}")

@image.command(name="buddie", description="Fetch a random image of Buddie. :]")
async def budzo(ctx: discord.ApplicationContext):
    await ctx.respond(random.choice (budimage))

@bot.command(name="help", description="Help")
async def help(ctx: discord.ApplicationContext):
    await ctx.respond("look at this menu dummy https://cdn.discordapp.com/attachments/1126856123119575081/1462173271213740244/image.png?ex=696d3a79&is=696be8f9&hm=c378f41412030d300e4253ff97417564e588fcecfb76917111626f308b46241a&")

@bot.command(name="friendquote", description="A quote from one of Buddie's friends")
async def friend(ctx:discord.ApplicationContext):
    await ctx.respond(random.choice (friendquotes))

@buddie.command(name="screenie", description="See Buddie's screen (He will be alerted) (I am not liable for anything that you see)")
@commands.cooldown(1, 15, commands.BucketType.user) 
async def scren(ctx:discord.ApplicationContext):
    # python allows for defs inside defs, so just put it here
    def on_exists(fname: str) -> None:
        """Callback example when we try to overwrite an existing screenshot."""
        file = Path(fname)
        if file.is_file():
            file.unlink()
    # run it ONCE the command is called
    with mss.mss() as sct:
        filename = sct.shot(output="LatestScreenshot.png", callback=on_exists)
        print("Took a screenshot at:")
        print(ctx.channel.id)
        playsound('screenshot.wav', block=False)
    await ctx.respond(file=discord.File(f'{filename}'))
    print()

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
    await ctx.respond("I don't know.")

@bot.command(name="scary_countdown", description="The countdown of doom! Gyulp.")
@commands.cooldown(1, 15, commands.BucketType.user) 
async def coutning(ctx:discord.ApplicationContext):
    await ctx.respond("10...")
    time.sleep(2)
    await ctx.send("9...")
    time.sleep(2)
    await ctx.send("8...")
    time.sleep(2)
    await ctx.send("7...")
    time.sleep(2)
    await ctx.send("6...")
    time.sleep(2)
    await ctx.send("5...")
    time.sleep(2)
    await ctx.send("4...")
    time.sleep(2)
    await ctx.send("3....")
    time.sleep(4)
    await ctx.send("2.....")
    time.sleep(6)
    await ctx.send("1......")
    time.sleep(10)
    await ctx.send("https://img.freepik.com/free-psd/single-yellow-potato-closeup-studio-shot_191095-85935.jpg?semt=ais_user_personalization&w=740&q=80")

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond("slow down there, pardner. this command is on cooldown for 15 seconds. go away.", ephemeral=True)
    else:
        raise error  # Here we raise other errors to ensure they aren't ignored

@bot.command(name="cudix_facts", description="CUDIX's seemingly random facts.")
async def cudih(ctx:discord.ApplicationContext):
    await ctx.respond("Detroit Lions own the Chicago Bears and Caleb Williams is not iceman\n\n\n\n\n\n... what? \"what does this mean\"...? i don't know either.")












































bot.run(os.getenv('TOKEN')) # type: ignore

# pycord tutorial shyt below:

#umm ima add it l8tr
