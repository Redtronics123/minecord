from nextcord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot logged in as {self.bot.user}")
        print("""
             (  `                                   (     
             )\))(   (            (           (     )\ )  
             ((_)()\  )\   (      ))\  (   (   )(   (()/(  
             (_()((_)((_)  )\ )  /((_) )\  )\ (()\   ((_)) 
             |  \/  | (_) _(_/( (_))  ((_)((_) ((_)  _| |  
             | |\/| | | || ' \))/ -_)/ _|/ _ \| '_|/ _` |  
             |_|  |_| |_||_||_| \___|\__|\___/|_|  \__,_| 
        """)


def setup(bot):
    bot.add_cog(Ready(bot))
