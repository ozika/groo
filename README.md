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
**New in version 0.0.7** 
Previous versions of `groo` only move up, that is, they look for the root file in the current folder, if it's not found then the search moves one folder up. However, this means that if the root file is anywhere *but* on the upward trajectory then it wouldn't be found. 

<img src="https://raw.githubusercontent.com/ozika/groo/main/src/groo/v007_upd.png" width=400>

---
Logo by [AbtoCreative](https://www.flaticon.com/authors/abtocreative) :heart:
