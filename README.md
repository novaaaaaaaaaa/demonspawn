### Discord Bot README

This is a simple Discord bot implemented in Python using the Discord.py library. The bot performs basic functions such as responding to messages and greeting new members in a designated channel.

#### Prerequisites
- Python 3.x installed on your system.
- Discord.py library installed. You can install it via pip:
- Requests library installed. You can install it via pip:
  ```
  pip install discord.py

  pip install requests
  ```



#### Setup
1. Clone or download the repository to your local machine.
2. Create a file named `token.txt` in the same directory as the bot script (`bot.py`) and place your Discord bot token inside it.
3. Ensure the required permissions for your bot on your Discord server.
4. Customize the bot's functionality according to your preferences.

#### Usage
1. Run the bot script `bot.py`.
   ```
   python bot.py
   ```
2. The bot should now be active on your Discord server.

#### Bot Functionality
- **Greetings**: When a new member joins the server, the bot sends a welcome message to a specified channel.
- **Commands**: The bot responds to the `$hello` command by sending 'bang' to the channel where the command was issued.
- **Status**: The bot periodically changes its status, alternating between 'playing with fire' and 'playing with the damned'.

#### Important Note
- Ensure that your `token.txt` file is kept private and never shared publicly. It contains sensitive information that grants access to your Discord bot.

Feel free to modify and extend the functionality of the bot as per your requirements. Happy coding! 🤖