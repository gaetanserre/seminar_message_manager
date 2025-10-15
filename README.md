# Seminar Message Manager

[![CI](https://github.com/gaetanserre/seminar_message_manager/actions/workflows/build.yml/badge.svg)](https://github.com/gaetanserre/seminar_message_manager/actions/workflows/build.yml)
[![PyPI version](https://badge.fury.io/py/seminar-message-manager.svg)](https://badge.fury.io/py/seminar-message-manager)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

A Python manager for automatically generating and sending mails, Zulip, Discord or Mattermost messages to announce upcoming seminars, using user-tunable html and markdown templates.

## 📦 Installation

Use `pip` to install the package:
```bash
pip install seminar-message-manager
```
## 💻 Usage

```bash
smm date [--seminar_csv csv_file.csv --mail_json mail.json --zulip_json zulip.json --discord_json discord.json --mattermost_json mattermost.json --template_mail template.html --template_zulip template.md --template_discord template.md (--send_mail | -sm) (--send_zulip | -sz) (--send_discord | -sd) (--send_mattermost | -smt) (--send | -s)]
```

### Argument details

- `seminar_csv` .csv file that describes the seminar's events following a specific template:
  ```csv
  date      ; location; first_name; last_name; work_name           ; work_link
  yyyy-mm-dd; room    ; John      ; Doe      ; My beautiful article; https://article-link.com
  ```
  By default, the package will look for `seminar.csv` in the root directory.
- `date` the date (yyyy-mm-dd) used to select the relevant information from the csv.

- `mail_json`.json file that described the mail information
  ```json5
  {
    "user"                   : "mail@mail.com",
    "password"               : "123456789",
    "smtp_server_domain_name": "smtp.mail.com",
    "port"                   : 587,
    "to"                     : ["mail_list@mail.com", "myothermail@mail.com"],
    "subject"                : "Upcoming seminar"
  }
  ```
  By default, the package will look for `mail.json` in the root directory.

- `zulip_json` .json file that describes the information needed by the Zulip bot:
  ```json5
  {
    "config_file": "zuliprc", // API file of the bot
    "bot_email"  : "mylab-bot@mylab.zulipchat.com",
    "channel"    : "Seminars",
    "topic"      : "Upcomming seminar",
    "old_topic"  : "Past seminars" // Topic in {channel} where past bot messages are moved
  }
  ```
  By default, the package will look for `zulip.json` in the root directory.

- `discord_json` .json file that describes the information needed by the Discord bot:
  ```json5
  {
    "webhook_url": "https://discord.com/api/webhooks/..."
  }
  ```
  By default, the package will look for `discord.json` in the root directory.

- `mattermost_json` .json file that describes the information needed by the Mattermost bot:
  ```json5
  {
    "webhook_url": "https://mattermost.com/hooks/..."
  }
  ```
  By default, the package will look for `mattermost.json` in the root directory.

- `template_mail` .html file that constitute the body of the mail ([example](templates/mail/announcement.html)). Some specific strings, indicated by `{}`, will be replaced by the package, using the corresponding csv line:
  - `{date}`
  - `{room}`
  - `{first_name}`
  - `{last_name}`
  - `{work_name}`
  - `{work_link}`

  By default, the package will look for `announcement.html` in the `./templates/mail` directory.
- `template_zulip` .md file, similar to html file, see [example](templates/zulip/announcement.md).

  By default, the package will look for `announcement.md` in the `./templates/zulip` directory.
- `template_discord` .md file, similar to html file, see [example](templates/discord/announcement.md).

  By default, the package will look for `announcement.md` in the `./templates/discord` directory.

- `template_mattermost` .md file, similar to html file, see [example](templates/mattermost/announcement.md).

  By default, the package will look for `announcement.md` in the `./templates/mattermost` directory.

- `--send_mail` or `-sm` if used, send message to the relevant mailing list.
- 
- `--send_zulip` or `-sz` if used, send message to the relevant Zulip topic.
- 
- `--send_discord` or `-sd` if used, send message to the relevant Discord channel.

- `--send_mattermost` or `-smt` if used, send message to the relevant Mattermost channel.

- `--send`or `-s` if used, send message to the relevant Zulip topic, Discord channel, Mattermost channel and mails.

## ⚖️ License

Distributed under the [GNU GPL 3.0 License](LICENSE).