# mebac
Media backup and sorting using exif metadata.

The utility recursively scans the source locations and makes the backup of the media files to specified destination.<br>
It structures the destination directories using the information from the media metadata, i.e.<br><br>
If the <code>mebac.conf</code> configuration is as following:<br>
<code>/src1/path</code><br>
<code>/src2/path</code> <br>
<code>/destination/path</code> <br><br>
Then, on the first run, the tool will create additional two directories to separate photos and videos<br>
<code>/destination/path/photos</code><br>
<code>/destination/path/videos</code> <br><br>
In addition, the creation date from the media metadata will be used for backup directory structure, i.e.<br>
<code>/destination/path/photos/2016/05/</code><br>
<code>/destination/path/videos/2015/03</code><br>
<code>etc.</code>

# Installation
On RHEL/CentOS simply build an rpm using supplied <code>"mebac.spec"</code> file and install.

On other systems edit <code>mebac</code> and <code>mebac-conf</code> scripts to point to the correct location of <code>mebac.conf</code> file.<br>
i.e.<br>
Replace <code>/var/lib/mebac/mebac.conf</code> with the value matching the location on your system.

# Usage
Run: <code>mebac-config</code> to configure locations<br>
Run: <code>mebac</code> to start the backup.

