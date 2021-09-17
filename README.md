# AUTOXIE

# Axie Infinity Auto Player

# V1NT3UM
- Time Machine! 
# COMPILE TO DIST
- python -OO -m py_compile <your program.py>
# INSTALLATION
- apt-get install python3.7 python3.7-dev python3-pip  python3-tk python3-dev
- pip3 install --upgrade setuptools pip
- pip3 install pyautogui
- pip3 install requests
- pip3 install opencv-python-headless
- NOTE: For python2 use 'pip'

# EXECUTE
- python dehumanizer.py <confidence> <browser>
## OR
- Prefer to use the trigger 'dehumanizer.sh' to start the service, as it holds the command inside a loop and will restart the python script in case there are crash. Thanks to Renan for first 'alien.sh'

#V0.7.0

<!--
ADD IN BASHRC

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
 }
 export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
 -->