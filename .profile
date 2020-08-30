## ~/.profile

# source bashrc if running bash
[ -n "$BASH_VERSION" ] && [ -f "$HOME/.bashrc" ] && . "$HOME/.bashrc"

# add local bin directory and all subdirectories to path
export PATH=$(find "$HOME/.local/bin" -type d | tr '\n' ':')$PATH

# default programs
export EDITOR="nvim"
export VISUAL="nvim"
export TERMINAL="alacritty"
#export BROWSER="firefox"

# development
export MAKEFLAGS="-j5"

# XDG Base Directory structure
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"

# clean up home folder
#export XAUTHORITY="$XDG_RUNTIME_DIR/Xauthority"
export LESSHISTFILE="-"
export TERMINFO="$XDG_DATA_HOME/terminfo"
export TERMINFO_DIRS="$XDG_DATA_HOME/terminfo:/usr/share/terminfo"
export PYTHONSTARTUP="$XDG_CONFIG_HOME/pythonrc"
#export INPUTRC="$XDG_CONFIG_HOME/readline/inputrc"
export RXVT_SOCKET="$XDG_RUNTIME_DIR/urxvtd"
export GNUPGHOME="$XDG_DATA_HOME/gnupg"
export WGETRC="$XDG_CONFIG_HOME/wgetrc"
export GTK2_RC_FILES="$XDG_CONFIG_HOME/gtk-2.0/gtkrc"

# Qt5 theme
export QT_QPA_PLATFORMTHEME="qt5ct"

# default wine options
export WINEARCH="win32"
export WINEPREFIX="$HOME/.local/wine/default/"
export WINEDLLOVERRIDES="winemenubuilder.exe=d"
export WINEDEBUG=-all # this is here because it supposedly increase the speed as wine don't need to print log to stdout (which is not required when running from launcher...) so unset it when installing a program for better troubleshooting.

# start X server if on tty1 and X server not already running
#[ "$(tty)" = "/dev/tty1" ] && ! ps -e | grep -qw Xorg &&\
#startx
