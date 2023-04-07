import sys
import os


sys.path.append(os.path.join(os.getcwd(), 'lib'))
# noinspection PyProtectedMember,PyUnresolvedReferences
sys._MEIPASS = os.path.join(sys._MEIPASS, 'lib')
