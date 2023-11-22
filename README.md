> **Note:** this repo is a fork of the original github [project](https://github.com/nzbget/FakeDetector)
> made by @hugbug.

> **Note:** This script is compatible with python 3.9.x and above. 

> **Note:** If you need support for Python 2.x or older Python3.x versions please use [v1.7](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v1.7) release.

> **Note:** [Here](https://github.com/nzbgetcom/nzbget/discussions/56) you can discuss problems with different versions of Python.

# FakeDetector
Fake detection [script](https://nzbget.com/documentation/extension-scripts/) for [NZBGet](https://nzbget.com).

Authors:
- Andrey Prygunkov <hugbug@users.sourceforge.net>
- Clinton Hall <clintonhall@users.sourceforge.net>
- JVM <jvmed@users.sourceforge.net>

Detects nzbs with fake media files. If a fake is detected the download is marked as bad. NZBGet removes the download from queue and (if option "DeleteCleanupDisk" is active) the downloaded files are deleted from disk. If duplicate handling is active (option "DupeCheck") then another duplicate is chosen for download if available.

The status "FAILURE/BAD" is passed to other scripts and informs them about failure.

For more info and support please visit forum topic [PP-Script FakeDetector](http://nzbget.net/forum/viewtopic.php?f=8&t=1394).
