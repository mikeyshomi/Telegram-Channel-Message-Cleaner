from telethon import TelegramClient
import asyncio

api_id = 13741389  # Replace with your API ID
api_hash = '8e3fead2e8bca9159cdeb004f420ab06'  # Replace with your API Hash
phone = '+2348121874059'  # Replace with your phone number including country code

client = TelegramClient('session', api_id, api_hash)

async def delete_my_messages():
    group = await client.get_entity('updatedarf')
    async for message in client.iter_messages(group, from_user='me'):
        try:
            await client.delete_messages(group, message.id)
            print(f"Deleted message {message.id}")
        except Exception as e:
            print(f"Failed to delete message {message.id}: {e}")

async def main():
    await client.start(phone)
    await delete_my_messages()
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())

