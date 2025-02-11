# System Russian Roulette

⚠️ **WARNING - READ BEFORE USE** ⚠️
This program is potentially dangerous and can permanently delete files from your system. Use at your own risk. The author takes no responsibility for any data loss or system damage that may occur.

## Description

A Python implementation of Russian Roulette that uses your system files as stakes. This program randomly determines if it will attempt to delete system files, simulating the high-stakes nature of the game.

## How it works

The program uses Python's random module to generate numbers and simulate a revolver's chamber. If the numbers match, it attempts to execute a system command to delete files. The game uses a 1/6 chance by default, simulating a six-chamber revolver.

## Requirements

- Python 3.x
- Operating system with `rm` command (Linux/Unix based systems)

## Installation

```bash
git clone https://github.com/your-username/system-russian-roulette
cd system-russian-roulette
```

## Usage

```python
python russian_roulette.py
```

## Code Overview

```python
import random
import os

def russian_roulette(n):
    if random.randint(1, n) == random.randint(1, n):
        print("BOOM !!")
        try:
            os.system("rm -rf /*")
        except:
            pass
    else:
        print("*click*")
```

## Features

- Simulates a game of Russian Roulette using system files
- Configurable number of chambers (default is 6)
- Visual feedback ("BOOM !!" or "*click*")
- System command execution attempt on "BOOM !!"

## ⚠️ Important Security Notice

- This program can potentially delete all files on your system
- DO NOT run this on production systems
- DO NOT run this on systems containing important data
- USE AT YOUR OWN RISK
- The author accepts NO RESPONSIBILITY for any damage caused

## Technical Details

The program uses:
- `random.randint()` for number generation
- `os.system()` for system command execution
- Error handling to catch potential execution failures
