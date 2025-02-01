from redbot.core import commands
import random
import time

class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def direwolf(self, ctx):
        """Kappa"""
        
        direwolfMoments = [
            "https://files.catbox.moe/b9q3i0.png", #hateyou /
            "https://files.catbox.moe/l7yjio.png", #medieval /
            "https://files.catbox.moe/a21zgp.png", #odin /
            "https://files.catbox.moe/n1km0q.png", #peanut /
            "https://files.catbox.moe/ce5pp3.png", #cigarette
            "https://files.catbox.moe/icm2fq.png", #scoliojungle /
            "https://files.catbox.moe/qq629z.PNG", #goodduel /
            "https://files.catbox.moe/ge8k2e.jpg", #frankfurtsoup /
            "https://files.catbox.moe/bvqotd.jpg", #114000euro /
            "https://files.catbox.moe/g3dxs1.png", #applerefernce /
            "https://files.catbox.moe/fola64.png", #elite /
            "https://files.catbox.moe/799bbh.png", #notracist /
            "https://files.catbox.moe/tbbn7r.png", #cry /
            "https://files.catbox.moe/zzvjxn.png", #gr /
            "https://files.catbox.moe/iz5n5b.jpg", #vilionce /
            "https://files.catbox.moe/meiapo.jpg", #praywc /
            "https://files.catbox.moe/h2flxr.jpg", #lifegoal /
            "https://files.catbox.moe/82sn0t.jpg", #manythings /
            "https://files.catbox.moe/z2yt9h.jpg", #lasagnamaster /
            "https://files.catbox.moe/3wkra4.jpg", #rango /
            "https://files.catbox.moe/oafneb.webp", #killet
            "https://files.catbox.moe/tokqce.webp", #littlerat
            "https://files.catbox.moe/u9hgdy.webp", #reallyguy
            "https://files.catbox.moe/kpm70f.webp", #shyvana
            "https://files.catbox.moe/sgh0z2.webp", #report
            "https://files.catbox.moe/u9bpjo.webp", #saycrow
            "https://files.catbox.moe/rfadpe.webp", #boosted
            "https://files.catbox.moe/xbeke6.webp", #notmywords
            "https://files.catbox.moe/pctzym.webp", #global
            "https://files.catbox.moe/29kv05.webp", #lastword
            "https://files.catbox.moe/06wd04.webp", #ape
            "https://files.catbox.moe/1ea09k.webp", #uwu
            "https://files.catbox.moe/bese74.webp", #insulting
            "https://files.catbox.moe/h71jum.webp", #gotwithrat
            "https://files.catbox.moe/3agngm.webp", #6euro
            "https://files.catbox.moe/10kpdl.webp", #sweetsummerchild
            "https://files.catbox.moe/71er96.webp", #evenrat
            "https://youtu.be/MVF4QbS9JTo?si=1mjMKjZS_daPAe1g", #tactevid
            "https://youtu.be/-2nBV6iEH_U?si=xgeJBMO85gOiw9LO", #thewolfvid /
            "https://youtu.be/4-mfiyTvw2M?si=W7vERcefwqpcmgfO", #wolfvid /
        ]

        rng = random.randint(0, int(len(direwolfMoments)-1))

        await ctx.send(direwolfMoments[rng])

    @commands.command()
    async def forsen(self, ctx):
        
        forsen_rng = random.randint(0, 1)

        forsen_pics = [
            "https://files.catbox.moe/h23fgn.png", #heil
            "https://files.catbox.moe/5rkvee.webp", #nword
        ]

        await ctx.send(forsen_pics[forsen_rng])
        await ctx.send("https://www.op.gg/summoners/euw/Forsenxd-EUW")

    @commands.command()
    async def scolio(self, ctx):

        await ctx.send("https://files.catbox.moe/6e0vai.png")
        await ctx.send("come back")

    @commands.command()
    async def tactemess(self, ctx):

        tacterng = random.randint(0, 10)

        for i in range(tacterng):
            await ctx.send("<@142588842614980608>")
            time.sleep(0.1)

    @commands.command()
    async def hesright(self, ctx):
        
        await ctx.send("https://files.catbox.moe/lk4s36.png")
        await ctx.send("He's right you know.")
