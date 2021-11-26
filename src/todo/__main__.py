from ._services import *
from .inject import inject

@inject
def main(run):
    run()

if __name__ == '__main__':
    main()