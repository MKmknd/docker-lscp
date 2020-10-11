import argparse
import os
import sys
import subprocess
import glob
import pickle

def dump_pickle(f_name, data):

    with open(f_name, "wb") as f:
        pickle.dump(data, f)


def load_pickle(f_name):

    with open(f_name, "rb") as f:
        data = pickle.load(f)

    return data


def use_lscp(snippet):
    with open('/home/work_dir/tmp/in/snippet.txt', 'w') as f:
        f.write(snippet)
    out = subprocess.check_output(['/home/work_dir/lscp_templates/lscp.pl'], stderr=subprocess.STDOUT).decode('utf-8', errors='ignore')
    # if the result is 'regular subexpression recursion limit (32766) exceed'
    if 'limit' in out:
        raise
    with open('/home/work_dir/tmp/out/snippet.txt', 'r') as f:
        result = ' '.join(f.read().splitlines()) # separate the output
    return result


def main():
    if not os.path.exists('/home/work_dir/tmp'):
        os.mkdir('/home/work_dir/tmp')
        os.mkdir('/home/work_dir/tmp/in')
        os.mkdir('/home/work_dir/tmp/out')

    file_list = glob.glob("/home/work_dir/diff_code/*.pickle")

    for f_path in file_list:

        snippet = load_pickle(f_path)

        paths = f_path.split("/")
        output_path = "/".join(paths[:-1]) + "/lscp_" + paths[-1]

        try:
            dump_pickle(output_path, use_lscp(snippet))
        except Exception:
            print('lscp failed at', f_path)


if __name__ == "__main__":
    main()
