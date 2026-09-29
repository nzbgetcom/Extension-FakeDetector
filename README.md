> **Note:** this repo is a fork of the original github [project](https://github.com/nzbget/FakeDetector)
> made by @hugbug.

## NZBGet Versions

- stable v23+ [v3.1](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v3.1)
- legacy v22 [v2.0](https://github.com/nzbgetcom/Extension-FakeDetector/releases/tag/v2.0)

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

## When detection happens

- **When the nzb is added to the queue**: the file names listed in the nzb are checked, so a download whose listed files include a banned extension (option `BannedExtensions`), or both media files and executables, is marked bad before anything is downloaded.
- **During download**: rar-archive volumes are listed (without unpacking) as they arrive; the last volume is moved to the top of the queue so this happens early.
- **After download**: the downloaded and unpacked files are checked.

Obfuscated posts only reveal their real file names after par-repair renaming, so for those the checks during and after download still apply.
