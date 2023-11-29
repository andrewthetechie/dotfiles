#!/bin/zsh

# gnuutils
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
PATH="$(brew --prefix)/opt/gawk/libexec/gnubin:$PATH"
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"