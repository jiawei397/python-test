class Test:
  i = 123

  def __init__(self, name):
    print('init', self)
    self.name = name
    self.run()

  def run(self):
    print('run')


a = Test('hahah')
print(a.i)
# a.run()
print(a.name)

