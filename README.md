<img src="https://raw.githubusercontent.com/ozika/groo/main/src/groo/logo.png" width=400>


This package simply finds the root of a project based on a filename.

**Usage**

1. Create a hidden file in the root directory of your project.

```bash
vim .my_hidden_root_file
```
**Tip:** Use project-specific name not a generic `.root` or even rely on `.git`. Get creative.

2. Install `groo`

```bash

pip install groo-ozika

```
**Tip:** use `conda` and make sure to activate the right environment to install into.

3. Import to your code and use


```python
from groo.groo import get_root
root_folder = get_root(".my_hidden_root_file")
```

**Tip:** Always use `os.path.join()` to declare paths. It will make your code run across platforms and you won't get any strange erorrs (e.g., extra `/`).

**Optional**
If you want to provide a time limit to the search for the root you can do so by using the `timelim` flag (in seconds). 
```python
root_folder = get_root(".my_hidden_root_file", timelim=10)
```

---

### Example usage

Let's say that wee want to keep all project-related files in a specific folder (which can be anywhere on your computer). Let's call this `project_folder`.

Then, within it we want to have some data `mydata.csv` in a `data` folder and some scripts in a `scripts` folder `runscript.py`.

To let `groo` identify the root folder we need to create a file there. I usually prefer to use a dot file because it will remain hidden, however, it can be anything. In this example we will create `.my_hidden_root_file` in the `project_folder`.

Once the hidden file is created, one might want to load it in their python script (or a jupyter ntbk). Here we want to load `data/mydata.csv` within the `scripts/runscript.py`.

To do that, we can use this example:
```python
from groo.groo import get_root
root_folder = get_root(".my_hidden_root_file")

import pandas as pd
df = pd.read_csv(os.path.join(root_folder, "data", "mydata.csv"))

```
Note that the same code will work for **any** script that is anywhere whithin the `project_folder`.

Enjoy!

## Release Notes
**New in version 0.1.0**  
1/ Fixed bug from 0.0.9  
2/ Added verbose option, if `verbose=True` groo will print out the directories that it's searching 

Added "quick search" which scans directories above in the hierarchy before performing a more comprehensive search.  

**New in version 0.0.9**

Added "quick search" which scans directories above in the hierarchy before performing a more comprehensive search.  

**New in version 0.0.8** 

Removed bug which was displaying path. 

**New in version 0.0.7** 
1. Previous versions of `groo` could only search for the root flag above in the directory hierarchy. Starting `0.0.7`, the flag can be in theory anywhere on the computer. The search algorithm starts from the location of the file and on each iteration moves a level up, performs a full search.
2. Since full search can sometimes be unpractical, `groo` now allows users to specify maximum time limit using the `timelim` flag `get_root(".my_hidden_root_file", timelim=10)`. 

<img src="https://github.com/ozika/groo/blob/main/src/groo/v007_upd.svg" width=600>

---
Logo by [AbtoCreative](https://www.flaticon.com/authors/abtocreative) :heart:
