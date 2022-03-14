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
                                    return final_list
                                    
                                    @Client.on_message(filters.command(CMD.DPLK) & filters.regex(r"https?://[^\s]+"))
                                    async def xy(bot, update):
                                      urlx = update.matches[0].group(0)
                                      ouo = xyz(urlx)
                                      message = await update.reply_text(
                                        text=ouo, disable_web_page_preview=True, quote=True
                                        )
                                        
                                        def xyz(urlx):
                                          Y = requests.get(url)
                                          bs4 = BeautifulSoup(Y.content, "lxml")
                                          X = bs4.find_all(href=re.compile(".jpg|.mp4"))
                                          for i in range(len(X)):
                                            dic = X[i]
                                            for key, values in dic.items():
                                              if key  == "href":
                                                url  =  values
                                                url_list.append(url)
                                                final_list = remove_dup(url_list)
                                                print(final_list)
                                                