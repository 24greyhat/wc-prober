import requests
import sys



print("\n(Wildcards Prober)\n")


class Probe:
    def __init__(self, url):
        self.url = url


        print(f"\n\n\n\nProbing: [{url}]\t")

        self.options()
        self.get()
        self.post()
        self.put()
        self.put()
        print(f"\n\n\n\n")

    def options(self):
        try:
            r = requests.options(self.url)

            print("\nHTTP: (OPTIONS)")

            for k,v in r.headers.items():
                print(f"\n\t{k}\t{v}")
        except Exception:
            print("[-] request failed!")


    def get(self):

        try:
            r = requests.get(self.url)
            
            print("\nHTTP: (GET)")


            for k,v in r.headers.items():
                print(f"\n\t{k}\t\t{v}")
        except Exception:
            print("[-] request failed!")



    def post(self):
        try:
            r = requests.post(self.url)
     
            print("\nHTTP: (POST)")

            for k,v in r.headers.items():
                print(f"\t{k}\t\t{v}")
        except Exception:
            print("[-] request failed!")


    def put(self):
        try:

            r = requests.put(self.url)

            print("\nHTTP: (PUT)")

            for k,v in r.headers.items():
                print(f"\t{k}\t\t{v}")

        except Exception:
            print("[-] request failed!")



    def patch(self):
        try:
            r = requests.patch(self.url)

            print("\nHTTP: (PATCH)")

            for k,v in r.headers.items():
                print(f"\t{k}\t\t{v}")

        except Exception:
            print("[-] request failed!")



    def delete(self):
        try:
            r = requests.delete(self.url)

            print("\nHTTP: (DELETE)")

            for k,v in r.headers.items():
                print(f"\t{k}\t\t{v}")

        except Exception:
            print("[-] request failed!")



data = sys.stdin.read().split()

for i in data:
    Probe(i)
