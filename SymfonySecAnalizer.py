# Standard libraries
import argparse

# Third-party imports
import requests
from requests.exceptions import RequestException

# Local application imports
from config import tests


def get_symfony_version(response_headers: requests.structures.CaseInsensitiveDict
                        ) -> str | None:
    """
    Función para obtener la versión de Symfony mediante los headers.
    """
    version = response_headers.get("X-Symfony-Version", None)
    if version:
        print(f"Symfony Version Detected: {version}")
        return version
    else:
        print("No Symfony version detected in headers.")
        return None


def run_tests(url: str, 
              test_paths: dict[str, str]
              ) -> dict:
    """
    Función para realizar las pruebas.

    Args:
        url (str):
            String of URL that you want to test.
        test_paths (dict[str, str]):
            Test paths to test as defined in the `config.py` file.
    
    Returns:
        A dictionary, that is either empty (if no test files / paths were 
        detected) or full of the found files / paths. 
    """
    results = {}
    for test, path in test_paths.items():
        test_url = f"{url.rstrip('/')}{path}"
        try:
            response = requests.get(test_url, timeout=5)
            if response.status_code == 200:
                print(f"[+] {test} found at {test_url}")
                results[test] = test_url
            else:
                print(f"[-] {test} not found at {test_url}")
        except RequestException as e:
            print(f"[!] Error testing {test_url}: {e}")
    return results


# Ejecución del POC
if __name__ == '__main__':
    # Parse arguments from the cmd line
    parser = argparse.ArgumentParser(
        description = "Run the program like this: `python SymfonySecAnalizer.py -u https://example.com`"
    )
    parser.add_argument(
        '-u',
        '--url',
        help = 'Put the desired URL here',
        type = str,
        required = True
    )
    args = parser.parse_args()
    target_url = args.url
    print(f'You are checking the following URL: {target_url}')
    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            print("Target is reachable.")
            version = get_symfony_version(response.headers)
            results = run_tests(target_url, tests)
            print("\nTest Results:")
            for test, url in results.items():
                print(f"{test}: {url}")
        else:
            print("Failed to reach the target.")
    except RequestException as e:
        print(f"Failed to connect to target: {e}")
