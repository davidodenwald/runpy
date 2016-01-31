# runpy

 A simple script that executes a given script everytime it's changed.

## Dependencies

python3.x

## Installation

Clone the git repo
```
git clone https://github.com/davidodenwald/runpy.git
```

Make runpy executable
```
cd runpy

chmod +x runpy
```

Move the file so it is in $PATH
```
sudo mv runpy /usr/local/bin/
```

## Usage

### Start runpy

```
runpy python3 script.py
```
This will run the file `script.py` everytime you make a change to it.

```
runpy python3 test.py script.py
```
This will run the file `test.py` everytime you make a change to the file `script.py`.

#### Stop runpy

`Ctr-c` to stop runpy
