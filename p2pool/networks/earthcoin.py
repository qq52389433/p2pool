#coding=utf-8
from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other
# CHAIN_LENGTH =客户端保留的份额数
# REAL_CHAIN_LENGTH =客户用于计算支出的最大份额
# REAL_CHAIN_LENGTH必须始终为<= CHAIN_LENGTH
# REAL_CHAIN_LENGTH 必须与所有其他客户端同步更改
# 更改可以通过更改一个，然后另一个来完成

PARENT = networks.nets['earthcoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'fc70035c7a81bc6f'.decode('hex')
PREFIX = '2472ef181efcd37b'.decode('hex')
P2P_PORT = 9333
# 难度设置
MIN_TARGET = 0
#MAX_TARGET = 2**256//2**32 - 1
MAX_TARGET = 1000 #2**48//2**32 - 1
# shares 下载开关,当有其他节点一直在打开的时候，可以开启
PERSIST = False 
WORKER_PORT = 9332
BOOTSTRAP_ADDRS = '148.163.168.167'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 100000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
