#!/bin/bash
export PYENV_ROOT="$HOME/.pyenv"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PATH="$HOME/.poetry/bin:$HOME/Library/Caches/pypoetry/virtualenvs/internet-speedtest-dDhD3n-b-py3.8/bin:$PATH"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

poetry run python speedtest_logger.py -d $DIR
