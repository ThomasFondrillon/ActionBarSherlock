#!/usr/bin/env python

import os
import re

repo = os.path.dirname(os.path.realpath(__file__))

code = 'android:versionCode="%s"'
name = 'android:versionName="%s"'
in_code = code % r'(\d+)'
in_name = name % r'([^"]+)'
new_code = None
new_name = None

for dirpath, dirnames, filenames in os.walk(repo):
    for filename in filenames:
        if filename == 'AndroidManifest.xml':
            filepath = os.path.join(dirpath, filename)
            with open(filepath) as f:
                contents = f.read()
            if new_code is None:
                print('Current version code: ' + re.search(in_code, contents).group(1))
                new_code = raw_input('New version code: ')
                print('Current version name: ' + re.search(in_name, contents).group(1))
                new_name = raw_input('New version name: ')
            contents = re.sub(in_code, code % new_code, contents)
            contents = re.sub(in_name, name % new_name, contents)
            with open(filepath, 'w') as f:
                f.write(contents)
