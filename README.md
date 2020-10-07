# i3statusTasks
An extension for i3status that keeps track of tasks you need to do for the day

# Installation

## Copying the files
Simply make a dir named `~/bin/` and clone `i3statusTasks` to it.
```bash
mkdir ~/bin
cd ~/bin
git clone git@github.com:RyanTheNerd/i3statusTasks.git
```

## Adding to path:
To add to path, simply append this line to the end of `~/.profile`:

`export PATH=$PATH:/home/$(whoami)/bin:/home/$(whoami)/bin/i3statusTasks`

## Configuring i3:
In the file `~/.i3/config`, simply find the line starting with `status_command i3status` and change it to `status_command i3status | i3status.py`.


You have now successfully have installed i3statusTasks. Now simply log out and log back in, and you should have your tasks listed on i3bar.
