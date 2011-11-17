import os

tomatoes_dir = os.path.join(os.path.expanduser('~'), ".pomotimer")
tomatoes_data = os.path.join(tomatoes_dir, "data.fs")
global_assets_dir = os.path.join('/', 'usr', 'share', 'pomotimer', 'assets')

if os.path.exists('assets'):
  assets_dir = 'assets'
else:
  assets_dir = global_assets_dir
