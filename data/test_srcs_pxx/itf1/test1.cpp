#include <iostream>
#include "test1.h"

namespace mymodule {

namespace test_unders {

Player::Player () {  
     life_points = 0;
     mana = 0;
   }

Player::Player (const int& a, const int& b) {  
        life_points = a;
        mana = b;
   }

Player::~Player () {}

const bool Player::alive () {  
     return (life_points > 0);
}

void Player::make_mana () {  
     mana++;
}

void Player::set_life_points(int t_life_points) {
  life_points = t_life_points;
}
int Player::get_life_points() {
  return life_points ;
}

void Player::set_mana(int t_mana) {
  mana = t_mana;
}
int Player::get_mana() {
  return mana ;
}

} // namespace mymodule

} // namespace test_unders

