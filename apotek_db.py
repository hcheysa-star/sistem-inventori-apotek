
import configparser
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
FILE_LINGKUNGAN_AKTIF = FOLDER / "lingkungan_aktif.txt"


def baca_konfigurasi():
    if not FILE_LINGKUNGAN_AKTIF.exists():
        raise FileNotFoundError(
            "File lingkungan_aktif.txt belum tersedia."
        )

    with open(FILE_LINGKUNGAN_AKTIF, "r", encoding="utf-8") as file:
        lingkungan = file.read().strip()

    if lingkungan not in ["dev", "staging", "prod"]:
        raise ValueError("Nama environment tidak valid.")

    file_config = FOLDER / f"config_{lingkungan}.ini"

    config = configparser.ConfigParser()
    if not config.read(file_config, encoding="utf-8"):
        raise FileNotFoundError(
            f"File {file_config.name} tidak ditemukan."
        )

    return lingkungan, config
