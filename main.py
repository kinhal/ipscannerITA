import socket
import requests
import os
import ipaddress
from colorama import Fore, Style # type: ignore

ip = input(Fore.LIGHTRED_EX + "Inserisci l'ip da anaizzare: " + Style.RESET_ALL)

def ip_scanner(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        print(Fore.LIGHTRED_EX +f"L'hostname di {ip} è: ", str(hostname) + Style.RESET_ALL)
    except socket.error:
        print(Fore.RED +"Non sono riuscito a trovare l'hostname." + Style.RESET_ALL)
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.is_private:
                print(Fore.RED +"L'ip è privato." + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX +"L'ip è pubblico." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED +"Ip invalido." + Style.RESET_ALL)
            
def os_info(ip):
    try:
        os_info = os.name
        print(Fore.LIGHTRED_EX +f"L'OS Name di {ip} è: ", str(os_info) + Style.RESET_ALL)
    except OSError:
        print(Fore.RED +"Errore." + Style.RESET_ALL)
        
def localization(ip_address):
    try:
        r = requests.get(f'https://ipapi.co/{ip_address}/json/', timeout=5)
        if r.status_code == 200:
            data = r.json()
            postal = data.get('postal', 'N/A')
            city = data.get('city', 'N/A')
            loc = data.get('loc')
            print(Fore.LIGHTRED_EX + f"Codice Postale: {postal}" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + f"Città: {city}" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + f"Google Maps Link: https://www.google.com/maps/search/?api=1&query={loc}" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "WARNING: Il link di Google Maps non è al 100% valido.." + Style.RESET_ALL)
    except requests.exceptions.ConnectionError:
            print(Fore.RED +"Errore." + Style.RESET_ALL)
          
if __name__ == "__main__":
    ip_scanner(ip)
    os_info(ip)
    localization(ip)
    input("\nPremi invio per uscire dal tool.")