import subprocess
import conf

def spawn(args):
    return subprocess.Popen(args)

def launch_imgs(imgs):
    spawn([conf.PURE_REF] + imgs)