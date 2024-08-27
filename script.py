from telethon import TelegramClient, events

# Configura tus credenciales
api_id = '28294893'
api_hash = 'cea88db934848d835463cd9828b051ab'
phone_number = '+5350056238'

# IDs de los canales
source_channel = '@BTC_60s_prediction'  # ID o nombre de usuario del canal de origen
destination_channel = 'canal de reenvio'  # ID o nombre de usuario del canal de destino
keyword = 'x6.25'  # La palabra que quieres buscar

# Crear el cliente
client = TelegramClient('nombre_sesion', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message_text = event.message.message

    # Verifica si el mensaje contiene la palabra clave
    if keyword in message_text:
        # Reenvía el mensaje al canal de destino
        await client.send_message(destination_channel, event.message)
        print(f'Mensaje reenviado: {message_text}')

async def main():
    await client.start(phone_number)

    print(f"Escuchando mensajes en {source_channel}...")

    # Mantén el cliente en ejecución
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())

