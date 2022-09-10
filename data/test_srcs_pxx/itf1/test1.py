
import ctypes
import pathlib

class Player:

  lib_path = str(pathlib.Path(__file__).parent.parent / "build/libprojectx.so")
  Player = ctypes.cdll.LoadLibrary(lib_path)


  def __init__(self):
    self.this_ = None

  def construct_object_0(self, ):
    self.this_ = Player.Player._Player_construct_0__()

  def construct_object_1(self, a, b):
    self.this_ = Player.Player._Player_construct_1__(a, b)

  def alive(self):
    return Player.Player._Player_alive__(self.this_)

  def make_mana(self):
    Player.Player._Player_make_mana__(self.this_)

  def set_life_points(self, life_points):
    Player.Player._Player_set_life_points__ (self.this_, life_points)

  def get_life_points(self):
    return Player.Player._Player_get_life_points__(self.this_)

  def set_mana(self, mana):
    Player.Player._Player_set_mana__ (self.this_, mana)

  def get_mana(self):
    return Player.Player._Player_get_mana__(self.this_)

  def __del__(self):
    Player.Player._delete_Player__(self.this_)



if __name__ == "__main__":
  # magic happens here
  pass
