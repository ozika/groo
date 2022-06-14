> "Groo, the calling of the home (directory)."

 

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


