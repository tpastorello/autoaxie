# AUTOXIE SLP MINER
# Axie Infinity Auto Player

## P0W3R3D B1
# V1NT3UM

# COMPILE TO DIST
- python -OO -m py_compile <your program.py>

# INSTALLATION 
## NOTE: For python2 use 'pip'
- apt-get install python3.7 python3.7-dev python3-pip  python3-tk python3-dev
- pip3 install --upgrade setuptools pip
- pip3 install pyautogui
- pip3 install requests
- pip3 install opencv-python-headless

# CONFIGURATION
- choose a name for your axie team. the name must not contain spaces, accents or special characters. ex: myteam
- create a folder on path '/src/screen/teams' called 'myteam'
- print your cards in order of importance

# EXECUTE

<team> your team name, ex. myteam
<levels> = lunacia ruin levels, separeted by comma: 1,3,4,6 - the level is chosen randomly

- python autoxie.py <team> <levels>

## OR
- Prefer to use the trigger 'autoxie.sh' to start the service, as it holds the command inside a loop and will restart the python script in case there are crash. Thanks to Renan for first 'alien.sh'

#V0.1.0

<!--
ADD IN BASHRC

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
 }
 export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "

 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
 -->
