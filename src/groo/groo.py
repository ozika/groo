def get_root(rootfile, timelim=10):
    import os 
    from pathlib import Path
    import time
    start = time.time()
    d = Path(os.getcwd())
    found = 0   
    while (found != 1) & ((time.time()-start) < float(timelim)):
        if os.path.isfile(os.path.join(d, rootfile)):
            found=1
        else:
            for root, dir, files in os.walk(d):
                #print(root)
                if rootfile in files:
                    found = 1 
                    d = root
            if found == 0:
                d=d.parent
    if found == 0:
        print("Root file not found in the time limit ("+str(timelim)+"s)\nIncrease time lim by providing timelim=XX argument")
    return d


#print(get_root("screening_survey_neurocode.lss", timelim=5))
    


