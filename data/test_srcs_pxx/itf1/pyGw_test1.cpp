#include <iostream>
#include "test1.h"

namespace mymodule {

namespace test_unders {

extern "C" {

Player * _Player_construct_0__() {
  return new Player();
}

Player * _Player_construct_1__(const int& a, const int& b) {
  return new Player(a, b);
}

const bool _Player_alive__(Player *self) {
  return self->alive();
}

void _Player_make_mana__(Player *self) {
  self->make_mana();
}

void _Player_set_life_points__(Player *self, int life_points) {
  self->set_life_points (life_points);
}

int _Player_get_life_points__(Player *self) {
  return self->get_life_points() ;
}

void _Player_set_mana__(Player *self, int mana) {
  self->set_mana (mana);
}

int _Player_get_mana__(Player *self) {
  return self->get_mana() ;
}

void _delete_Player__(Player *self) {
  delete self;
}


}

} // namespace mymodule

} // namespace test_unders

