#!/usr/bin/env python
import sys, glob

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from HelloThrift import HelloThrift
from HelloThrift.ttypes import *

try:

  # Make socket
  tsocket = TSocket.TSocket('localhost', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(tsocket)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = HelloThrift.Client(protocol)

  # Connect!
  transport.open()

  print("hello")
  print(client.getData("hello"))
  # Close!
  transport.close()

except Thrift.TException, tx:
  print '%s' % (tx.message)

