with open("requirements.txt", 'r') as f:
    lines = f.readlines()


a = open("requirements_conda.txt", 'w')
b = open("requirements_pip.txt", 'w')
for line in lines:
    if "pypi_0" in line:
        s = line.split('=')
        b.write(f"{s[0]}=={s[1]}\n")
        # a.write('\n')
    else:
        a.write(line)
        # b.write('\n')
