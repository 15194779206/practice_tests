import os
import sys

Data_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Data_dir)

from core import main
# from database import data_cre
if __name__ == '__main__':
    main.run()
