# AbuseRemoverBot

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/BadshahAk/AbuseRemoverBot)

> A Professional Telegram Bot to **Auto Delete Abusive Words**, **Detect NSFW Stickers/GIFs**, **Warn Users**, and **Mute after 3 Warnings**.  
> Fully customizable and easy to deploy on **Heroku**.

---

## Features:

- Delete Abusive Messages Instantly
- Detect and Delete NSFW Stickers, GIFs
- Track User Warnings (3 warns = 24 hours mute)
- Send Deleted Content to a Logger Channel
- Ignore Replies (except abusive reply gets deleted too)
- Admins' Abuse also gets Deleted
- Advanced Abuse Detection (Hindi, English, Local Gali)
- MongoDB based Warning System
- Heroku and Docker Deploy Support
- Highly Optimized and Stable

---

## Variables:

| Variable | Description |
|:---------|:------------|
| `API_ID` | Telegram API ID (from [my.telegram.org](https://my.telegram.org)) |
| `API_HASH` | Telegram API HASH |
| `BOT_TOKEN` | Your Bot Token from [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Your Telegram User ID |
| `LOGGER_ID` | Channel ID where bot logs activities |
| `CRIME_CHANNEL` | Channel username where abusive content is saved |
| `MONGO_URI` | MongoDB database URI |

---

## Deploy to Heroku:

1. Click the button below:

    [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/BadshahAk/AbuseRemoverBot)

2. Fill all environment variables correctly.
3. Done!

---

## Deploy Manually:

```bash
$ git clone https://github.com/BadshahAk/AbuseRemoverBot
$ cd AbuseRemoverBot
$ pip install -r requirements.txt
$ python3 main.py
