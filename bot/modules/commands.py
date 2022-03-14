import os
import linkGrabber
from pyrogram import Client, filters

from bot import CMD
from bot.welpers.translations import lang
from bot.welpers.utilities import bypasser


@Client.on_message(filters.command(CMD.START))
async def start(bot, update):
    await update.reply_text(
        text=lang.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
    )


@Client.on_message(
    filters.command(CMD.ATSN)
    & filters.regex(r"artstation\.com/(?:artwork|projects)/([0-9a-zA-Z]+)")
)
async def atsn(bot, update):
    id = update.matches[0].group(1)
    ouo = bypasser.art_k(id)
    message = await update.reply_text(
        text=ouo, disable_web_page_preview=False, quote=True
    )


@Client.on_message(filters.command(CMD.DPLK) & filters.regex(r"https?://[^\s]+"))
async def dpkl(bot, update):
    url = update.matches[0].group(0)
    ouo = bypasser.droplink(url)
    message = await update.reply_text(
        text=ouo, disable_web_page_preview=True, quote=True
    )


@Client.on_message(filters.command(CMD.WETR) & filters.regex(r"https?://[^\s]+"))
async def wetr(bot, update):
    url = update.matches[0].group(0)
    ouo = bypasser.wetransfer(url)
    message = await update.reply_text(
        text=ouo, disable_web_page_preview=True, quote=True
    )


@Client.on_message(filters.command(CMD.GPLK) & filters.regex(r"https?://[^\s]+"))
async def gpkl(bot, update):
    url = update.matches[0].group(0)
    ouo = bypasser.gplinks(url)
    message = await update.reply_text(
        text=ouo, disable_web_page_preview=True, quote=True
    )


@Client.on_message(filters.command(CMD.MDIK) & filters.regex(r"https?://[^\s]+"))
async def mdik(bot, update):
    url = update.matches[0].group(0)
    ouo = bypasser.mdisk(url)
    message = await update.reply_text(
        text=ouo, disable_web_page_preview=True, quote=True
    )


@Client.on_message(filters.command(CMD.BIFM) & filters.regex(r"https?://[^\s]+"))
async def bif(bot, update):
    x = update.matches[0].group(0)
    url = bypasser.encod(x)
    ouo = bypasser.bifm(url)
    message = await update.reply_text(
        text=ouo, disable_web_page_preview=True, quote=True
    )

def remove_dup(lst):
    set1 = set()
    final_list = []
    for i in lst:
        set1.add(i)
    for i in set1:    
        final_list.append(i)
    if final_list:
        if len(final_list) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
             out_file.write(str(final_list))
        message = await update.reply_document(
             document=filename,
             disable_notification=True,
             quote=True
        )
        os.remove(filename)
    else:
         message = await update.reply_text(
            text=final_list, disable_web_page_preview=True, quote=True)


@Client.on_message(filters.command(["test"]) & filters.regex(r"https?://[^\s]+"))
async def xy(bot, update):
    urlx = update.matches[0].group(0)
    xyz(urlx):
    Xf = await update.edit("`mm ...`")
    user_link = urlx
    links = linkGrabber.Links(user_link)
    grabbed_links = links.find(href=re.compile(".jpg|.mp4"))
    url_list = []
    for i in range(len(grabbed_links)):
        dic = grabbed_links[i]
         
        for key, values in dic.items():
            if key  == "href":
                url  =  values
                url_list.append(url)
                final_list = remove_dup(url_list)
