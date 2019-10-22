<?php

  function f(& $x) {
     print('inside func' . $x);
     $x = 21;
     print('inside func' . $x);
  }
  $y = 10;
  print('outside func' . $y);
  f($y);
  print('outside func' . $y);
?>
