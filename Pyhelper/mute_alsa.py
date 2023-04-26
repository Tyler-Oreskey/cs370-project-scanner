import ctypes

# Module to supress uneeded ALSA warnings from the Pyaudio mudule.
# This moudle was geneourly provided by Eugene, and larsks from:
# https://stackoverflow.com/questions/36956083/how-can-the-terminal-output-of-executables-run-by-python-functions-be-silenced-i/36966379#36966379

ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int,
                                      ctypes.c_char_p, ctypes.c_int,
                                      ctypes.c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

try:
    asound = ctypes.cdll.LoadLibrary('libasound.so.2')
    asound.snd_lib_error_set_handler(c_error_handler)
except OSError:
    pass