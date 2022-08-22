# HelloWorld

A very simple repository for my tests on [Senko](https://github.com/RangerDigital/senko).

I have forked [release 2.0.4 of Senko](https://github.com/RangerDigital/senko/releases/tag/v2.0.4) to avoid `u***` packages, in order to use a regular Python distribution.

It's mainly a Linux systemd service to be executed on a Rapsberry Pi (to represent the target that receive OTA updates).

## From a Raspberry Pi

- `cd /home/pi`
- `git clone https://github.com/Bktero/HelloWithSenko.git`
- `cd HelloWithSenko`
- `sudo cp hello_with_senko.service /etc/systemd/system`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable hello_with_senko`
- `sudo systemctl start hello_with_senko`
- `sudo journalctl -u hello_* -b 0 -f`

## From a computer

- Change `boot.py` or `hello.py`
- Commit and push to GitHub
- You should see the changes on the Raspberry Pi (this may take several minutes)