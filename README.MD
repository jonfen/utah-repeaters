## Requirements

```bash
$ sudo apt -y install snapd git
$ snap install code-insiders --classic
$ git config --global core.editor "code-insiders --wait"
$ git config --global difftool.vscode.cmd 'code-insiders --wait --diff $LOCAL $REMOTE'
```

## Linux

```bash
$ ./setup-virtual-env.sh
$ code-insiders .
```
F5
```bash
$ xdg-open utah_repeaters.xlsx
```
## References
* http://utahvhfs.org/rptr.html