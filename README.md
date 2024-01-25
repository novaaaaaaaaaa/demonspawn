# Discord Bot with Welcome Message and Status Rotation

This is a simple Discord bot script written in Python using the [discord.py](https://discordpy.readthedocs.io/) library. The bot has functionality to welcome new members to a specific channel and rotates its status playing different games.

## Prerequisites

Before running the bot, ensure you have the following installed:

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/)

## Setup

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Create a virtual environment (optional but recommended).

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Create a file named `token.txt` in the same directory as the script and place your bot token inside it.

## Configuration

- `welcome_channel_id`: Set the channel ID where the welcome messages will be sent.
- `logger`: Configures logging to save Discord events in `discord.log`.
- `intents`: Sets up custom intents for better member tracking.

## Running the Bot

Run the bot using the following command:

```bash
python your_bot_script.py
```

Make sure your bot is added to your Discord server, and the necessary permissions are granted.

## Bot Features

- Welcomes new members to the specified channel.
- Responds to the command `$hello` with a message.
- Rotates its status playing different games.

## Customization

Feel free to modify the script to add more features or customize the behavior of your bot.

## Using a Class-based Client

The script includes an alternative implementation using a class-based client. If you prefer using a class-based approach, uncomment the relevant code and comment out the original bot setup.

```python
# class my_client(discord.Client):
#     # ... (uncomment and modify as needed)
```

## Disclaimer

This script is a basic template for a Discord bot. It's recommended to enhance and modify it based on your specific requirements and needs. Ensure you comply with Discord's [Terms of Service](https://discord.com/terms) and [Developer Policy](https://discord.com/developers/docs/policy) while developing and deploying your bot.
