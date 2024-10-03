import requests
import json
import logging
import getpass

key = 'ec1e2ebed1754f1b8c00f2b90aa15906'
headers = {
    'content-type': 'application/json',
    'api-version': '3',
    'User-Agent': 'python',
    'hibp-api-key': key
}

def main():
    try:
        email = input("Ingrese el correo a investigar: ")
        url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'
        response = requests.get(url, headers=headers)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        logging.basicConfig(filename='hibpERROR.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S %p",
                            level=logging.ERROR)
        logging.error(f"Error en la solicitud a la API: {e}")
        pass
    else:
        try:
            data = response.json()
            encontrados = len(data)

            if encontrados > 0:
                for filtracion in data:
                    print(filtracion["Name"])
            else:
                print(f"El correo {email} no ha sido filtrado")

            msg = f"{email} Filtraciones encontradas: {encontrados}"
            logging.basicConfig(filename='hibpINFO.log',
                                format="%(asctime)s %(message)s",
                                datefmt="%m/%d/%Y %I:%M:%S %p",
                                level=logging.INFO)
            logging.info(msg)
        
        except json.JSONDecodeError as e:
            logging.basicConfig(filename='hibpERROR.log',
                                format="%(asctime)s %(message)s",
                                datefmt="%m/%d/%Y %H:%M:%S %p",
                                level=logging.ERROR)
            logging.error(f"Error al decodificar la respuesta JSON: {e}")
            pass
        
        except KeyError as e:
            logging.basicConfig(filename='hibpERROR.log',
                                format="%(asctime)s %(message)s",
                                datefmt="%m/%d/%Y %H:%M:%S %p",
                                level=logging.ERROR)
            logging.error(f"Clave faltante en la respuesta: {e}")
            pass
        
    finally:
        print("Proceso terminado.")

if __name__ == "__main__":
    main()