#!/usr/bin/python3

def print_func(par):
  print("Hello : ", par)
  return


def test(par):
  if __name__ == '__main__':
    print('程序自身在运行')
  else:
    print('我来自另一模块')
  print("test : ", par)
  return

# test('haha')
