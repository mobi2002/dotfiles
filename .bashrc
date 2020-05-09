#
# ~/.bashrc
#
# If not running interactively, don't do anything

[[ $- != *i* ]] && return

# Aliases to make my life easier
alias ls='ls -F --color=auto' ## list unhidden files
alias ll='ls -lshF --color=auto' ## list unhidden files in list form
alias la='ls -AF --color=auto' ## list all files
alias lla="ls -lAshF --color=auto" ## list all files in list form
alias grep='grep -i --color=auto'
alias cd..='cd ..'
alias mv='mv -iv' ## verbose output + confirmation
alias rm='rm -Iv --one-file-system' ## verbose output + confirmation
alias sudo='sudo ' ## to make aliases work with sudo
alias cp='cp -iv' ## verbose output + confirmation
alias df='df -h' ## output in megabytes
alias diff='diff --color=auto'
alias poweroff='sudo poweroff'
alias reboot='sudo reboot'
alias vifm='vifmrun'
alias config='/usr/bin/git --git-dir=$HOME/.local/dotfiles.git/ --work-tree=$HOME' ## command to manage my dotfiles

# Customize default shell behaviour
shopt -s autocd ## To do 'cd directory' without typing 'cd directory' and only typing 'directory'
shopt -s cdspell ## To atomatically correct directory path if minor error exists
shopt -s no_empty_cmd_completion ## To not search completion in $PATH when attempted with empty line
shopt -s histappend ## To append history to 'HISTFILE' rather than overwriting it
shopt -s checkwinsize
HISTCONTROL=ignoreboth ## don't put duplicate lines or lines starting with space in the history

# My prompt customization
PS1='\[\033[01;36m\]\u\[\033[01;37m\]@\[\033[01;32m\]\h:\[\033[01;34m\]\w\[\033[00m\]\$ '

c() {
	path="$(find ~/{.config/,.local/} -type d -name "icons" -prune -o -type d -name "wine" -prune -o  -type f -print ; find ~/ -maxdepth 1 -type f -name ".*")"
	file="$(echo $path | sed 's/\ /\n/g' | fzf)"
	[ -z $file ] || env $EDITOR $file
	unset path file
}

EC() {
	echo -e '\e[1;33m'exit code: $?'\e[m'
}
trap EC ERR

# command not found provided by pkgfile package
source /usr/share/doc/pkgfile/command-not-found.bash
