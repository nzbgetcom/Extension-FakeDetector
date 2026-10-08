> **Note:** this repo is a fork of the original github [project](https://github.com/nzbget/FakeDetector)
> made by @hugbug.

## Requirements

- NZBGet v23+ and Python 3.8+
- Legacy NZBGet v22: use v2.0 release
- Python 3.7 or older: use v1.7 release

# FakeDetector
Fake detection [script](https://nzbget.com/documentation/extension-scripts/) for [NZBGet](https://nzbget.com).

Authors:
- Andrey Prygunkov <hugbug@users.sourceforge.net>
- Clinton Hall <clintonhall@users.sourceforge.net>
- JVM <jvmed@users.sourceforge.net>

Detects nzbs with fake media files. If a fake is detected the download is marked as bad. NZBGet removes the download from queue and (if option "DeleteCleanupDisk" is active) the downloaded files are deleted from disk. If duplicate handling is active (option "DupeCheck") then another duplicate is chosen for download if available.

The status "FAILURE/BAD" is passed to other scripts and informs them about failure.

## Installation

  - Download the newest version from [releases page](https://github.com/nzbgetcom/Extension-FakeDetector/releases).
  - Unpack into pp-scripts directory. Your pp-scripts directory now should have folder "FakeDetector" with file "main.py";
  - Open settings tab in NZBGet web-interface and define settings for FakeDetector;
  - Save changes and restart NZBGet.

## Options

### BannedExtensions

Downloads which contain files with any of the following extensions will be marked as fake.
Extensions must be separated by a comma (eg: .wmv, .divx). Matching is case-insensitive.

The file names listed in the nzb are checked as soon as it is added to the queue,
so a banned file posted as-is is rejected before anything is downloaded.
Files inside archives are checked as the archive volumes are downloaded.

## When detection happens

- **When the nzb is added to the queue**: the file names listed in the nzb are checked, so a download whose listed files include a banned extension (option `BannedExtensions`), or both media files and executables, is marked bad before anything is downloaded.
- **During download**: rar-archive volumes are listed (without unpacking) as they arrive; the last volume is moved to the top of the queue so this happens early.
- **After download**: the downloaded and unpacked files are checked.

Obfuscated posts only reveal their real file names after par-repair renaming, so for those the checks during and after download still apply.

## Credits

This script is part of the [NZBGet](https://nzbget.com) project.
