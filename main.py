import discord
from discord.ext import commands
import os
import random

Prefix = "#"
Token = os.environ['TOKEN']
client = commands.Bot(command_prefix=Prefix)


@client.event
async def on_ready():
 print(f"Im In Discord {client.user.name}")
 await client.change_presence(activity=discord.Activity(
 type=discord.ActivityType.watching,
 name=f"{Prefix}help Servers   {len(client.guilds)}"),status=discord.Status.idle)



@client.command(aliases=['كت تويت', 'كت'])
async def cut(ctx):
    cut = [
        "- كم لعبة في هاتفك؟",
        "- أكثر فترة دراسية قريبة لقلبك وكونت فيها أصدقاء؟", "- أقبح شعور؟",
        "- غداؤك لليوم؟", "- نسبة النعاس عندك حاليًا؟",
        "- \"آسف لا أستطيع التحدث معك\" ما هو ردّك على الجملة؟",
        "- اسم بنت جميل وفخم بحرف السين؟", "- ماذا تفعل عندما تشتاق؟",
        "- ماذا يعني لك الانتظار؟", "- كيف كان أسبوعك؟",
        "- من اسباب الخيانه ؟", "- مادة تكرها بس درجاتك عالية فيها ؟",
        "- مقوله ماشي عليها هذي الفترة ؟ ", "- الاخ يفتش جوال اخته ؟",
        "- كم من عشرة الصبر عندك ؟", "- لماذا تختفي المشاعر الحلوة بسرعة؟",
        "- أجمل شيء حصل معك في هاليوم؟", "- آخر إنجازاتك؟",
        "- صِف نفسك بكلمة وحيدة فقط ؟! ", "- مغني عالقة معك أغانيه هاليومين؟",
        "- اعتقد انه عندي فوبيا مِن؟",
        "- مستعد للتضحية من أجل من تُحب؟ \n 1. نعم \n 2. لا\n3. حسب التضحية" <
        "- كم سنة مضت على امتلاكك لهاتفك؟",
        "- فترة دراسية لو أتيح لك إعادتها توافق؟\n1. الإبتدائي\n2. الثانوي\n3. الجامعة\n4. كرهت الدراسة",
        "- لغة حاولت تتعلمها ومللت؟",
        "- تقول: كيف أتخلّص من مشاعري تجاه شخص أعرف أنه لا يحبني؟",
        "- صريح، لمن تشتاق؟", "- رياضة تابعتها وأعجبتك بجانب كرة القدم؟",
        "- أجمل بلد أوروبي يمكن زيارته في الشتاء؟🌧❄",
        "- شعورك الحالي في كلمة؟", "- كلمة تلخص أحداث يومك؟",
        "- شخص يقول: متى يحق لي عدم احترام الشخص الذي بمقابلي؟",
        "- أكثر نوع من الشوكولاتة تُحبه؟", "- ذكرى تبتسم عندما تخطر في بالك؟",
        "- أكثر درس تعلمته من مواقع التواصل؟", "- أغرب عاداتك؟",
        "- أجمل شعور؟", "- حكمة عالقة في ذهنك؟", "- شيء تود تجربته؟",
        "- شخصية قديمة تُحبها؟"
    ]
    msg = random.choice(cut)
    carnage = discord.Embed(color=0x555555,
                            description="**" + msg + "**",
                            timestamp=ctx.message.created_at)
    carnage.set_footer(text=ctx.author.display_name,
                       icon_url=ctx.author.avatar_url)
    carnage.set_thumbnail(url=ctx.guild.icon_url)
    carnage.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(embed=carnage)


client.run(Token)
