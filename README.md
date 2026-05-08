# QuoteWatch

A lightweight stock quote monitoring tool for Chinese A-shares market.

## Features

- Real-time stock price and percentage change display
- Supports Shanghai, Shenzhen, and Beijing stock exchanges
- Floating transparent window
- Draggable interface
- Auto-refresh every 2 seconds

## Stock Code Rules

| Market | Code Prefix | Exchange Prefix |
|--------|-------------|-----------------|
| Shanghai Main Board | 600/601/603/605 | sh |
| STAR Market (Sci-Tech Innovation Board) | 688 | sh |
| Shenzhen Main Board | 000/001/002 | sz |
| ChiNext (Growth Enterprise Market) | 30 | sz |
| Beijing Stock Exchange | 83/87/88/920 | bj |

## Usage

### 1. Configure Stock Codes

Create `config.txt` in the same directory as the executable, with one stock code per line:

```
688981
000001

```

Or use exchange prefix (lowercase required):
```
sh600519
sz000001
bj830799
```

### 2. UI Configuration (Optional)

Create `ui.txt` to customize UI settings:

```
透明度：85
```

### 3. Run

Simply run `QuoteWatch.exe`.

### 4. Exit

Right-click on the window to exit.

## Build from Source

### Prerequisites

```bash
pip install pyinstaller requests
```

### Build Command

```bash
pyinstaller --onefile --windowed --icon="icon.png" --name QuoteWatch main.py
```

### Build Output

The executable will be generated in the `dist/` directory.

## Data Source

Stock data is fetched from Tencent Finance API (`qt.gtimg.cn`).

## License

MIT
