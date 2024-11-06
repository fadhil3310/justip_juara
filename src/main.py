import asyncio
import sys
import shared.geolocation as geo
import shared.panic as pa


def main():
    # Tes dapet lokasi
    asyncio.run(geo.report())

if __name__ == "__main__":
    # Bypass exception handling dahulu karena masih dalam tahap pengembangan
    # pa.bypass_handling = True
    sys.excepthook = pa.except_hook
    main()