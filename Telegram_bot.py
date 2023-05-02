import asyncio
import telegram
import time

bot_token = 'your bot token'
bot = telegram.Bot(token=bot_token)

async def main():
    group_id = input('Telegram group ID: ')
    try:
        await bot.get_chat(chat_id=group_id)
    except telegram.error.TelegramError as e:
        print("This group doesn't exist")
        exit()

    message_text = input('Enter message: ')
    num_messages = int(input('Enter number of messages to send: '))
    send_rate = int(input('Enter message send rate in milliseconds (only numbers): '))

    for i in range(num_messages):
        try:
            await bot.send_message(chat_id=group_id, text=message_text)
            await asyncio.sleep(send_rate / 1000)
        except telegram.error.RetryAfter as e:
            print(f"Flood control exceeded. Retrying in {e.retry_after} seconds.")
            send_rate *= 2
            await asyncio.sleep(e.retry_after)
        except telegram.error.TelegramError as e:
            print(f"Error sending message: {e}")
            continue

asyncio.run(main())



