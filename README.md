# Crypto-price Telegram bot

### Description

This is a telegram bot written in python to monitor cryptocurrency prices on CEX exchanges
(Binance, ByBit, MEXC, Gate.io and BingX)

## Installation

Use the [git](https://git-scm.com/) to clone repository 

```bash
git clone https://github.com/alexeusdefire/pricebot.git
```

## Usage

### 1. Go to Telegram and search for @BotFather (https://t.me/botfather)

### 2. Create your own bot with BotFather (use this [docs](https://core.telegram.org/bots))

### 3. After cloning the repository, go to the directory and create an .env file in the root of the directory

### 4. Put your token from BotFather to .env file

### 5. Go to terminal and create virtual environment:

```bash
pyhon -m venv .venv
```
### 6. Activate venv:

### For PowerShell:
```
.\venv\Scripts\Activate.ps1
```

### For CMD:
```
.\.venv\Scripts\activate.bat
```

### For Linux/macOS
```
source .venv/Scripts/activate
```

### 7. Install dependencies

```
pip install -r requirements.txt
```

### 8. Run main.py in IDE or write in terminal:
```
python main.py
```
