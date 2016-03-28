# Shascii

Shascii is a terminal splash screen based on ascii art. Ideal for bash or sh consoles.
The main goal of this project is to brag every time we open our terminal. Enjoy it.

![demo image](https://raw.githubusercontent.com/oskargicast/shascii/gh-pages/images/spider.png)

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
$ echo -e "\npython ~/.zsh/shascii/welcome.py" >> .bashrc
```

Or this, for zsh:
```bash
$ echo "\npython ~/.zsh/shascii/welcome.py" >> .zshrc
```

## Customizing the shell

You can see and edit the default configuration in this file:

```bash
$ cat ~/.zsh/shascii/message.json
```

For instance, if you edit *message.json* with this:

```bash
{
    "asci-art": "chasqui.txt",
    "welcome-message": "Hi shascii"
}
```

You will get this awesome **[peruvian chasqui](http://en.wikipedia.org/wiki/Chaski)**, pronounced like */shascii/*

![demo image](https://raw.githubusercontent.com/oskargicast/shascii/gh-pages/images/chasqui.png)
