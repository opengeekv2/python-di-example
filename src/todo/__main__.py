from ._services import *
from .di import inject

@inject
def main(run):
    run()

if __name__ == '__main__':
    main()