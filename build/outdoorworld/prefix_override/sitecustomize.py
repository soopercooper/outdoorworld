import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/crolson1/Desktop/outdoorworld/install/outdoorworld'
