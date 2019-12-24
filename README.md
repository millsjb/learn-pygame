# learn-pygame
> This beginner project serves as a playground to learn and build with pygame



## Setup
In order to run locally..

create the python virtual environment
```sh
$ python3 -m venv env
```

clone the project
```sh
$ git clone <projecturl>
```

activate the python virtual environment
```sh
$ source env/bin/activate
```

verify that python 3.6.8 is installed
```sh
$ python --version
```

verify that pip is installed
```sh
$ pip --version
```

install all dependencies using pip
```sh
$ pip install -r requirements
```

### Possible extra setup
For WSL users..

run bash command before executing game to allow GUI window to open in Windows 10
```sh
$ export DISPLAY=:0
```

set up ALSA for sound
```sh
$ 
```

(if using ssh) activate ssh-agent to use git within vs code
```sh
$ eval $(keychain --eval ~/.ssh/git)
```
