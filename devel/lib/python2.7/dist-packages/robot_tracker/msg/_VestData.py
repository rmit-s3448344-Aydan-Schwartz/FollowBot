# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_tracker/VestData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VestData(genpy.Message):
  _md5sum = "009a90b705b09d3266a4baee5469658e"
  _type = "robot_tracker/VestData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 x_center
float32 y_center
float32 area
float32 rotation_angle
float32 cam_height
float32 cam_width
"""
  __slots__ = ['x_center','y_center','area','rotation_angle','cam_height','cam_width']
  _slot_types = ['float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_center,y_center,area,rotation_angle,cam_height,cam_width

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VestData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x_center is None:
        self.x_center = 0.
      if self.y_center is None:
        self.y_center = 0.
      if self.area is None:
        self.area = 0.
      if self.rotation_angle is None:
        self.rotation_angle = 0.
      if self.cam_height is None:
        self.cam_height = 0.
      if self.cam_width is None:
        self.cam_width = 0.
    else:
      self.x_center = 0.
      self.y_center = 0.
      self.area = 0.
      self.rotation_angle = 0.
      self.cam_height = 0.
      self.cam_width = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.x_center, _x.y_center, _x.area, _x.rotation_angle, _x.cam_height, _x.cam_width))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.x_center, _x.y_center, _x.area, _x.rotation_angle, _x.cam_height, _x.cam_width,) = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.x_center, _x.y_center, _x.area, _x.rotation_angle, _x.cam_height, _x.cam_width))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.x_center, _x.y_center, _x.area, _x.rotation_angle, _x.cam_height, _x.cam_width,) = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6f = None
def _get_struct_6f():
    global _struct_6f
    if _struct_6f is None:
        _struct_6f = struct.Struct("<6f")
    return _struct_6f
