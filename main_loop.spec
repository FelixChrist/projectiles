# -*- mode: python -*-
a = Analysis(['main_loop.py', 'projectile.py', 'question.py', 'slider.py', 'eztext.py'],
             pathex=['/home/felix/Documents/Projectiles'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main_loop',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='main_loop')
