# QuoteWatch 股票行情小工具 / Stock Quote Monitor

> 基于网友代码修改 / Based on code from a fellow netizen

[中文](#中文) | [English](#english)

---

## 中文

### 功能特点

- 实时显示股票价格和涨跌幅
- 支持沪市、深市、北交所所有股票
- 透明悬浮窗显示
- 窗口可自由拖动
- 每 2 秒自动刷新

### 股票代码规则

| 市场 | 代码前缀 | 交易所前缀 |
|------|----------|------------|
| 沪市主板 | 600/601/603/605 | sh |
| 科创板 | 688 | sh |
| 深市主板 | 000/001/002 | sz |
| 创业板 | 30 | sz |
| 北交所 | 83/87/88/920 | bj |

### 使用说明

**1. 配置股票代码**

在与 exe 同目录下创建 `config.txt` 文件，每行一个股票代码：

```
600519
688981
000001
300750
830799
```

也可以直接使用交易所前缀（必须小写）：
```
sh600519
sz000001
bj830799
```

**2. UI 配置（可选）**

创建 `ui.txt` 文件来自定义界面：

```
透明度：85
```

**3. 运行程序**

双击 `QuoteWatch.exe` 运行即可。

**4. 退出程序**

右键点击窗口即可退出。

### 编译打包

```bash
pip install pyinstaller requests
pyinstaller --onefile --windowed --icon="图标.png" --name QuoteWatch main.py
```

编译后的 exe 文件在 `dist/` 目录下。

### 数据来源

股票数据来源于腾讯财经接口 (`qt.gtimg.cn`)。

---

## English

### Features

- Real-time stock price and percentage change display
- Supports Shanghai, Shenzhen, and Beijing stock exchanges
- Floating transparent window
- Draggable interface
- Auto-refresh every 2 seconds

### Stock Code Rules

| Market | Code Prefix | Exchange Prefix |
|--------|-------------|-----------------|
| Shanghai Main Board | 600/601/603/605 | sh |
| STAR Market | 688 | sh |
| Shenzhen Main Board | 000/001/002 | sz |
| ChiNext | 30 | sz |
| Beijing Stock Exchange | 83/87/88/920 | bj |

### Usage

**1. Configure Stock Codes**

Create `config.txt` in the same directory as the executable, one code per line:

```
600519
688981
000001
300750
830799
```

Or use exchange prefix (lowercase required):
```
sh600519
sz000001
bj830799
```

**2. UI Configuration (Optional)**

Create `ui.txt` to customize UI settings:

```
Transparency: 85
```

**3. Run**

Double-click `QuoteWatch.exe` to run.

**4. Exit**

Right-click on the window to exit.

### Build from Source

```bash
pip install pyinstaller requests
pyinstaller --onefile --windowed --icon="icon.png" --name QuoteWatch main.py
```

The executable will be generated in the `dist/` directory.

### Data Source

Stock data is fetched from Tencent Finance API (`qt.gtimg.cn`).

### License

MIT
