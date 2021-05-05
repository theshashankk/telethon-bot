
token = '1670476906:AAFAuzBosTcVVavWrJBx_4gUhuBFJfhSN-8'
api_id = 1357804
api_hash = 'b5a852ec39670bf077914dfa6d5ef4c5'

from telethon import TelegramClient, events
bot = TelegramClient (api_id, api_hash).start(bot_token=token)
@bot.on(events.NewMessage(pattern='/start'))
 async def code (event):
  await event.reply("jana bhen ne lodeee avi bot bana nhi ki tuu apni gand lekr aa gya bsdkkk bott tohh bannee dee pehle")

bot.run_until_disconnected()
