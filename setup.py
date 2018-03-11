from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["hashlib", "sys"], excludes = [], include_files = ["Softies-icons-lock_256px.png"])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base)
]

setup(
    name='PassHash',
    version = '1.0',
    description = 'A Simple MD5/SHA1 Program',
    options = dict(build_exe = buildOptions),
    executables = executables
)