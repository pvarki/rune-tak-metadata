#!/usr/bin/python3

import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Merge translation files.')
    parser.add_argument('-t', '--template', help='Translation template file', required=True)
    parser.add_argument('-s', '--source', help='Source translation file', required=True)
    parser.add_argument('-o', '--output', help='Output file (defaults to template file).', default=None)

    args = parser.parse_args()

    template_name = args.template
    source_name = args.source
    output_file = args.output if args.output else template_name

    with open(template_name, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)

    with open(source_name, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    for key in data1:
        if key in data2:
            data1[key] = data2[key]

    with open(output_file, 'w', encoding='utf-8') as f_out:
        json.dump(data1, f_out, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
