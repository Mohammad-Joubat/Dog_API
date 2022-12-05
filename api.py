import json
from random import choice
from urllib import request as urlrequest, parse as urlparse


def api_request(endpoint="breeds/list"):
    return json.loads(urlrequest.urlopen(
        urlparse.urljoin("https://dog.ceo/api/", endpoint)
    ).read().decode("utf-8"))


def list_dogs():
    return api_request("breeds/list")


def random(breed, subbreed):
    if breed is None:
        return api_request("breeds/image/random".format(breed))
    if subbreed is None:
        return api_request("breed/{}/images/random".format(breed))
    else:
        return api_request("breed/{}/{}/images/random".format(breed, subbreed))


def list_images(breed, subbreed):
    if subbreed is None:
        return api_request("breed/{}/images".format(breed))
    else:
        return api_request("breed/{}/{}/images".format(breed, subbreed))


if __name__ == "__main__":
    breeds = list_dogs()
    # Dog types in list
    list_breeds = breeds['message']
    choice_list_breeds = choice(list_breeds)
    print("Types OF Dogs --> \n", breeds, "\n")
    print("Random Choice Breeds --> \n", random(None, None), "\n")
    print("Random Choice SUB_Breeds-->\n", list_images(choice_list_breeds, None))