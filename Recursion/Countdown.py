def cuenta(n):
  print(n)
  if n == 0:
    return 0
  else:
    return cuenta(n - 1)

import Countdown
Countdown.cuenta(5)