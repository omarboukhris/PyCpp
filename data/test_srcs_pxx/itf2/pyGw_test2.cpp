#include <iostream>
#include "../itf1/test1.h"
#include "test2.h"

namespace mymodule {

namespace test2 {

extern "C" {

Myclass2 * _Myclass2_construct_0__() {
  return new Myclass2();
}

Myclass2 * _Myclass2_construct_1__(const int a, const mymodulconste::Player<T1, T2<V1, int&**, V3<std::string, int, temp<int>>>> b) {
  return new Myclass2(a, b);
}

void _Myclass2_set_a2__(Myclass2 *self, ns::int*&**&* a2) {
  self->set_a2 (a2);
}

ns::int*&**&* _Myclass2_get_a2__(Myclass2 *self) {
  return self->get_a2() ;
}

void _Myclass2_set_c3__(Myclass2 *self, float c3) {
  self->set_c3 (c3);
}

float _Myclass2_get_c3__(Myclass2 *self) {
  return self->get_c3() ;
}

void _delete_Myclass2__(Myclass2 *self) {
  delete self;
}


}

} // namespace mymodule

} // namespace test2

