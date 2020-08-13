# internet-speed-monitor
Is your internet as garbage as mine? Are you beholden to throttling by evil 
monopolistic ISPs such as Spectrum? Would you like to try to track how your 
internet speed fluctuates throughout the day? You've come to the right place. 
This repo contains a script to monitor and log broadband speed. I am using it 
on a Raspberry Pi, but you could really run it anywhere.

## Setup
Create a directory for the project and clone the repo:
```
mkdir /home/[user]/internet-speed-monitor
cd /home/[user]/internet-speed-monitor
git clone https://github.com/nathanielrindlaub/internet-speed-monitor.git
```

Create a virtual environment and activate it from the project root directory 
(`/home/[user]/internet-speed-monitor`):
```
pip install virtualenv
virtualenv env -p python3
source env/bin/activate
```

CD into the git repo and Install dependencies and deactivate the virtual env:
```
cd internet-speed-monitor
pip install -r requirements.txt
deactivate
```

Create cronjob by opening up chrontab:
```
crontab -e
```
And save the following line (don't forget to add your own project root). This 
will run the script every half hour.
```
0,30 * * * * cd [path-to-project-root]/internet-speed-monitor/internet-speed-monitor && /usr/bin/python3 speedtest.py
```