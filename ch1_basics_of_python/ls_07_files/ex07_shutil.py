import shutil

shutil.copy('ex04.txt', 'ex06_dir/ex04_copy.txt')
# копирование с метеоданными
shutil.copy2('ex04.txt', 'ex06_dir/ex04_copy2.txt')
# shutil.rmtree('ex06_dir')
