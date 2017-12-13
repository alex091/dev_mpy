import argparse
import concurrent.futures
import hashlib
import os


def calc_hash(file):
    f_hash = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            f_hash.update(data)
    return f_hash.hexdigest()


if __name__ == '__main__':
    usage = "--narg [files]"
    workers = os.cpu_count() * 2 + 1

    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('--nargs', nargs='+', action="store",
                        dest="files",
                        help="Use --nargs files ")
    files = parser.parse_args().files

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        future_to_hash = {executor.submit(calc_hash, file): file for file in files}
        for future in concurrent.futures.as_completed(future_to_hash):
            f_hash = future_to_hash[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (f_hash, exc))
            else:
                print('hash for %s is %s' % (f_hash, data))
