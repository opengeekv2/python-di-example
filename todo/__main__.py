from ._infrastructure._services import *
from bite_di import inject

@inject
def main(run):
    run()

if __name__ == '__main__':
    main()