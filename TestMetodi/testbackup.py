import os
import glob
import time
import shutil


def main():
    appPath = '/etc/appName'
    date = str(int(time.time()))

    folders = glob.glob('staging/*')
    latest = max([int(v.split('/')[1]) for v in folders])
    basePath = [v for v in folders if str(latest) in v][0]

    # Backup
    try:
        os.mkdir('bak')
    except:
        pass
    os.mkdir('bak/%s' % (date))
    shutil.copytree('%s/api' % (appPath), 'bak/%s/api' % (date))

    # Remove
    shutil.rmtree('%s/api' % (appPath))

    # Copy
    shutil.copytree(basePath, '%s/api' % (appPath))


if __name__ == '__main__':
    main()
