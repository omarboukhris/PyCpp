#pragma once

#include <iostream>
#include "../itf1/test1.h"

namespace mymodule {

namespace test2 {


// No class documentation was specified
class Myclass2 : public mymodulconste::Player<T1, T2<V1, int&**, V3<std::string, int, temp<int>>>>, private otherClasdb, public XAz<T> {

public:
  /*!
  doc goes here
  */
  Myclass2 ();

  // No documentation specified
  Myclass2 (const int a, const mymodulconste::Player<T1, T2<V1, int&**, V3<std::string, int, temp<int>>>> b);

  // No documentation specified
  ~Myclass2 ();

  void set_a2 (ns::int*&**&* t_a2);
  ns::int*&**&* get_a2() ;

  void set_c3 (float t_c3);
  float get_c3() ;

private:
  /*! \brief attr doxy doc */
  ns::int*&**&* a2;

  // No documentation specified
  float c3;


} ;

} // namespace mymodule

} // namespace test2

