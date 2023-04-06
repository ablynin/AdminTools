# -*- mode: python -*-
import os
import shutil

block_cipher = None
progname = 'AdminTools'
version = '1.1'


a = Analysis([fr'Z:\Python Projects\{progname}\{progname}.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=['add_lib.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          icon=fr'source\{progname}.ico',
          exclude_binaries=True,
          name=progname,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=f'{progname}_{version}')

path = f'dist\{progname}_{version}'
tgt = 'lib'
src = 'source'
exclude = ['base_library.zip', 'python36.dll', f'{progname}.exe']
os.makedirs(os.path.join(path, tgt))
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
for file in files:
    if file not in exclude:
        os.rename(os.path.join(path, file), os.path.join(path, tgt, file))
shutil.copytree(src, os.path.join(path, src), ignore=shutil.ignore_patterns('*.ts'))