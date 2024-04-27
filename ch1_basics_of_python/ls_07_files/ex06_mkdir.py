import os
import shutil
from pathlib import Path


# # # os.makedirs('ex06_dir/bin')
# # Path('ex06_dir/path1').mkdir(parents=True, exist_ok=True)
# Path('ex06_dir/bin/path2').mkdir(parents=True, exist_ok=True)

# os.rmdir('ex06_dir')
# Path('ex06_dir').rmdir()

# shutil.rmtree('ex06_dir/bin')


print(os.listdir())
p = Path(Path.cwd())
for obj in p.iterdir():
    print(f'name={obj.name:<30}, anchor={obj.anchor:<10}, suffix={obj.suffix:<10}, dir={obj.is_dir():<15}')


for dir_path, dir_names, file_names in os.walk(Path.cwd()):
    print(f'dir_path={dir_path}, dir_names={dir_names}, file_names={file_names}')

