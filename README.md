# GSSU
Simple Server Utility in Python (submission for the GNU project, hence the "G") {not submitted to FSF yet, but I know for a fact it'll probably be rejected.}

GSSU is a simple-yet-powerful server utility written in Python for portability. It can be used to sniff traffic on a particular port, good for diagnosing several issues. It only uses libraries provided in the Python STDLIB (standard library/libraries already installed on Python by default) which means that compatibility should be good for Windows, Mac, Linux and BSD alike unless there are some sorts of privilege-strict things going on.

Usage (Linux, SELinux or AppArmor may conflict in some ways, please report if they do):
```
git clone https://https://github.com/xTrayambak/GSSU.git
cd GSSU
python3 main.py <youraddr> <yourport> <verbose> <buffer_size>
```

Usage (Microsoft Windows, may need to launch terminal as administrator):
```
git clone https://github.com/xTrayambak/GSSU.git
cd GSSU
py main.py <youraddr> <yourport> <verbose> <buffer_size>
```

_________
Issues, bugs, QOL changes, vulnerabilities must be reported in the issues tab.
