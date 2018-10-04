import sys
import os
import zipfile
import pycurl

username = sys.argv[1]
password = sys.argv[2]
url = sys.argv[3]
folder = sys.argv[4]
# fo = open("foo.txt", "wb")
# fo.write(username+"\n"+password+"\n"+url+"\n"+folder)
# fo.close()
zipfilename = "%s.zip" % (folder.replace("/", "_"))
zfile = zipfile.ZipFile("channel.zip", 'w', zipfile.ZIP_DEFLATED)
rootlen = len(folder) + 1
for base, dirs, files in os.walk(folder):
	for file in files:
		if file != ".git" and file != "LICENSE" and file != "README.md":
			fn = os.path.join(base, file)
			zfile.write(fn, fn[rootlen:])
zfile.close()

curl = pycurl.Curl()
curl.setopt(pycurl.POST, 1)
curl.setopt(pycurl.URL, url)
curl.setopt(pycurl.HTTPPOST, [("mysubmit", "Install"), ("archive", (curl.FORM_FILE, "channel.zip"))])
curl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_DIGEST)
curl.setopt(pycurl.USERNAME, username)
curl.setopt(pycurl.PASSWORD, password)
curl.perform()

os.remove("channel.zip")
