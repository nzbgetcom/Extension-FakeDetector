> **Note:** this repo is a fork of the original github [project](https://github.com/nzbget/FakeDetector)
> made by @hugbug.

## NZBGet Versions

- pre-release v23+  [v3.0](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v3.0)
- stable  v22 [v2.0](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v2.0)
- legacy  v21 [v2.0](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v2.0)

> **Note:** This script is compatible with python 3.8.x and above. 
If you need support for Python 2.x or older Python3.x versions please use [v1.7](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v1.7) release.


# FakeDetector
Fake detection [script](https://nzbget.com/documentation/extension-scripts/) for [NZBGet](https://nzbget.com).

Authors:
- Andrey Prygunkov <hugbug@users.sourceforge.net>
- Clinton Hall <clintonhall@users.sourceforge.net>
- JVM <jvmed@users.sourceforge.net>

Detects nzbs with fake media files. If a fake is detected the download is marked as bad. NZBGet removes the download from queue and (if option "DeleteCleanupDisk" is active) the downloaded files are deleted from disk. If duplicate handling is active (option "DupeCheck") then another duplicate is chosen for download if available.

The status "FAILURE/BAD" is passed to other scripts and informs them about failure.
