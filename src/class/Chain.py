#链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, s):
        return Chain('%s/%s' % (self._path, s))

    def __str__(self):
        return self._path

str = Chain().status.user.timeline.list

print(str)

str = Chain().users('michael').repos

print(str)
