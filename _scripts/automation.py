import subprocess

def remove_lines(fn, s, e):
    string = ""
    f = open(fn, 'r+')
    l = list(f)
    string = "".join(l[0:s]) + "".join(l[e:])
    f.seek(0)
    f.write(string)
    f.truncate()
    f.close()

def replace_lines(fn, s, e, txt):
    string = ""
    f = open(fn, 'r+')
    l = list(f)
    string = "".join(l[0:s]) + txt + "".join(l[e:])
    f.seek(0)
    f.write(string)
    f.truncate()
    f.close()

def append(fn, txt):
    f = open(fn, 'a')
    f.write(txt)
    f.close()

def run(cmds):
    p = subprocess.Popen(cmds, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()
    #return value 0 if successful 1 if fail exit status
    return retval
