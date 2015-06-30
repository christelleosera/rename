import os
import sys

print "Current directory is: %s" % os.getcwd()
print 'Replacing "%s" with "%s" in filenames' % (sys.argv[1], sys.argv[2])


[os.rename(f, f.replace(sys.argv[1], sys.argv[2])) for f in os.listdir('.') if not f.startswith('.')]