# Exit Screen for i3

This is a simple and hacky exit screen for i3wm that allows quick access
to shutdown, reboot, suspend, lock or logout of your system.

## Usage

### Run Directly
```bash
$ ./exit-screen.py
```
or
```bash
$ ./exit-screen.sh
```

### Add to i3 Config
```
bindsym $mod+p exec bash $HOME/Scripts/power.sh
for_window [title="Exit Screen"] floating enable
```

## Shortcuts
When the screen is toggled, you may use the following shortcuts:
```
(s) Shutdown
(q) Log Off
(l) Lock Screen
(h) Suspend
(r) Reboot
```