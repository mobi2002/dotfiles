#!/bin/sh

# some environment variables for gui applications (gtk2) are supposed to be sourced in X so I source my profile from here
[ -f ~/.profile ] && . ~/.profile

exec bspwm
