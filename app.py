from telethon.sync import TelegramClient
import datetime
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('telethon.config')
api_id = config['telethon_credentials']['api_id']
api_hash = config['telethon_credentials']['api_hash']

client = TelegramClient('session_name', api_id, api_hash)
chats = ["USERNAME_OF_CHANNELS"]
df = pd.DataFrame()
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)

for chat in chats:
    with client:
        # datetime.date.today() - datetime.timedelta(days=1)
        for message in client.iter_messages(chat, offset_date=start_date, reverse=True):
            message_date = message.date.date()
            
            # if message_date > end_date:
            #     break
            
            data = {
                "group": chat,
                "sender id": message.sender_id,
                "message": message.text,
                "date": message_date
            }
            
            temp_df = pd.DataFrame(data, index=[1])
            df = df._append(temp_df)


# df["date"] = df["date"].dt.tz_localize(None)
df.to_excel("data_{}.xlsx".format(datetime.date.today()), index=False)
