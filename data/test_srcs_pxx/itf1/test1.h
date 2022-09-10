#pragma once

#include <iostream>

namespace mymodule {

namespace test_unders {


// No class documentation was specified
class Player  {

public:
  // No documentation specified
  Player ();

  // No documentation specified
  Player (const int& a, const int& b);

  // No documentation specified
  ~Player ();

public:
  // No documentation specified
  const bool alive ();

  // No documentation specified
  void make_mana ();


  void set_life_points (int t_life_points);
  int get_life_points() ;

  void set_mana (int t_mana);
  int get_mana() ;

private:
  // No documentation specified
  int life_points;

  // No documentation specified
  int mana;


} ;

} // namespace mymodule

} // namespace test_unders

