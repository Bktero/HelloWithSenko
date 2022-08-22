# HelloWorld

A very simple repository for my tests on [Senko](https://github.com/RangerDigital/senko).

I have forked [release 2.0.4 of Senko](https://github.com/RangerDigital/senko/releases/tag/v2.0.4) to avoid `u***` packages, in order to use a regular Python distribution.

## On a Raspberry Pi

- Ih `/home/pi`, `git clone https://github.com/Bktero/HelloWithSenko.git`
- Copy `hello_with_senko.service` to `/etc/systemd/system`
- `systemctl daemon-reload`
- `systemctl enable hello_with_senko`
- `systemctl start hello_with_senko`
- `systemctl -u hello_* -b 0 -f`
