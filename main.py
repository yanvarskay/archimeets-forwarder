import asyncio
from telethon import TelegramClient, events
from aiohttp import web

# --- твои данные ---
api_id = 26949120
api_hash = 'eedc531c26cc3535997ceac80f84d82e'
bot_token = '7981956100:AAGFXB3hx153WjwTMIlA2-juLIO0Syllb5Y'

# --- ключевые слова ---
KEYWORDS = [
    'воркшоп', 'встреча', 'конференция', 'круглый стол',
    'open talk', 'выставка', 'биеннале', 'форум',
    'фестиваль', 'рандом кофе', 'конкурс', 'лекция', 'заявка', 
    'паблик ток', 'паблик-ток', 'паблик-токе', 'дискуссия', 'meeting',
    'вечер', 'регистрация', 'регистрации', 'мероприятие', 'мероприятия',
    'финал', 'день', 'сессия', 'спикер', 'спикеры', 'анонс',
    'лекторий', 'лекций', 'лекции', 'вебинар', 'воркшопа',
    'воркшопов', 'ссылке', 'ссылка', 'конкурса', 'конкурсе',
    'конкурсу', 'фестивале', 'фестивалю', 'форума',
    'дискуссия', 'дискуссию', 'событие', 'события', 'мероприятие'
]

# --- каналы ---
CHANNELS = [
    'meeting_businessclub', 'ab_tobe', 'oamspb',
    'kgplo47', 'aclassdom', 'gorod_proekt_spb',
    'civil_architects', 'mlaplus_russia', 'planthebest',
    'march_pro', 'ahouseproject'
]

TARGET_CHAT = '@Archi_Meets'

# --- Telethon клиент ---
client = TelegramClient('session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    msg = event.message.message.lower()
    if any(kw in msg for kw in KEYWORDS):
        text = f"\ud83d\udd0d Найдено событие:\n\n{event.message.message}\n\n\ud83d\udc49 https://t.me/{event.chat.username}/{event.id}"
        await client.send_message(TARGET_CHAT, text)

# --- Фейковый HTTP сервер для Railway / Render ---
async def handle(request):
    return web.Response(text="Bot is running!")

app = web.Application()
app.router.add_get("/", handle)

async def main():
    await client.start()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
    print("Bot and web server started.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
