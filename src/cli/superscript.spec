# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['superscript.py'],
             pathex=['/workspaces/tra-data-analysis/src'],
             binaries=[],
             datas=[],
             hiddenimports=[
                 "dnspython", 
                 "sklearn.utils._weight_vector",
                 "requests",
                 "websockets.legacy",
                 "websockets.legacy.server",
             ],
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
          [('W ignore', None, 'OPTION')],
          name='superscript',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
