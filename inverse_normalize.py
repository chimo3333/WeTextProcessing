# Copyright (c) 2022 Xingchen Song (sxc19@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

# TODO(xcsong): multi-language support
from itn.chinese.inverse_normalizer import InverseNormalizer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', help='input string')
    parser.add_argument('--file', help='input file path')
    parser.add_argument('--overwrite_cache', action='store_true',
                        help='rebuild *.far')
    args = parser.parse_args()

    normalizer = InverseNormalizer(
        cache_dir='itn', overwrite_cache=args.overwrite_cache,
        enable_standalone_number=True)

    if args.text:
        print(normalizer.tag(args.text))
        print(normalizer.normalize(args.text))
    elif args.file:
        with open(args.file) as fin:
            for line in fin:
                print(normalizer.tag(line.strip()))
                print(normalizer.normalize(line.strip()))


if __name__ == '__main__':
    main()
