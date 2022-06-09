def get_root(rootfile):
    import os 
    from pathlib import Path
    d = Path(os.getcwd())
    found = 0
    while found == 0:
        if os.path.isfile(os.path.join(d, rootfile)):
            found = 1
        else:
            d=d.parent
    
    return d
