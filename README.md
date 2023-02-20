# Telegram bot
Telegram Bot with SQLite database authorization

## Files:
* Database - folder with database files
* Handlers - folder with files for messages and button creation
* Config - file with bot's telegram token (other variables can be added there)
* Create_bot - "Create bot" itself
* Main - bot launch

## Configuration:
### Config.py
* _telegram_bot_token_ - here is your bot's API TOKEN \
![image](https://user-images.githubusercontent.com/46675878/220085522-77e0c1b7-d009-408d-9b9a-6c76453274ed.png)

### Create_bot.py
* _sqlite3.connect_ - here is the path to your database file \
![image](https://user-images.githubusercontent.com/46675878/220084950-576456e6-ca75-4272-9b90-896c9a6df344.png)

## Launch
### Pycharm:
* Open your bot folder with Pycharm and if you have the "Current file" setting, open main.py and click start (green arrow) \
![image](https://user-images.githubusercontent.com/46675878/220087279-5774fbc7-5bb2-4c64-92e2-c13419169500.png)

### Command Deck:
#### Windows and Linux:
```
cd your_path_to_folder
python main.py
```
> On Linux you might not have "python main.py" work, try "python3 main.py"
