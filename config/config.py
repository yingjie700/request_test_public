from configparser import ConfigParser
cp=ConfigParser()
cp.read("config.ini")

section=cp.sections()[0]
print(section)

print(cp.options(section))
#得到该section的所有键值对
print(cp.items(section))

