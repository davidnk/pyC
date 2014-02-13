import subprocess
import os


def runC(functions='', run='', imports=[]):
    prog = []
    for i in imports:
        prog.append("#include {}".format(i))
    prog.append(function)
    prog.append("int main() {")
    prog.append(run + ';')
    prog.append("return 0;}")
    with open("/tmp/tempC.c", "w") as c:
        c.write('\n'.join(prog))
    os.system("gcc /tmp/tempC.c -o /tmp/tempC.x")
    ret = subprocess.check_output("/tmp/tempC.x")
    os.system("rm /tmp/tempC.x /tmp/tempC.c")
    return ret
