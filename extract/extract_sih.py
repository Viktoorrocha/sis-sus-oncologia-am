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

def extrair_e_subir(uf, ano):
    meses = list(range(1, 13))
    bag = pysus.ftp.sih(state=uf, year=ano, month=meses)
    arquivos_rd = [f for f in bag if f.name.startswith("RD")]
    print(f"{uf}/{ano}: {len(arquivos_rd)} arquivos RD encontrados")

    for f in arquivos_rd:
        print(f"  subindo {f.name}...")
        upload_para_volume(f.path, f.name)
        os.remove(f.path)

    print(f"{uf}/{ano}: concluído")

if __name__ == "__main__":
    UFS = ["SP"]
    ANOS = [2019, 2020, 2021, 2022, 2023]

    for uf in UFS:
        for ano in ANOS:
            extrair_e_subir(uf, ano)