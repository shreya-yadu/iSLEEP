
from enum import Enum
from struct import Struct
from util import dp

msg_fmt = Struct(">69B")
fields = ('type', 'class', 'group', 'topic', 'src', 'data')

def unpack_msg(data):
  """Unpack a message into a field dictionary

  >>> from Message import *
  >>> msg = bytearray([1, 2, 46, 2, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4])
  >>> c = {'type': mtype.SUBSCRIBE, 'class': ftype.SLEEP,'group': 46,'topic': 2, 'src': 7,'data': bytearray(b'\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x05\x01\x02\x03\x04')}
  >>> d2 = unpack_msg(msg)
  >>> [k for k in c if c[k] != d2[k]]
  []

  """

  if len(data) != msg_fmt.size:  #check length if its within the 69 bytes
    dp("Data size does not match size of struct")
  msg_dict = {}  #define empty dictionary
  i = 0
  for f in fields: #check types etc, loop through all fields
    if f != 'data': #check until type is not data
      msg_dict[f] = data[i]   #msg_dict of f is equal to data of i
      i += 1 #increment i
  msg_dict['data'] = data[i:] # transfer value of data from i till the end
  msg_dict['type'] = mtype(msg_dict['type'])  #assign value of type and class from mytpe and ftype
  msg_dict['class'] = ftype(msg_dict['class'])
  return msg_dict

def pack_msg(msg_dict): #pack a message
  """Pack a message dictionary into structure

  msg = bytearray([1, 2, 46, 2, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3, 4])
  c = unpack_msg(msg)
  >>> msg == pack_msg(c)
  True

  """
  #set values to all fields, getting values from the dictionary corresposing to the field names.
  for item in fields:
    assert item in msg_dict, "Missing field"  #checks if all the field in msg_dict exist, if they dont throw an exception.
  m_type = msg_dict["type"].value #assigning respective values
  m_class = msg_dict["class"].value
  m_group = int(msg_dict["group"])
  m_topic = int(msg_dict["topic"])
  m_src = int(msg_dict["src"])
  m_data = msg_dict["data"]
  m = bytearray([m_type, m_class, m_group, m_topic, m_src]) #creating a byte array from them
  m += m_data
  return m
  # and return value.

#defining class ftype
class ftype(Enum):
  """Format type is the same as the topic in this project"""
  TEMP = 0
  ACCEL = 1
  SLEEP = 2
  LED = 3


#defining class mytpe
class mtype(Enum):
  """Message type field"""
  PUBLISH = 0
  SUBSCRIBE = 1
  ENTER = 2
  LEAVE = 3


