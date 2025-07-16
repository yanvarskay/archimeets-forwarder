from telethon import TelegramClient, events

# === ТВОИ ДАННЫЕ ===
api_id = 26949120
api_hash = 'eedc531c26cc3535997ceac80f84d82e'
bot_token = '7981956100:AAGFXB3hx153WjwTMIlA2-juLIO0Syllb5Y'

# === НАСТРОЙКИ ===
KEYWORDS = [
    'воркшоп', 'встреча', 'конференция', 'круглый стол', 'open talk',
    'выставка', 'биеннале', 'форум', 'фестиваль', 'рандом кофе', 'конкурс',
    'лекция', 'заявка'
]

CHANNELS = [
    'meeting_businessclub', 'ab_tobe', 'oamspb', 'kgplo47', 'aclassdom',
    'gorod_proekt_spb', 'civil_architects', 'mlaplus_russia', 'planthebest',
    'march_pro', 'ahouseproject'
]

TARGET_CHAT = '@Archi_Meets'

# === КОД ===
client = TelegramClient('session_name', api_id,
                        api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    msg = event.message.message.lower()
    if any(kw in msg for kw in KEYWORDS):
        text = f"📌 Найдено событие:\n\n{event.message.message}\n\n🔗 https://t.me/{event.chat.username}/{event.id}"
        await client.send_message(TARGET_CHAT, text)


print("✅ Бот запущен и слушает каналы!")
client.run_until_disconnected()
