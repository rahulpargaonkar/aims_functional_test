from invoke import task
import subprocess

@task
def test(c,specname=''):
    process=subprocess.Popen("gauge run specs/"+specname,shell=True)
    output, error = process.communicate()
    print (output)