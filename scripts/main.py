
import src.mypkg as mypkg
from src.mypkg import separate_funcs

if __name__ == '__main__':
    
    # functions in root package namespace
    so = mypkg.SmallType()
    bo = mypkg.BigType()

    # functions in submodule namespace
    mypkg.submodule.my_submodfunc()
    
    # functions in separate_funcs namespace, imported separately
    separate_funcs.separate_func1()

