# GetMeA

> Only Linux supported!

> Don't you just want to get a bun ?

```bash
~: getmea bun
```

GetMeA is an AI-powered software installer. It aims to combat the recent trend of not putting software into the distro-specific registries (looking at you, Deno or Bun :p), which leads to developers wasting their precious time googling and getting sidetracked the fricking curl <someaddress> | sh command.

Just run getmea and tell it what to install. It will use your system package manager if possible but fall back to searching the web for you and coming up with a plan. Because AI has proven itself to be extremely wacky, you'll, of course, be asked before it runs any commands to protect your highly customized Linux installation.

## Installation

- Download the latest build artifact
- Run the setup: `./getmea.bin setup`

## Development

```bash
# Install deps
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Debug project
python src/main.py

# Compile project
nuitka src/main.py 
```

## Attribution

This product includes software developed by UncleCode (<https://x.com/unclecode>) as part of the Crawl4AI project (<https://github.com/unclecode/crawl4ai>).
