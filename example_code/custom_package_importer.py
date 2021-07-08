
'''
Add directory so that the pm4pymdl package will be imported from local repository (not site-packages)
'''
def apply():
    
    import os 
    print("os: ",os.getcwd())
    import sys
    sys.path.append(os.getcwd())
    print("sys:",r"\n".join(sys.path))