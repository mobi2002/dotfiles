# source bashrc if running bash
[ -n "$BASH_VERSION" ] && [ -f "$HOME/.bashrc" ] && . "$HOME/.bashrc"

# add local bin folder to path if it exist
[ -d "$HOME/.local/bin" ] && export PATH="$HOME/.local/bin:$PATH"

# default programs
export EDITOR="nvim"
export VISUAL="nvim"
export TERMINAL="st"
export BROWSER="qutebrowser"

# development
export MAKEFLAGS="-j5"

# XDG Base Directory structure
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"

# clean up home folder (inspired by Luke Smith)
# Note: variables for gtk2rc and qt style are in ~/.config/xinitrc
# because they need to be accessable by gui apps
export XAUTHORITY="$XDG_RUNTIME_DIR/Xauthority"
export LESSHISTFILE="-"
export TERMINFO="$XDG_DATA_HOME/terminfo"
export TERMINFO_DIRS="$XDG_DATA_HOME/terminfo:/usr/share/terminfo"
export PYTHONSTARTUP="$XDG_CONFIG_HOME/pythonrc"
export INPUTRC="$XDG_CONFIG_HOME/readline/inputrc"
export HISTFILE="$XDG_DATA_HOME/bash/history"

# some coloring in less
export LESS=-R
export LESS_TERMCAP_mb=$'\E[1;31m'     # begin blink
export LESS_TERMCAP_md=$'\E[1;36m'     # begin bold
export LESS_TERMCAP_me=$'\E[0m'        # reset bold/blink
export LESS_TERMCAP_so=$'\E[01;44;33m' # begin reverse video
export LESS_TERMCAP_se=$'\E[0m'        # reset reverse video
export LESS_TERMCAP_us=$'\E[1;32m'     # begin underline
export LESS_TERMCAP_ue=$'\E[0m'        # reset underline

# start X server if on tty1 and X server not already running
[ "$(tty)" = "/dev/tty1" ] && ! ps -e | grep -qw Xorg &&\
startx "$XDG_CONFIG_HOME/xinitrc"

sudo loadkeys ~/.config/keys.map
