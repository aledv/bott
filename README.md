# bott

This telegram bot will save audio files sent to it in a given directory, or execute shell script.

Simple python telegram bot based on Telepot library to save audio to server or execute shell script.
No need to set port-forwardings, no custom signed certificates, no webhooks, no bullshit.

# You'll need to run bott.py:

- Python interpreter, on debian: "sudo apt-get python".
- Telepot library, on debian with python installed: "sudo pip install telepot".
- Telegram bot token, obtainable via @BotFather chat, write it at the 'config.py'.

To enable bot to comunicate with you ( due to telegram security policy, anti-spam etc...), 
you need to chat first by opening bot chat and sending "/start", enough to unlock bot direct messaging without human interaction.

# To run bott

- **$ python bott.py [&]** 
- (to give bot root access) **$ sudo python bott.py [&]**
- [&] is for background process

# To run bott on startup

Edit /etc/rc.local and past **$ python bott.py [&]** before **exit** for run the boot on startup.

The bot is configured to reply only to your userid for security reasons, ever use spaces to indentate or you'll get execution errors, use tabs instead.
