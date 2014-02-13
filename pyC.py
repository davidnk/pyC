import subprocess
import os


def runC(functions='', run='', imports=[]):
    prog = []
    for i in imports:
        prog.append("#include {}".format(i))
    prog.append(functions)
    prog.append("int main() {")
    prog.append(run + ';')
    prog.append("return 0;}")
    with open("__pyC_tempC.c", "w") as c:
        c.write('\n'.join(prog))
    os.system("gcc __pyC_tempC.c -o __pyC_tempC.x")
    ret = subprocess.check_output("./__pyC_tempC.x")
    os.system("rm __pyC_tempC.x __pyC_tempC.c")
    return ret
