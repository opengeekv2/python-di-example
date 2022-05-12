import todo._infrastructure
from todo.core import right_ports

def main(run = right_ports.run):
    run()

if __name__ == '__main__':
    main()