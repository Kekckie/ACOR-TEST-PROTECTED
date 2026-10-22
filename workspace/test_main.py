from main import double
for value in (0, 2, -3, 10):
    assert double(value) == value + value
print('NATIVE_RUNNER_OK')
