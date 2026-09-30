import subprocess
import os
import pysus

CATALOG = "sih_sus_oncologia"
SCHEMA = "bronze"
VOLUME = "raw_files"

def upload_para_volume(local_path, filename):
    destino = f"dbfs:/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}/{filename}"
    subprocess.run(
        ["databricks", "fs", "cp", local_path, destino, "--overwrite"],
        check=True
    )

def extrair_snapshot_cnes(uf, ano):
    bag = pysus.ftp.cnes(state=uf, year=ano, month=[12], group="ST")

    for f in bag:
        upload_para_volume(f.path, f.name)
        os.remove(f.path)

    return len(bag)

if __name__ == "__main__":
    UF = "AM"
    ANOS = [2019, 2020, 2021, 2022, 2023]

    for ano in ANOS:
        qtd = extrair_snapshot_cnes(UF, ano)
        print(f"CNES {UF}/{ano} (snapshot dezembro): {qtd} arquivo(s) enviado(s)")

    print("\nExtracao CNES finalizada.")