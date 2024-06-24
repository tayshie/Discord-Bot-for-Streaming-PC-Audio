# Discord Audio Bot

This Discord bot allows users to stream audio from their PC to a Discord voice channel. It includes a web interface for managing user preferences and bot settings.

## Features

- Join and leave voice channels
- Stream system audio to Discord voice channels
- Web interface for managing users and preferences
- RESTful API for user management

## Prerequisites

- Python 3.8+
- FFmpeg
- Discord Bot Token
- (Optional) Virtual environment

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-audio-bot.git
   cd discord-audio-bot
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install FFmpeg:
   - On Windows: Download from https://ffmpeg.org/download.html and add it to your PATH.
   - On macOS: Use Homebrew: `brew install ffmpeg`
   - On Linux: Use your package manager, e.g., `sudo apt-get install ffmpeg`

## Configuration

1. Copy `config/config.example.json` to `config/config.json`.
2. Edit `config/config.json` and fill in your Discord bot token and other settings.

## Usage

1. Start the bot and web server:
   ```
   python main.py
   ```

2. In Discord, invite the bot to your server and use the following commands:
   - `!join`: Bot joins your current voice channel
   - `!leave`: Bot leaves the voice channel
   - `!stream [duration]`: Bot streams audio for the specified duration (default: 5 seconds)

3. Access the web interface at `http://localhost:5000` (or the host/port specified in your config).

## Project Structure

```
discord_audio_bot/
│
├── config/
│   ├── config.json
│   └── config_schema.json
│
├── bot/
│   ├── __init__.py
│   ├── audio_handler.py
│   └── commands.py
│
├── web/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── database/
│   └── models.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py)
- [Flask](https://flask.palletsprojects.com/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)

## Disclaimer

This bot is for educational purposes only. Ensure you have the right to stream any audio content and that you comply with Discord's Terms of Service and API usage guidelines.
