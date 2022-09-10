
import ctypes
import pathlib

class Myclass2:

  lib_path = str(pathlib.Path(__file__).parent.parent / "build/libprojectx.so")
  Myclass2 = ctypes.cdll.LoadLibrary(lib_path)


  def __init__(self):
    self.this_ = None

  def construct_object_0(self, ):
    self.this_ = Myclass2.Myclass2._Myclass2_construct_0__()

  def construct_object_1(self, a, b):
    self.this_ = Myclass2.Myclass2._Myclass2_construct_1__(a, b)

  def set_a2(self, a2):
    Myclass2.Myclass2._Myclass2_set_a2__ (self.this_, a2)

  def get_a2(self):
    return Myclass2.Myclass2._Myclass2_get_a2__(self.this_)

  def set_c3(self, c3):
    Myclass2.Myclass2._Myclass2_set_c3__ (self.this_, c3)

  def get_c3(self):
    return Myclass2.Myclass2._Myclass2_get_c3__(self.this_)

  def __del__(self):
    Myclass2.Myclass2._delete_Myclass2__(self.this_)



if __name__ == "__main__":
  # magic happens here
  pass
