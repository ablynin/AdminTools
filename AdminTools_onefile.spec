# -*- mode: python -*-
import os
import shutil

block_cipher = None
progname = 'AdminTools'


a = Analysis([fr'Z:\Python Projects\{progname}\{progname}.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
		  a.binaries,
          a.zipfiles,
          a.datas,
		  icon=r'source\AdminTools.ico',
          name='AdminTools',
          debug=False,
          strip=False,
          upx=True,
          console=False )

src = 'source'
tgt = 'dist'
shutil.copytree(src, os.path.join(tgt, src), ignore=shutil.ignore_patterns('*.ts'))