import sys
from packaging.version import Version


def verify_version(last_version, current_version):
    if not (last_version < current_version):
        print('New version needs to be higher than old version')
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    verify_version(Version(sys.argv[1]), Version(sys.argv[2]))
