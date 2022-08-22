# HelloWorld

A very simple repository for my tests on [Senko](https://github.com/RangerDigital/senko).

I have forked [release 2.0.4 of Senko](https://github.com/RangerDigital/senko/releases/tag/v2.0.4) to avoid `u***` packages, in order to use a regular Python distribution.

## On a Raspberry Pi

- Ih `/home/pi`, `git clone https://github.com/Bktero/HelloWithSenko.git`
- `cd HelloWithSenko`
- `sudo cp hello_with_senko.service /etc/systemd/system`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable hello_with_senko`
- `sudo systemctl start hello_with_senko`
- `sudo journalctl -u hello_* -b 0 -f`
