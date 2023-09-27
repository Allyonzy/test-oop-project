import numpy as np
import lib
from lib.hero import Hero

if __name__ == "__main__":
    text = f"Версия numpy {np.__version__}"
    print(text)

    elven_test = Hero()
    print(elven_test.__str__())