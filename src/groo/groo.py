def get_root(rootfile, timelim=10, verbose=False):
    import os 
    from pathlib import Path
    import time
    start = time.time()
    d = Path(os.getcwd())
    found = 0   
    # Quick search termination conditions
    # 1/ the path has been found
    # 2/ time limite 1s runs out 
    # 3/ the search has root the upper-most directory
    while (found == 0) &  (float(time.time()-start)<float(1)) & (str(d)!="/"):
        if verbose: 
            print("Quick search: " + str(d))
        if os.path.isfile(os.path.join(d, rootfile)):
            found = 1
        else:
            d=d.parent
    if found==0:
        d = Path(os.getcwd())
        if verbose: 
            print("Switch to full tree search")
        while (found != 1) & ((time.time()-start) < float(timelim)):
            if os.path.isfile(os.path.join(d, rootfile)):
                found=1
            else:
                for root, dir, files in os.walk(d):
                    if verbose: 
                        print("Full search: " + str(root))
                    if rootfile in files:
                        found = 1 
                        d = root
                if found == 0:
                    d=d.parent
        if found == 0:
            print("Root file not found in the time limit ("+str(timelim)+"s)\nIncrease time lim by providing timelim=XX argument")
    return d


    


