from watchman import WatchmanApp
from pyuac import main_requires_admin


@main_requires_admin
def main():
    WatchmanApp()


if __name__ == "__main__":
    main()
