from cx_Freeze import setup, Executable

base = None


executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "PassHash",
    options = options,
    version = "1.0",
    description = 'Simple MD5/SHA-1 calculator.',
    executables = executables
)
