# Shascii

Shascii is a terminal splash screen based on ascii art. Ideal for bash or sh consoles.
The main goal of this project is to brag every time we open our terminal. Enjoy it.

![demo image](https://raw.githubusercontent.com/oskargicast/shascii/gh-pages/images/terminal1.png)

## Setup

We download the project.

```bash
$ mkdir .zsh && cd .zsh
$ https://github.com/oskargicast/shascii.git
```

Then we need to add this line to the the end of the .bashrc or .zshrc config files.

```bash
python ~/.zsh/shascii/welcome.py 
```

Or just execute this, for bash.

```bash
$ echo "\npython ~/.zsh/shascii/welcome.py" >> .bashrc
```

Or this, for zsh:
```bash
$ echo "\npython ~/.zsh/shascii/welcome.py" >> .zhrc
```
